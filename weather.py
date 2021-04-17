from geopy.geocoders import Nominatim
import requests
gn = geocoders.GeoNames()
def get(address):
  coords = gn.geocode(address)[1]
  html = requests.get("http://www.7timer.info/bin/astro.php?lon={}&lat={}&ac=0&unit=metric&output=json&tzshift=0".format(coords[0],coords[1])).content.get()
  print(html)
get("Kansas City, KS")
from geopy.geocoders import Nominatim
>>> geolocator = Nominatim(user_agent="specify_your_app_name_here")
>>> location = geolocator.geocode("175 5th Avenue NYC")
>>> print(location.address)
Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
>>> print((location.latitude, location.longitude))
(40.7410861, -73.9896297241625)
>>> print(location.raw)
{'place_id': '9167009604', 'type': 'attraction', ...}
