## About The Project

This project is used to output the atmospheric pressure at 4am for the past three days for a geographical location whose latitude and longitude is given as the input by the user. It uses https://openweathermap.org/api to get the required data from the API of OpenWeathermap.org. 

### Built With
* [Python 3.10](https://www.python.org/)

## Getting Started
To run this project you just need to have a version of Python (version 3 or greater) installed in your system.
### Prerequisites
Things you need to run the project and how to install/get them.
* requests
  ```sh
  pip install requests
  ```
 * Get a free API Key at https://openweathermap.org/api

### Running the project
1. Clone the task1.py file in your system.
2. Open command prompt and navigate to the directory where you have cloned the task1.py file.
3. Check if you installed 'requests' library by running ```pip install request```
4. Run the python file by running ```python task1.py``` .
5. Enter the _latitude_ , _longitude_ and the _api key_ obatained from the Openweathermap.org. and press enter.

### Dependencies
**The Request**
When you want to interact with data via a REST API, this is called a request. A request is made up of the following components:

>**Endpoint** – The URL that delineates what data you are interacting with. Similar to how a web page URL is tied to a specific page, an endpoint URL is tied to a specific resource within an API.

>**Method** – Specifies how you’re interacting with the resource located at the provided endpoint. REST APIs can provide methods to enable full Create, Read, Update, and Delete (CRUD) functionality. Here are common methods most REST APIs provide:

>**The Responsec**
When you perform a request, you’ll get a response from the API. Just like in the request, it’ll have a response header and response data, if applicable. The response header consists of useful metadata about the response, while the response data returns what you actually requested. This can be any sort of data, as it’s really dependent on the API. The text is usually returned as JSON, but other markdown languages like XML are also possible. 

### Code Logic
The task was to get the latidude and longitude from the user and print the atmospheric prerssure of that place at 4am for past three days by using the API's provided in free tier account of OpenWeatherMap.org. 
* I have used the Historical weather data section of the documentation which lets us provide the date in Unix timestamp to get the weather from a particular day.
* Firstly I asked the user to input the latitude and longitude of the location they wanted the data about.
* I have also made the user input their api-key as input so that it can be used by anyone with their own api-key.
* After that I am taking the current system date and time and changing the hour to 4am if the current time is after 4am on that day or changing the date to yesterday's date and time as 4am.
* Then I stored all the input parameters in a dictionary which is a map like key-value type data structure which is used as an input structure to enter query params. 
* Then I run a loop which runs thrice each time subtracting the value of 1 day in seconds (86400) from the Unix timestamp we generated above. 
* After that I am just getting the particular value of pressure and date from the response and printing in the cnonsole.
* I have used to try-except to throw any error which occurs during making the api call, making the code rubust.

