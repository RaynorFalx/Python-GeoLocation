from django import template
from geopy.geocoders import Nominatim
import geocoder


register = template.Library()
geolocator = Nominatim()

@register.filter(name='addstr')
def addstr(arg1, arg2):
    concatenate = str(arg1) + str(arg2)
    str(concatenate)
    return concatenate


@register.filter(name='lat')
def lat(concatenate):
    location = geocoder.google(concatenate)
    lat = location.lat
    return lat

@register.filter(name='lng')
def lng(concatenate):
    location =  geocoder.google(concatenate)
    lng = location.lng
    return lng

