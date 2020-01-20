"""
Creating a program to collect weather information as per user choice
Using the api provided by weatherstack.com to query the values and storing in \
a global response variable
According to the user's choice, the values can be displayed
"""

import requests


def query_response(city):
    url = "http://api.weatherstack.com/current?access_key=\
    4d7e313e8ed86caa673c2723f4c68d24&query=" + city
    global response
    response = requests.get(url)
    return response


def check_temp():
    return response.json()["current"]["temperature"]


def check_humidity():
    return response.json()["current"]["humidity"]


def check_region():
    return response.json()["location"]["region"]


def check_coordinates():
    x = response.json()["location"]["lat"]
    y = response.json()["location"]["lon"]
    return (x, y)


def main():
    city_name = input("\nEnter city name: ")
    city_name = city_name.title()
    query_response(city_name)
    print("1.Temperature\n2.Humidity\n3.Region\n4.Coordinates\n")
    value = int(input("Please select one of the following: \n"))
    if value == 1:
        print(check_temp())
    elif value == 2:
        print(check_humidity())
    elif value == 3:
        print(check_region())
    elif value == 4:
        print(check_coordinates())
    else:
        print("\nBad value")
        exit(1)


if __name__ == "__main__":
    main()
