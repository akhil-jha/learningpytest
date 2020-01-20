# Checking some default/average values for city as "Pune"

import sample3

city = sample3.query_response("Pune")


def test_check_temp():
    avg_temp = 25
    assert city.json()["current"]["temperature"] == avg_temp


def test_check_humidity():
    avg_humidity = 50
    assert city.json()["current"]["humidity"] == avg_humidity


def test_check_region():
    region = "Maharashtra"
    assert city.json()["location"]["region"] == region


def test_check_coordinates():
    x = city.json()["location"]["lat"]
    y = city.json()["location"]["lon"]
    assert (x, y) == ('18.533', '73.867')
