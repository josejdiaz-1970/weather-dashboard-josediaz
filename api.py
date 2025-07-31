import requests
from dotenv import load_dotenv
import os
import datetime
import csv 

class LoadApi():

    def __init__(self, error_handler=None, show_error=None):
        
        load_dotenv()
        self.api_key = os.getenv("JD_API_KEY")

        # self.api_site = "http://api.openweathermap.org/data/2.5/weather" #Old API call 

        self.api_geocode = "http://api.openweathermap.org/geo/1.0/direct"
        self.api_site = "https://api.openweathermap.org/data/3.0/onecall"
        self.api_historical = "https://api.openweathermap.org/data/3.0/onecall/timemachine" #To get historical data for charts.


        self.show_error = show_error or (lambda title, msg: print(f"[{title}] {msg}"))

        self.error_handler = error_handler #Callback function to send errors to the GUI.

    def get_lat_lon(self, city):
    
        try:
            response = requests.get(self.api_geocode, params={
                "q": city,
                "limit": 1,
                "appid": self.api_key
            }, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not data:
                error_msg = "City not found."
               
                if self.error_handler:
                    self.error_handler(error_msg)
                
                return None, None
            
            return data
        except Exception as e:
            error_msg = f"Geo API error: {str(e)}"
            if self.error_handler:
                self.error_handler(error_msg)

            return None, None    



    def getData(self, city):

        self.geodata = self.get_lat_lon(city)

        #STill trying to fix this error handling code - TBD
        # try:
        #     lat = self.geodata[0]['lat']
        #     lon = self.geodata[0]['lon']
    
        #     if lat is None or lon is None:
        #         if self.show_error:
        #             self.show_error("Geolocation error", "Latitude or longitude is missing.")
        #     return None, None

        # except (IndexError, KeyError, TypeError) as e:
        #     if self.show_error:
        #         self.show_error("Geolocation error", f"Invalid geolocation data: {e}")
        #     return None, None
        
        if self.geodata[0]['lat'] is None or self.geodata[0]['lon'] is None:
            
            return None, None

        self.city=self.geodata[0]["name"]
        self.state = self.geodata[0].get("state", "")        
        self.country = self.geodata[0]["country"]

        try:

            response = requests.get(self.api_site, params={
                "lat": self.geodata[0]['lat'],
                "lon": self.geodata[0]['lon'],
                "exclude": "minutely",  # or "minutely,hourly,daily,alerts"
                "appid": self.api_key,
                "units": "imperial"
            }, timeout=5)
            response.raise_for_status()
            
            return response.json(), self.geodata

        #Handle errors of the Weather API
        except Exception as e:            
            
            if self.error_handler:
                self.error_handler("Weather API Error:", str(e))
            return None    

        #Handles status error codes        
        except requests.exceptions.RequestException as e:
            
            if self.error_handler:
                self.error_handler("Status Code Returned:", str(e))

        #Handles http errors...    
        except requests.exceptions.HTTPError as http_err:
           
            if self.error_handler:
                self.error_handler("HTTP error: ", str(http_err))
            
        except requests.exceptions.RequestException as req_err:
            
            if self.error_handler:
                self.error_handler("Request Error, Network error: ", str(req_err))
            
        except Exception as e:

            error_msg = f"An unexpected error occurred: {str(e)}"
            if self.error_handler:
                self.error_handler("An unexpected error occurred: ", str(e))

        return None


#Class to break the json file apart into individual data points

class ParseData():

    def __init__(self, data, city="",state="", country=""):
        
        self.city = city
        self.state = state
        self.country = country 
        self.FthenC = True #Boolean to pass on to GUI to swap the Units 
        
        print(f"DATA: \n {self.city} {self.state} {self.country}")
        current = data["current"]

        #Data for left frame and bottom frame

        # Checks to see if there is an alert section in the json response. If not
        # except the KeyError and send the summary instead.
        try:
            if data['alerts']:
                self.alerts = data['alerts'][0]['event']
                self.alertdescription = data['alerts'][0]['description']
                self.summary = "** See Alerts Description screen. **"
        except:
            KeyError 
            self.alerts = "No alerts."  
            self.summary = data['daily'][0]['summary']  



        #Data for right frame
        self.daily = data.get("daily", [])

            
        self.temperature_first = round(current['temp']) #Assign the Fahrenheit value to first temp
        self.temperature_second = round((self.temperature_first - 32) * (5/9)) #Celsius to second

        #For the team project
        self.temperature = self.temperature_first

        #If the country is not in the officially use fahrenheit, use celsius as first temp
        self.uses_fahrenheit = ["US", "PR", "BS", "KY", "PW", "FM", "MH", "LR"]
        if self.country not in self.uses_fahrenheit:
            self.temperature_first, self.temperature_second = self.temperature_second, self.temperature_first
            self.FthenC = False
            
       
        self.feels_like = round(current['feels_like'])
        self.description = current['weather'][0]['description'].capitalize()
        self.humidity = current['humidity']
        
        #Get hourly precipitation 
        self.precipitation = f"None : 0"
        #Team 
        self.precipitation_team = ""
        
        daily_forecast = data.get("daily", [])

        for day in daily_forecast:
            date = datetime.datetime.fromtimestamp(day["dt"]).strftime("%Y-%m-%d")

            precipitation_types = ["rain", "snow", "sleet", "hail"]
            for precip in precipitation_types:
                todays_precipitation = day.get(precip, 0)
                self.precipitation_team = todays_precipitation #For team file
                if todays_precipitation > 0:
                    self.precipitation = f"{precip} : {todays_precipitation * 0.0393701}"
         

        self.pressure = current['pressure']
        self.icon_code = current['weather'][0]['icon'] #WORKS
        
        self.uv = current['uvi']
        self.windspeed = round(current['wind_speed'])
        self.direction = current['wind_deg']
        self.visibility = current['visibility']
        self.curtime = datetime.datetime.fromtimestamp(current['dt']) 
        self.sunup = datetime.datetime.fromtimestamp(data['daily'][0]['sunrise'])
        self.sundown = datetime.datetime.fromtimestamp(current['sunset'])  

        #Bottom Frame

       
    def full_location(self):
        if self.state:
            return f"{self.city}, {self.state}, {self.country}"
        return f"{self.city}, {self.country}"

    def wind_deg_to_cardinal(self, deg):
        
        dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        ix = round(deg / 45) % 8
        return dirs[ix]   

import json 
import csv
import pandas as pd      

class SaveData():

    def __init__(self, filename, parsed, city):

        self.filename = filename    
        self.parsed = parsed
        self.city = city

        try:
            file_exists = os.path.isfile(self.filename)
            with open(self.filename, mode="a", newline="", encoding="utf-8") as f:
       
                writer = csv.writer(f)

                # Write headers only if the file is new
                if not file_exists:
                    if 'jjd' in self.filename:
                        writer.writerow([
                            "Current Time", "City", "State", "Country", "Temperature", "Feels Like", "Humidity", "Precipitation", "Pressure",
                            "Wind_Speed", "Wind Direction", "Visibility", "Sunrise", "Sunset"
                        ])
                   
                    else:
                        writer.writerow([
                            "Current Time", "City", "State", "Country", "Temperature in Preferred Units", "Temperature Alternate Units", "Feels Like" "Description", "Humidity",
                            "Precipitation", "Pressure", "UV Index", "Wind_Speed", "Direction","Sunrise", "Sunset"
                        ])
                
                if 'jjd' in self.filename:
                    writer.writerow([
                        self.parsed.curtime.strftime('%Y-%m-%d %H:%M:%S'),
                        self.city,
                        self.parsed.state,
                        self.parsed.country,
                        self.parsed.temperature,
                        self.parsed.feels_like,
                        self.parsed.humidity,
                        self.parsed.precipitation_team,
                        self.parsed.pressure,
                        self.parsed.windspeed,
                        self.parsed.direction,
                        self.parsed.visibility,
                        self.parsed.sunup.strftime('%H:%M:%S'),
                        self.parsed.sundown.strftime('%H:%M:%S')
                    ])
               
                else:
                    writer.writerow([
                        self.parsed.curtime.strftime('%Y-%m-%d %H:%M:%S'),
                        self.city,
                        self.parsed.state,
                        self.parsed.country,
                        self.parsed.temperature_first,
                        self.parsed.temperature_second,
                        self.parsed.feels_like,
                        self.parsed.description,
                        self.parsed.humidity,
                        self.parsed.precipitation,
                        self.parsed.pressure,
                        self.parsed.uv,
                        self.parsed.windspeed,
                        self.parsed.direction,
                        self.parsed.sunup.strftime('%H:%M:%S'),
                        self.parsed.sundown.strftime('%H:%M:%S')
                    ])

        except FileNotFoundError as e:
            print(f"Cannot find or create {self.filename}: {e}")