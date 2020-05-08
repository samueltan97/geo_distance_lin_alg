from math import radians, sin, asin, sqrt, atan2, cos
import numpy as np
import requests
import os
import pandas as pd
from preprocess import Location, address_to_long_lat, develop_orthogonal_vector


def calculate_manhattan_distance(origin: Location, point: Location, orthogonal_vectors):
    # convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians,
                                 [origin.latitude, origin.longitude, point.latitude,
                                  point.longitude])
    v1, v2 = orthogonal_vectors
    i_hat = v1
    j_hat = v2
    a = np.array([[i_hat[0], j_hat[0]], [i_hat[1], j_hat[1]]])
    print('a', a)
    print(lon1, lat1, lon2, lat2)
    b = np.array([lon2 - lon1, lat2 - lat1])
    print('b', b)
    x = (np.linalg.solve(a, b)).tolist()
    print(x)
    mid_point = [i_hat[0] * x[0] + lon1, i_hat[1] * x[0] + lat1]
    return abs(haversine(lon1, lat1, mid_point[0], mid_point[1])) + abs(
        haversine(mid_point[0], mid_point[1], lon2, lat2))


def haversine(lon1, lat1, lon2, lat2):
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3956
    return c * r

if __name__ == "__main__":
    addresses = address_to_long_lat(["Reading Terminal Market, PA, US",
                                     "Race Street Pier, Philadelphia, PA, US",
                                     "Pennsylvania Convention Center, Philadelphia, PA, US",
                                     "12/13th & Locust Street Station, Philadelphia, PA, US"])
    vectors = (develop_orthogonal_vector(Location(addresses[2]), Location(addresses[3])))
    print(vectors)
    print(calculate_manhattan_distance(Location(addresses[0]), Location(addresses[1]), vectors))