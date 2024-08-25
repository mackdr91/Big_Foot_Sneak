# generate_qr_codes.py
import qrcode
from .models import Sneaker
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Sneaker)
def generate_qr_codes():
    sneakers = Sneaker.objects.all()
    for sneaker in sneakers:
        data = f"http://yourdomain.com/sneaker/{sneaker.id}/"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save(f"qrcodes/sneaker_{sneaker.id}.png")
        return f"qrcodes/sneaker_{sneaker.id}.png"


