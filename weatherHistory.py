import csv
import json
import requests
import sys


def getWeather(airportName, nums, APIKey):
	#transform the airport name to location(lat, lon)

	strRes = ""
	if nums > 40 or nums <= 0:
		strRes = "exceed the range, Please enter the num from 0 to 40!"
		return strRes

	locationList = [0,0]
	flag01 = True

	with open('./data.csv', 'r') as f:
	    reader = csv.reader(f)
	    for row in reader:
	    	if  airportName == row[3]:
	    		locationList[0] = int(float(row[4]))
	    		locationList[1] = int(float(row[5]))
	    		flag01 = False
	    		break

	if(flag01):
		strRes = "airportName is wrong. Please enter the correct full airportName"
		return strRes

	print("location is {loc}".format(loc=locationList))

	# Request for API results
	str01 = "https://api.openweathermap.org/data/2.5/forecast?lat="
	str02 = "&lon="
	str04 = "&appid="
	str03 = str01 + str(locationList[0]) + str02 + str(locationList[1]) + str04 + APIKey

	r = requests.get(str03)
	a = r.json()

	# for loop to obtain the weather based on units numbers
	strUnit = "C"
	for i in range (0,nums):
		strTime = a['list'][i]["dt_txt"]
		strTemperature = str(int(float(a['list'][i]['main']['temp']) - 273.15))

		print("Time：{time}, Temperature: {temperature} {unit}".format(time=strTime, temperature=strTemperature, unit=strUnit))

	return strRes

def main():

	#Obtain the input
	print("Please enter the airport's full name: ")
	airportName = sys.stdin.readline()
	print("Please enter the units to forecast (1 unit = 3 hour) (the range is [0, 40]): ")
	hourNums = sys.stdin.readline()
	print("Please enter the openweathermap API Key: ")
	APIKey = sys.stdin.readline().strip()
	print("")

	nums = int(float((hourNums.strip())))
	airportName = airportName.strip()

	#call for method getWeather()
	getWeather(airportName, nums, APIKey)

if __name__=="__main__":
  main()