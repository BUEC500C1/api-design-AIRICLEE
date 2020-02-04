from weatherHistory import getWeather



# NOTICE!!!
# You must add the API key here, then the test program can be tested !!!
APIkey = "**********************"

def test_unitType():
	assert getWeather("Watts Field", 41, APIkey) == "exceed the range, Please enter the num from 0 to 40!"
	assert getWeather("Watts Field", 0, APIkey) == "exceed the range, Please enter the num from 0 to 40!"
	assert getWeather("Watts Field", -1, APIkey) == "exceed the range, Please enter the num from 0 to 40!"

def test_airportExit():
	assert getWeather("Watts Field!!", 29, APIkey) == "airportName is wrong. Please enter the correct full airportName"
	assert getWeather("fgdasifhi", 5, APIkey) == "airportName is wrong. Please enter the correct full airportName"
	assert getWeather("watts field", 12, APIkey) == "airportName is wrong. Please enter the correct full airportName"