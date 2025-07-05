import requests
from dotenv import load_dotenv
import os
import datetime
import csv 

class LoadApi():

    def __init__(self):
        
        load_dotenv()
        self.api_key = os.getenv("JD_API_KEY")

        self.api_site = "http://api.openweathermap.org/data/2.5/weather"

    def getData(self, city):

        self.city=city

        try:
            url = f"{self.api_site}?q={self.city}&appid={self.api_key}&units=imperial"
            self.data = requests.get(url)
            self.data.raise_for_status()
            self.current = self.data.json()
            
            message=""

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

    def __init__(self, current):
        
        self.current = current
           
        self.temperature = current['main']['temp']
        self.description = current['weather'][0]['main']+", "+current['weather'][0]['description']
        self.humidity = current['main']['humidity']
        self.pressure = current['main']['pressure']
        self.icon_code = current['weather'][0]['icon']
        
        self.curtime = datetime.datetime.fromtimestamp(current['dt']) 
        self.sunup = datetime.datetime.fromtimestamp(current['sys']['sunrise'])
        self.sundown = datetime.datetime.fromtimestamp(current['sys']['sunset'])   

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
                        "City", "Temperature", "Description", "Humidity",
                        "Pressure", "Time", "Sunrise", "Sunset"
                    ])

                writer.writerow([
                    self.city,
                    self.parsed.temperature,
                    self.parsed.description,
                    self.parsed.humidity,
                    self.parsed.pressure,
                    self.parsed.curtime.strftime('%Y-%m-%d %H:%M:%S'),
                    self.parsed.sunup.strftime('%H:%M:%S'),
                    self.parsed.sundown.strftime('%H:%M:%S')
                ])

        except FileNotFoundError as e:
            print(f"Cannot find or create {self.filename}: {e}")