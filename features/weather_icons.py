#weather icons
'''
Will load icons based on the current conditions.

'''
def get_icons(code):
   
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
    pass