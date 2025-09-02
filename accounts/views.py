from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import transaction
from .forms import UserRegistrationForm, UserProfileForm, UserUpdateForm
from .models import UserProfile, Order, OrderItem
from products.models import Product
import uuid
import string
import random

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form, 'title': 'Register'})

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    recent_orders = Order.objects.filter(user=request.user)[:5]
    
    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'recent_orders': recent_orders,
        'title': 'My Profile'
    })

@login_required
def edit_profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
    
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'title': 'Edit Profile'
    })

@login_required
def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/orders.html', {
        'orders': orders,
        'title': 'My Orders'
    })

@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, order_id=order_id, user=request.user)
    return render(request, 'accounts/order_detail.html', {
        'order': order,
        'title': f'Order {order.order_id}'
    })

def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

@login_required
def checkout_authenticated(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty!')
        return redirect('product_list')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        if name and email and phone and address:
            # Calculate total
            total = 0
            for product_id, item in cart.items():
                total += float(item['price']) * item['quantity']
            
            # Create order
            with transaction.atomic():
                order = Order.objects.create(
                    user=request.user,
                    order_id=generate_order_id(),
                    total_amount=total,
                    shipping_name=name,
                    shipping_email=email,
                    shipping_phone=phone,
                    shipping_address=address
                )
                
                # Create order items
                for product_id, item in cart.items():
                    try:
                        product = Product.objects.get(id=product_id)
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            quantity=item['quantity'],
                            price=item['price']
                        )
                    except Product.DoesNotExist:
                        continue
                
                # Clear cart
                request.session['cart'] = {}
                request.session.modified = True
                
                messages.success(request, f'Thank you {name}! Your order {order.order_id} has been placed successfully.')
                return redirect('accounts:order_detail', order_id=order.order_id)
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    # Calculate cart totals
    cart_items = []
    total = 0
    
    for product_id, item in cart.items():
        item_total = float(item['price']) * item['quantity']
        cart_items.append({
            'name': item['name'],
            'price': float(item['price']),
            'quantity': item['quantity'],
            'total': item_total,
        })
        total += item_total
    
    # Pre-fill form with user data
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'cart_items': cart_items,
        'total': total,
        'user_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
        'user_email': request.user.email,
        'user_phone': profile.phone,
        'user_address': profile.address,
        'title': 'Checkout'
    }
    
    return render(request, 'accounts/checkout_authenticated.html', context)
