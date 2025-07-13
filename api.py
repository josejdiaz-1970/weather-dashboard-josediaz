import requests
from dotenv import load_dotenv
import os
import datetime
import csv 

class LoadApi():

    def __init__(self):
        
        load_dotenv()
        self.api_key = os.getenv("JD_API_KEY")

        # self.api_site = "http://api.openweathermap.org/data/2.5/weather"

        self.api_geocode = "http://api.openweathermap.org/geo/1.0/direct"
        self.api_site = "https://api.openweathermap.org/data/3.0/onecall"

    def get_lat_lon(self, city):
        try:
            response = requests.get(self.api_geocode, params={
                "q": city,
                "limit": 1,
                "appid": self.api_key
            })
            response.raise_for_status()
            data = response.json()
            if not data:
                print("City not found")
                return None, None
            # return data[0]["lat"], data[0]["lon"]
            print(f"DATA: {data}\n\n\n\n\n")
            return data
        except Exception as e:
            print(f"Geo API error: {e}")
            return None, None    



    def getData(self, city):

        self.geodata = self.get_lat_lon(city)
        
        if self.geodata[0]['lat'] is None or self.geodata[0]['lon'] is None:
            return None

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
            })
            response.raise_for_status()
            print(response.json()) 
            return response.json(), self.geodata
        except Exception as e:
            print(f"Weather API error: {e}")
            return None    

            # # url = f"{self.api_site}?q={self.city}&appid={self.api_key}&units=imperial"
            # url = f"{self.api_site}lat=33.44&lon=-94.04&exclude=hourly,daily&appid={self.api_key}"
            # geocodeurl = f"{self.api.geocode}?q={self.city},&limit=1&appid={self.api_key}"
            # self.data = requests.get(url)
            # self.data.raise_for_status()
            # self.current = self.data.json()
            # print(self.current)
            
            
            if str(self.current.get("cod")) != "200":
                # message = conditions.get("message", "Invalid city specified.")
                print(self.current.get("message", "Invalid city specified."))
                # messagebox.showerror(title="City Error", message=f"City '{city}' not found. {message.capitalize()}")
                # return None

            return self.current
        # print(conditions)

        except requests.exceptions.RequestException as e:
            # messagebox.showerror(message=f"Status code returned: {e}")
            print(f"Status code returned: {e}")
        except requests.exceptions.HTTPError as http_err:
            # messagebox.showerror(title="HTTP Error", message=f"HTTP error: {http_err}")
            print("HTTP Error", message=f"HTTP error: {http_err}")
        except requests.exceptions.RequestException as req_err:
            # messagebox.showerror(title="Request Error", message=f"Network error: {req_err}")
            print(f"Request Error, Network error: {req_err}")
        except Exception as e:
            # messagebox.showerror(title="Unexpected Error", message=f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred: {e}")

        # return None


#Class to break the json file apart into individual data points

class ParseData():

    def __init__(self, data, city="",state="", country=""):
        
        self.city = city
        self.state = state
        self.country = country 
        self.FthenC = True #Boolean to pass on to GUI to swap the Units   

        current = data["current"]

        #Data for left frame and bottom frame

        # Checks to see if there is an alert section in the json response. If not
        # except the KeyError and send the summary instead.
        try:
            if data['alerts']:
                self.alerts = data['alerts'][0]['event']
                self.summary = data['alerts'][0]['description']
        except:
            KeyError 
            self.alerts = "No alerts."  
            self.summary = data['daily'][0]['summary']  



        #Data for right frame
        self.daily = data.get("daily", [])

        self.temperature_first = round(current['temp']) #Assign the Fahrenheit value to first temp
        self.temperature_second = round((self.temperature_first - 32) * (5/9)) #Celsius to second

        #If the country is not in the officially use fahrenheit, use celsius as first temp
        self.uses_fahrenheit = ["US", "PR", "BS", "KY", "PW", "FM", "MH", "LR"]
        if self.country not in self.uses_fahrenheit:
            self.temperature_first, self.temperature_second = self.temperature_second, self.temperature_first
            self.FthenC = False
            
       
        self.feels_like = round(current['feels_like'])
        self.description = current['weather'][0]['description'].capitalize()
        self.humidity = current['humidity']
        self.pressure = current['pressure']
        self.icon_code = current['weather'][0]['icon']
        self.uv = current['uvi']
        self.windspeed = round(current['wind_speed'])
        self.direction = current['wind_deg']
        self.visibility = current['visibility']
        # self.curtime = datetime.datetime.fromtimestamp(current['dt']) 
        # self.sunup = datetime.datetime.fromtimestamp(current['sys']['sunrise'])
        # self.sundown = datetime.datetime.fromtimestamp(current['sys']['sunset'])  

        #Bottom Frame

       
    def full_location(self):
        if self.state:
            return f"{self.city}, {self.state}, {self.country}"
        return f"{self.city}, {self.country}"

    def wind_deg_to_cardinal(self, deg):
        
        dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        ix = round(deg / 45) % 8
        return dirs[ix]   

        

class SaveData():

    def __init__(self, filename, parsed, city):

        self.filename = filename    
        self.parsed = parsed
        self.city = city

        try:
            file_exists = os.path.isfile(self.filename)
            with open(self.filename, mode="a", newline="") as f:
       
                writer = csv.writer(f)

                # Write headers only if the file is new
                if not file_exists:
                    writer.writerow([
                        "City", "State", "Country", "Temperature", "Description", "Humidity",
                        "Pressure", "UV Index", "Wind_Speed", "Direction"
                    ])

                writer.writerow([
                    self.city,
                    self.parsed.state,
                    self.parsed.country,
                    self.parsed.temperature_first,
                    self.parsed.temperature_second,
                    self.parsed.feels_like,
                    self.parsed.description,
                    self.parsed.humidity,
                    self.parsed.pressure,
                    self.parsed.uv,
                    self.parsed.windspeed,
                    self.parsed.direction,
                    # self.parsed.curtime.strftime('%Y-%m-%d %H:%M:%S'),
                    # self.parsed.sunup.strftime('%H:%M:%S'),
                    # self.parsed.sundown.strftime('%H:%M:%S')
                ])

        except FileNotFoundError as e:
            print(f"Cannot find or create {self.filename}: {e}")