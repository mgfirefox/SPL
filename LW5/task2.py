import numpy
import pandas


def start():
    data = pandas.read_csv("test.csv", sep=",", nrows=1000)

    data = data.fillna({"Id": 0, "DistrictId": 0, "Rooms": 0., "Square": 0., "LifeSquare": 0., "KitchenSquare": 0.,
                        "Floor": 0, "HouseFloor": 0., "HouseYear": 0, "Ecology_1": 0., "Ecology_2": "Unspecified",
                        "Ecology_3": "Unspecified", "Social_1": 0, "Social_2": 0, "Social_3": 0, "Healthcare_1": 0.,
                        "Healthcare_2": 0, "Shops_1": 0, "Shops_2": "Unspecified"})

    n_rooms_flats_amount = []
    for i in range(int(numpy.max(data["Rooms"])) + 1):
        n_rooms_flats_amount.append(0)

    for rooms_item in data["Rooms"]:
        n_rooms_flats_amount[int(rooms_item)] += 1

    each_district_flats_amount = pandas.pivot_table(
        data, index="DistrictId", columns="Rooms", aggfunc="count", fill_value=0).iloc[:, 0:7].copy()

    print(each_district_flats_amount)
    print(n_rooms_flats_amount)
