from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.shortcuts import render
from psycopg2.extensions import JSON
from .models import Toilet

from . import models
# Create your views here.


def update_location(request):
    try:
        user_profile = models.Profile.objects.get(user=request.user)
        if not user_profile:
            raise ValueError("Can't get User details")
        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)
        user_profile.location = point
        user_profile.save()
        return JsonResponse({"message": f"Set location to {point.wkt}."}, status=200)
    except Exception as e:
        return JsonResponse({"message": JSON.stringify(e)},status=400)


def home(request):
    toilets = Toilet.objects.all().values
    return render(request, "home.html", {"toilets": toilets})
