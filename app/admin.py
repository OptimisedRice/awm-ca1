from django.contrib.gis import admin
from .models import Profile
# Register your models here.
admin.site.register(Profile, admin.OSMGeoAdmin)
