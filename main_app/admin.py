from django.contrib import admin
from .models import Cat , Feeding , Profile

# Register your models here
admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Profile)