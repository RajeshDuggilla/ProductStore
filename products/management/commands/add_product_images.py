from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Add images to existing products'

    def handle(self, *args, **options):
        # Image mappings for products
        product_images = {
            'Wireless Bluetooth Headphones': 'products/wireless-bluetooth-headphones.png',
            'Smart Fitness Watch': 'products/smart-fitness-watch.png',
            'Laptop Stand Adjustable': 'products/laptop-stand-adjustable.png',
            'USB-C Fast Charger': 'products/usb-c-fast-charger.png',
            'Mechanical Gaming Keyboard': 'products/mechanical-gaming-keyboard.png',
            'Wireless Mouse Precision': 'products/wireless-mouse-precision.png',
            'Phone Camera Lens Kit': 'products/phone-camera-lens-kit.png',
            'Portable Power Bank': 'products/portable-power-bank.png',
            'Bluetooth Speaker Waterproof': 'products/bluetooth-speaker-waterproof.png',
            'LED Desk Lamp Smart': 'products/led-desk-lamp-smart.png',
        }

        for product_name, image_path in product_images.items():
            try:
                product = Product.objects.get(name=product_name)
                product.image = image_path
                product.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Updated image for: {product.name}')
                )
            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Product not found: {product_name}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully updated product images')
        )