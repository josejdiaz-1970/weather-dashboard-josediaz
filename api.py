import requests
from dotenv import load_dotenv
import os

api_site = "http://api.openweathermap.org/data/2.5/weather"

        #Change self.key to look at .env
load_dotenv()        
api_key = os.getenv("JD_API_KEY")

city="San Juan,PR"
try:
    url = api_site + "?q=" + city + "&appid=" + api_key + "&units=imperial"
    data = requests.get(url)
    data.raise_for_status()
    conditions = data.json()
    message=""

    if str(conditions.get("cod")) != "200":
        # message = conditions.get("message", "Invalid city specified.")
        print(conditions.get("message", "Invalid city specified."))
        # messagebox.showerror(title="City Error", message=f"City '{city}' not found. {message.capitalize()}")
        # return None

        # return conditions
    print(conditions)

except requests.exceptions.RequestException as e:
#     # messagebox.showerror(message=f"Status code returned: {e}")
    print(f"Status code returned: {e}")
except requests.exceptions.HTTPError as http_err:
#     # messagebox.showerror(title="HTTP Error", message=f"HTTP error: {http_err}")
    print("HTTP Error", message=f"HTTP error: {http_err}")
except requests.exceptions.RequestException as req_err:
#     # messagebox.showerror(title="Request Error", message=f"Network error: {req_err}")
    print(f"Request Error, Network error: {req_err}")
except Exception as e:
#     # messagebox.showerror(title="Unexpected Error", message=f"An unexpected error occurred: {e}")
    print(f"An unexpected error occurred: {e}")

# return None
