# api-design-AIRICLEE

## Summary
Use OpenWeatherMAP API and data.csv which contains the information of all of the airports in USA, to realize the function that can output the target airport's temperature in following 5 days.

## User Story
* As a customer who want to by flight tickets, they want to see the weather information of the airport in advance, to avoid any delay of flight cause of the weather.
* As a customer who will arrive in a airport by plane, they need to know the local weather to decide which cloths to wear(like jackets or T-shirts)
* As a staff in airport, they need to manage all the flight routes. Therefore they need to get the weather informatoin in following hours to manage in a more reasonable way.

## Related Files
* **weatherHistory.py**  
This is the main file to forecast the temperature with the input (airportname, units)
airportname means user should imput the full name of the airport which he wants to get weather information
units means how many hours from now to future, user wants to obtain. Besides, 1 unit means 3 hours. Due to the limitation of API, we only can get 5 days in future and the units in result is 3 hours

* **data.csv**  
This is a file which contains all the airports' information is USA, including the latitude, longtitude, airport's full name, local_code and so on. Therefore, this file is like a dictionary. We can obtain the locations's precise latitude and longtitude through airport's full name

* **test_weatherHistory.py** 
This file is meant to test the main file weatherHistory.py. Check whether it will have grammatical errors or any other bugs that will cause the program run forever or collapse

## Steps in weatherHistory.py
1. Get parameters from input and transform them into compatible type included airport name, units and API keys
2. Find the airport name in data.csv. Once finded it, then get the corresponding latitude and longtitude and break the finding loop
3. Use the Key, latitude and longtitude to form the url to request API results
4. Extract temperature data from .json results

## Test Samples
TODO
