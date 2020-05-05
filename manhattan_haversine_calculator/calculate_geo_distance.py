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
    i_hat = v1 if abs(v1[0]) > abs(v2[0]) else v2
    j_hat = v2 if abs(v1[0]) > abs(v2[0]) else v1
    a = np.array([[i_hat[0], j_hat[0]], [i_hat[1], j_hat[1]]])
    b = np.array([lon2 - lon1, lat2 - lat1])
    x = (np.linalg.solve(a, b)).tolist()
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
    # api_key = os.environ['API_KEY']
    # path = os.getcwd()
    # census_tracts = pd.read_csv(
    #     path + "\\data\\distance_data\\fatal-overdoses_philadelphia-census-tracts_2017-01_2019-06.csv", index_col=False)
    # mat_location = pd.read_csv(path + "\\data\\distance_data\\geocoded_dbhids_mat-locations_tad-2020-02-28.csv",
    #                            index_col=False)
    # mat_location = mat_location[mat_location['Buprenorphine?'] == "Yes"]
    # census_tract_list = []
    # mat_location_list = []
    # for index, row in census_tracts.iterrows():
    #     print(row['TractNum'])
    #     census_tract_list.append(OverdoseLocation(row['TractNum'], row['INTPTLAT10'], row['INTPTLON10']))
    # for index, row in mat_location.iterrows():
    #     print(row['ProgramName'])
    #     mat_location_list.append(ProviderLocation(row['ProgramName'], row['Zip'], row['latitude'], row['longitude']))
    # for tract in census_tract_list:
    #     for mat in mat_location_list:
    #         print(tract.name, mat.name)
    #         tract.provider_distance[mat.name + "_" + str(mat.zip_code)] = calculate_google_distance(api_key, tract, mat)
    #     tract.calculate_provider_within_range(1.0)
    #     print(tract.provider_within_distance_count, tract.provider_within_distance_names)
    # distance_matrix = pd.DataFrame()
    # distance_matrix['mat_bupe_names'] = [(x.name + "_" + str(x.zip_code)) for x in mat_location_list]
    # print(distance_matrix.tail())
    # for tract in census_tract_list:
    #     print(list(tract.provider_distance.values()))
    #     distance_matrix[tract.name] = list(tract.provider_distance.values())
    # census_tract_provider_count = [x.provider_within_distance_count for x in census_tract_list]
    # census_tract_provider_names = [x.provider_within_distance_names for x in census_tract_list]
    # census_tracts['nearby_bupe_program_count'] = census_tract_provider_count
    # census_tracts['nearby_bupe_program_names'] = census_tract_provider_names
    # census_tracts.to_csv(path + "\\data\\distance_data\\distance_analysis.csv", index=False)
    # distance_matrix.to_csv(path + "\\data\\distance_data\\distance_matrix.csv", index=False)
    addresses = address_to_long_lat(["108 Chambers St, New York, NY 10007, USA",
                                     "30 White St, New York, NY 10013, USA"])
    vectors = (develop_orthogonal_vector(Location(addresses[0]), Location(addresses[1])))
    print(calculate_manhattan_distance(Location({'lat': 40.7257979,'lng': -73.997636}), Location({'lat':40.7332669,'lng':-73.9872548}), vectors))