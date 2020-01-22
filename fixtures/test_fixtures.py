import pytest
import fixtures_file


"""Using fixtures to request the initial data everytime a new test is run.
The scope under fixture defines how many times the fixture will run.
Other scopes include class, module, session"""


@pytest.fixture(scope='function')
# To query the weather details
def get_city_info():
    print("In fixtures")
    global city
    city = fixtures_file.query_response("Delhi")
    yield print("ENDING FIXTURES")


# Test for temperature
def test_check_temp(get_city_info):
    avg_temp = 14
    assert city.json()["current"]["temperature"] == avg_temp


"""Using pytest marker.
To skip the particular test to run and providing the respective reason to it"""


@pytest.mark.skip(reason="Variable")
# Test for humidity
def test_check_humidity(get_city_info):
    avg_humidity = 65
    assert city.json()["current"]["humidity"] == avg_humidity


# Test for region
def test_check_region(get_city_info):
    region = "Delhi"
    assert city.json()["location"]["region"] == region


# Test for coordinates
def test_check_coordinates(get_city_info):
    x = city.json()["location"]["lat"]
    y = city.json()["location"]["lon"]
    assert (x, y) == ('28.667', '77.217')
