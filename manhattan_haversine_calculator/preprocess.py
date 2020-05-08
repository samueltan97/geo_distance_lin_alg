from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import os
import math
import requests


class Location:

    def __init__(self, data):
        self.latitude = data['lat']
        self.longitude = data['lng']


def zip_code_to_long_lat(addresses):
    geolocator = Nominatim(user_agent="geocoding", timeout=2)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=3)
    location = []
    for address in addresses:
        print(address)
        location.append(geolocator.geocode(address))
    print(location)
    return location



def address_to_long_lat(addresses):
    location = []
    for address in addresses:
        URL = "https://maps.googleapis.com/maps/api/geocode/json"
        PARAMS = {'address': address, 'key': "AIzaSyB6I4zkyEG1G-1MSglJJH2VSYDnLg5g444"}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        location.append(data["results"][0]["geometry"]["location"])
    return location


def develop_orthogonal_vector(origin: Location, point: Location):
    dlng = point.longitude - origin.longitude
    dlat = point.latitude - origin.latitude
    x = dlng / math.sqrt(dlng ** 2 + dlat ** 2)
    y = dlat / math.sqrt(dlng ** 2 + dlat ** 2)
    v1 = (x, y)
    v2 = (0 * x + -1 * y, 1 * x + 0 * y)
    return v1, v2


if __name__ == "__main__":
    addresses = address_to_long_lat(["Reading Terminal Market, PA, US",
                                     "Race Street Pier, Philadelphia, PA, US",
                                     "Pennsylvania Convention Center, Philadelphia, PA, US",
                                     "12/13th & Locust Street Station, Philadelphia, PA, US"])
    print(addresses)
    print(develop_orthogonal_vector(Location(addresses[2]), Location(addresses[3])))
    # URL = "https://maps.googleapis.com/maps/api/geocode/json"
    # PARAMS = {'address': "1325-1399 Diamond St, Philadelphia, PA 19122, USA"}
    # r = requests.get(url=URL, params=PARAMS)
