from django.core.management.base import BaseCommand
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Populate database with sample categories and update products'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Electronic devices and accessories'},
            {'name': 'Audio', 'description': 'Audio equipment and accessories'},
            {'name': 'Computer Accessories', 'description': 'Computer peripherals and accessories'},
            {'name': 'Mobile Accessories', 'description': 'Smartphone and mobile device accessories'},
            {'name': 'Gaming', 'description': 'Gaming peripherals and accessories'},
            {'name': 'Power & Charging', 'description': 'Power banks, chargers, and power accessories'},
            {'name': 'Home & Office', 'description': 'Home and office equipment'},
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )

        # Get categories for assignment
        electronics = Category.objects.get(name='Electronics')
        audio = Category.objects.get(name='Audio')
        computer = Category.objects.get(name='Computer Accessories')
        mobile = Category.objects.get(name='Mobile Accessories')
        gaming = Category.objects.get(name='Gaming')
        power = Category.objects.get(name='Power & Charging')
        home = Category.objects.get(name='Home & Office')

        # Update products with categories
        product_categories = {
            'Wireless Bluetooth Headphones': audio,
            'Smart Fitness Watch': electronics,
            'Laptop Stand Adjustable': computer,
            'USB-C Fast Charger': power,
            'Mechanical Gaming Keyboard': gaming,
            'Wireless Mouse Precision': computer,
            'Phone Camera Lens Kit': mobile,
            'Portable Power Bank': power,
            'Bluetooth Speaker Waterproof': audio,
            'LED Desk Lamp Smart': home,
        }

        for product_name, category in product_categories.items():
            try:
                product = Product.objects.get(name=product_name)
                product.category = category
                product.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Updated {product.name} -> {category.name}')
                )
            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Product not found: {product_name}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated categories and updated products')
        )