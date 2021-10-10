# Importing libraries
import requests
import datetime
import time

if __name__ == '__main__':
    # Getting longitude, latitude and api_key input from user and storing it in a dictionary
    query = dict()
    query['lat'] = input('Enter latitude of the location: ')
    query['lon'] = input('Enter longitude of the location: ')
    query['units'] = 'metric'
    query['appid'] = input('Enter your api key for openweathermap.org: ')

    # Checking current time if its after or before 4am and modifying query_param accordingly
    currentDateTime = datetime.datetime.today()
    if currentDateTime.hour > 4:
        newDateTime = currentDateTime.replace(hour=4, minute=00, second=00)
    else:
        newDateTime = currentDateTime.replace(day=currentDateTime.day - 1, hour=4, minute=00, second=00)
    print("Date-time : Atmospheric Pressure")

    # Making the call 3 times with subtracting number of seconds in a day from newDateTime calculated above to get
    # atmospheric pressure at 4 am on each day.
    for x in range(3):
        query['dt'] = int(newDateTime.timestamp()) - (86400*x)

        # Using try-except to catch and print if any error occurs during api call
        # Using request python library to make http api calls and formatting and printing the desired output.
        try:
            response = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine', params=query, timeout=5)
            response.raise_for_status()
            responseObject = response.json()
            day = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(responseObject["current"]["dt"]))
            pressure = responseObject["current"]["pressure"]
            print(day, ":", pressure)
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
