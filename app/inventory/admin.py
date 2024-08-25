from django.contrib import admin

from .models import Size, Sneaker, Location, Collection

# Register your models here.


admin.site.site_header = 'Sneaker Inventory'
admin.site.site_title = 'Sneaker Inventory'
admin.site.index_title = 'Sneaker Inventory'


admin.site.register(Size)
admin.site.register(Sneaker)
admin.site.register(Location)
admin.site.register(Collection)
