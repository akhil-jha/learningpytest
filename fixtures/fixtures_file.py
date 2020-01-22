"""Creating a program to collect weather information as per user choice
Using the api provided by weatherstack.com to query the values and storing in
a global response variable
According to the user's choice, the values can be displayed"""


import requests


"""Method query_response() creates a HTTP GET request to the weatherstack.com
via the api and stores the response in a requests.models.Response
object and returning the object to the method call."""


def query_response(city):
    url = "http://api.weatherstack.com/current?access_key="\
           "4d7e313e8ed86caa673c2723f4c68d24&query=" + city
    global response
    response = requests.get(url)
    # print(type(response))
    return response


# To extract the temperature from the response object
def check_temp():
    return response.json()["current"]["temperature"]


# To extract the humidity from the response object
def check_humidity():
    return response.json()["current"]["humidity"]


# To extract the region from the response object
def check_region():
    return response.json()["location"]["region"]


# To extract the coordinates from the response object
def check_coordinates():
    x = response.json()["location"]["lat"]
    y = response.json()["location"]["lon"]
    return x, y


def main():
    city_name = input("\nEnter city name: ")
    # To convert the city name in Camel Case as required by the api
    city_name = city_name.title()
    query_response(city_name)
    print("1.Temperature\n2.Humidity\n3.Region\n4.Coordinates\n")
    value = int(input("Please select one of the following: \n"))
    if value == 1:
        print(check_temp())  # Choice for temperature
    elif value == 2:
        print(check_humidity())  # Choice for humidity
    elif value == 3:
        print(check_region())  # Choice for region
    elif value == 4:
        print(check_coordinates())  # Choice for coordinates
    else:
        print("\nBad value")  # When none of the options enterted
        exit(1)  # Error code


if __name__ == "__main__":
    main()
