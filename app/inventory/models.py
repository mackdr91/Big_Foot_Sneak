from django.db import models
from core.models import Profile
import qrcode
from io import BytesIO
from django.core.files import File


# Create your models here.


class Size(models.Model):
    SIZES = (
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
    )

    size = models.CharField(max_length=2, choices=SIZES, default='9')
    quantity = models.IntegerField(default=0)
    sneaker = models.ForeignKey('Sneaker', on_delete=models.CASCADE, related_name='sizes')


class Location(models.Model):
    store_number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Locations"
        ordering = ['name']

    def __str__(self):
        return self.name


class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    is_new = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', null=True, blank=True)






    def save(self, *args, **kwargs):
        qr_data = f"Name: {self.name}\nBrand: {self.brand}\nColor: {self.color}\nPrice: {self.price}\nDescription: {self.description}\nRelease Date: {self.release_date}\
        \nPurchase Date: {self.purchase_date}\nLocation: {self.location}"
        self.qr_code.save(f"{self.name}_qrcode.png", generate_qr_code(data=qr_data), save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Sneakers"
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.brand}) - ${self.price} - {self.release_date}'



def generate_qr_code(data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return File(buffer, name="qrcode.png")


class Collection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateField(auto_now=True)
    sneaker = models.ManyToManyField('Sneaker', related_name='collections')


