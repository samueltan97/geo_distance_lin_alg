from geocoding import address_to_long_lat
import math

class Location:

    def __init__(self, data):
        self.latitude = data['lat']
        self.longitude = data['lng']
#
# class LocationPair:
#
#     def __init__(self, origin: Location, point:Location, manhattan_dist):
#         self.origin = origin
#         self.point = point
#         self.manhattan_dist = manhattan_dist
#         self.lat_diff = abs(origin.latitude - point.latitude)
#         self.lng_diff = abs(origin.longitude - point.longitude)
#
#     def calculate_angle_relative_to_latlng(self):
#         # asinx + bcosx = c
#         # (a/c)sinx + (b/c)cosx = 1
#         # cosysinx + sinycosx = 1
#         # sin(x+y) = 1
#         # cosy = (self.lat_diff - self.lng_diff)/self.manhattan_dist
#         # siny = (self.lat_diff + self.lng_diff)/self.manhattan_dist
#         beta = math.acos((self.lat_diff - self.lng_diff)/self.manhattan_dist)
#         x = math.asin(1) - beta
#         print(x)
#         return x

def develop_orthogonal_vector(origin: Location, point:Location):
    dlng = point.longitude - origin.longitude
    dlat = point.latitude - origin.latitude
    x = dlng / math.sqrt(dlng**2 + dlat**2)
    y = dlat / math.sqrt(dlng**2 + dlat**2)
    v1 = (x, y)
    v2 = (0*x + -1*y, 1*x + 0*y)
    return v1, v2

if __name__ == "__main__":
    # pair = LocationPair(Location({'lat':39.9893286, 'lng':-75.1555033}), Location({'lat': 39.9913969,'lng':-75.1594955}), 0.480)
    # pair.calculate_angle_relative_to_latlng()
    print((-75.1565118 - -75.1555033)/ math.sqrt((-75.1565118 - -75.1555033) ** 2 + (39.9846699 - 39.9893286)**2),
          (39.9846699 - 39.9893286)/ math.sqrt((-75.1565118 - -75.1555033) ** 2 + (39.9846699 - 39.9893286)**2))

