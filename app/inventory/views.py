from django.shortcuts import render, get_object_or_404
from .models import Sneaker

def sneaker_detail(request, sneaker_id):
    sneaker = get_object_or_404(Sneaker, id=sneaker_id)
    sizes = sneaker.sizes.all()
    return render(request, 'sneaker_detail.html', {'sneaker': sneaker, 'sizes': sizes})




