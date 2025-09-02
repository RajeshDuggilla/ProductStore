from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category
import json

def home(request):
    featured_products = Product.objects.filter(category__isnull=False)[:6]
    categories = Category.objects.all()
    return render(request, 'products/home.html', {
        'featured_products': featured_products,
        'categories': categories
    })

def product_list(request):
    products = Product.objects.select_related('category').all()
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Category filtering
    category_slug = request.GET.get('category', '')
    selected_category = None
    if category_slug:
        try:
            selected_category = Category.objects.get(slug=category_slug)
            products = products.filter(category=selected_category)
        except Category.DoesNotExist:
            pass
    
    # Price filtering
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    if min_price:
        try:
            products = products.filter(price__gte=float(min_price))
        except ValueError:
            pass
    if max_price:
        try:
            products = products.filter(price__lte=float(max_price))
        except ValueError:
            pass
    
    # Pagination
    paginator = Paginator(products, 8)  # Show 8 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products
    })

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        
        # Get cart from session
        cart = request.session.get('cart', {})
        
        # Add or update product in cart
        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += quantity
        else:
            cart[str(product_id)] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': quantity,
                'slug': product.slug
            }
        
        # Save cart to session
        request.session['cart'] = cart
        request.session.modified = True
        
        messages.success(request, f'{product.name} added to cart!')
        return redirect('product_detail', slug=product.slug)
    
    return redirect('product_list')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    
    for product_id, item in cart.items():
        item_total = float(item['price']) * item['quantity']
        cart_items.append({
            'product_id': product_id,
            'name': item['name'],
            'price': float(item['price']),
            'quantity': item['quantity'],
            'total': item_total,
            'slug': item['slug']
        })
        total += item_total
    
    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def update_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 0))
        
        if str(product_id) in cart:
            if quantity > 0:
                cart[str(product_id)]['quantity'] = quantity
            else:
                del cart[str(product_id)]
            
            request.session['cart'] = cart
            request.session.modified = True
            messages.success(request, 'Cart updated!')
    
    return redirect('cart_view')

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty!')
        return redirect('product_list')
    
    if request.method == 'POST':
        # Process checkout form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        if name and email and phone and address:
            # Clear cart after successful "order"
            request.session['cart'] = {}
            request.session.modified = True
            messages.success(request, f'Thank you {name}! Your order has been placed successfully.')
            return redirect('home')
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
    
    return render(request, 'products/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })
