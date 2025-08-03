#weather icons.py
#Tps25-Capstone
#Date: 02-Aug-2025
'''
weather_icons.py loads icons based on the current conditions. Uses Erik Flower's icons
and if the fail, it defaults to open weather maps icons. Erik's icons are now default.

'''

import tkinter.font as tkfont
import os

# Define the font path (relative to your project)
font_path = os.path.join("assets", "fonts", "weathericons-regular-webfont.ttf")


# Register the font with Tkinter
def load_icon_font(root):
    try:
        tkfont.nametofont("Weather Icons")
    except tkfont.TclError:
        root.tk.call("font", "create", "Weather Icons", "-family", "Weather Icons", "-size", "24")
        root.tk.call("font", "configure", "Weather Icons", "-family", "Weather Icons") 


icon_map = {
    "01d": "\uf00d",  # clear day
    "01n": "🌙", #"\uf02e",  # clear night
    "02d": "\uf002",  # few clouds day
    "02n": "\uf086",  # few clouds night
    "03d": "\uf041",  # scattered clouds
    "04d": "\uf013",  # broken clouds
    "09d": "\uf019",  # shower rain
    "10d": "\uf008",  # rain day
    "11d": "\uf01e",  # thunderstorm
    "13d": "\uf01b",  # snow
    "50d": "\uf014",  # mist
    # Add more if needed
}

def get_icons(code):

        icon_map = {
        "01d": "\uf00d",  # clear day - works
        "01n": "🌙",#"\uf02e",  # clear night
        "02d": "\uf002",  # few clouds day - works
        "02n": "\uf086",  # few clouds night
        "03d": "\uf041",  # scattered clouds - NOT WORKING
        "03n": "\uf041",  # scattered clouds - NOT WORKING
        "04d": "\uf013",  #broken clouds day
        "04n": "\uf013", # broken clouds night- NOT WORKING
        "09d": "\uf019",  # shower rain
        "10d": "\uf008",  # rain day
        "10n": "\uf008", #"🌧", #rain night
        "11d": "\uf01e",  # thunderstorm
        "13d": "\uf01b",  # snow
        "50d": "\uf014",  # mist
        "50n": "\uf014",  # mist
        # Add more if needed

        }

        return icon_map.get(code, "\uf07b")  # default: "na" icon

def get_default_icons(code):

      
     icon_map = {
            "01d": "☀️", "01n": "🌙",
            "02d": "🌤", "02n": "☁️",
            "03d": "☁️", "03n": "☁️",
            "04d": "☁️", "04n": "☁️",
            "09d": "🌧", "09n": "🌧",
            "10d": "🌦", "10n": "🌧",
            "11d": "⛈", "11n": "⛈",
            "13d": "❄️", "13n": "❄️",
            "50d": "🌫", "50n": "🌫"
        }
     return icon_map.get(code, "❓") 

#Icons in color, will be SVG files
def get_color_icons(code):
    
    icon_map = {
         
         "01d": "01d.png",
         "01n": "01n.png",
         "02d": "02d.png",
         "02n": "02n.png",
         "13d": "13d.png",
    }

    return icon_map.get(code, "default.png")
    pass