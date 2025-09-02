from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Populate database with sample products'

    def handle(self, *args, **options):
        # Clear existing products
        Product.objects.all().delete()
        
        sample_products = [
            {
                'name': 'Wireless Bluetooth Headphones',
                'description': 'Premium quality wireless Bluetooth headphones with noise cancellation and 30-hour battery life. Perfect for music lovers and professionals.',
                'price': 2999.00
            },
            {
                'name': 'Smart Fitness Watch',
                'description': 'Track your fitness goals with this advanced smartwatch featuring heart rate monitoring, GPS, and waterproof design.',
                'price': 5999.00
            },
            {
                'name': 'Laptop Stand Adjustable',
                'description': 'Ergonomic aluminum laptop stand that adjusts to multiple angles. Improves posture and provides better ventilation for your laptop.',
                'price': 1299.00
            },
            {
                'name': 'USB-C Fast Charger',
                'description': '65W USB-C fast charger compatible with laptops, smartphones, and tablets. Compact design perfect for travel.',
                'price': 899.00
            },
            {
                'name': 'Mechanical Gaming Keyboard',
                'description': 'RGB mechanical gaming keyboard with customizable keys and tactile feedback. Perfect for gaming and typing enthusiasts.',
                'price': 3499.00
            },
            {
                'name': 'Wireless Mouse Precision',
                'description': 'High-precision wireless mouse with ergonomic design and long battery life. Ideal for both work and gaming.',
                'price': 1599.00
            },
            {
                'name': 'Phone Camera Lens Kit',
                'description': 'Professional camera lens kit for smartphones including wide-angle, macro, and fisheye lenses with carrying case.',
                'price': 2199.00
            },
            {
                'name': 'Portable Power Bank',
                'description': '20000mAh portable power bank with fast charging support and multiple USB ports. Never run out of battery again.',
                'price': 1799.00
            },
            {
                'name': 'Bluetooth Speaker Waterproof',
                'description': 'Waterproof Bluetooth speaker with 360-degree sound and 12-hour battery life. Perfect for outdoor adventures.',
                'price': 2499.00
            },
            {
                'name': 'LED Desk Lamp Smart',
                'description': 'Smart LED desk lamp with adjustable brightness, color temperature control, and USB charging port.',
                'price': 1999.00
            }
        ]

        for product_data in sample_products:
            product = Product.objects.create(**product_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created product: {product.name}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated {len(sample_products)} products')
        )