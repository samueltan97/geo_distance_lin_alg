import requests
import math


class Location:

    def __init__(self, data):
        self.latitude = data['lat']
        self.longitude = data['lng']


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
    addresses = address_to_long_lat(["1325-1399 Diamond St, Philadelphia, PA 19122, USA",
                                     "Broad St & York St, Philadelphia, PA 19132, United States"])
    print(develop_orthogonal_vector(Location(addresses[0]), Location(addresses[1])))
