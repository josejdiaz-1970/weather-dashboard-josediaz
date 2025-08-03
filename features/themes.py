#theme selector 
'''
The code for theme selection in the GUI. Will have light and dark modes. If 
I have time will add a them to switch based on the weather conditions.

'''

#To Do:

# Add color icons but with colors that change based on theme


default_theme = {
    "bg_color": "#26788D",       # Main background color
    "fg_color": "#26788D",       # Frame background color
    # "left_fg_color": "#3590A7",       # Left Frame background color
    "font_color": "#E3ECEE",     # Text label color
    "font_style": "Helvetica",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#3E6D79",      # Button color
    "button_fg": "#ffffff",       # Button text color
    "icon_color": "#E3ECEE",          #icon color for basic icons
    "button_hover": "#ffffff"
}

# Light Theme
light_theme = {
    "bg_color": "#f0f0f0",
    "fg_color": "#f0f0f0",
    "font_color": "#111111",
    "font_style": "Helvetica",
    "font_size": 14,
    "button_bg": "#e2d5d5",
    "button_fg": "#000000",
    "icon_color": "#111111",
    "button_hover": "#ffffff"
}

# Dark Theme
dark_theme = {
    "bg_color": "#242424",       
    "fg_color": "#242424",       
    "font_color": "#f5f5f5",     
    "font_style": "Open Sans",   
    "font_size": 14,             
    "button_bg": "#3B3737",     
    "button_fg": "#ffffff",
    "font_color": "#f5f5f5",
    "icon_color": "#f5f5f5",
    "button_hover": "#ffffff"        
}

#Future

rain_theme = {
    "bg_color": "#6384A2",       # Main background color
    "fg_color": "#6384A2",       # Frame background color
    "font_color": "#CEDDEE",     # Text label color
    "font_style": "Myanmar Text",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#75AAB8",      # Button color
    "button_fg": "#ffffff",      # Button text color
    "icon_color": "#52687D",    # Icon color for basic icons
    "button_hover": "#ffffff"
}

#Make background a light sky blue. Like a summer day.
sunny_theme = {
    "bg_color": "#81CFFF",       # Main background color
    "fg_color": "#81CFFF",       # Frame background color
    "font_color": "#000000",     # Text label color
    "font_style": "Times New Roman",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#FFFFBB",      # Button color
    "button_fg": "#000000",       # Button text color
    "icon_color": "#FFFF70",      # Icon color for basic icons
    "button_hover": "#ffffff"
}

moon_theme = {

    "bg_color": "#212e39",       # Main background color
    "fg_color": "#212e39",       # Frame background color
    "font_color": "#edc8a9",     # Text label color
    "font_style": "Bookman Old Style",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#595f72",      # Button color
    "button_fg": "#000000",       # Button text color
    "icon_color": "#f7d9c1",       #Icon color for basic icons
    "button_hover": "#ffffff"  

}

cloudy_theme = {
    "bg_color": "#84b6e4",       # Main background color
    "fg_color": "#84B6e4",       # Frame background color
    "font_color": "#000000",     # Text label color
    "font_style": "Lucida",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#5a7492",      # Button color
    "button_fg": "#000000",       # Button text color
    "icon_color": "#d7e2ef",     #Icon color for basic icons
    "button_hover": "#ffffff"
}

partly_cloudy_theme = {

    "bg_color": "#99b6cc",       # Main background color
    "fg_color": "#99b6cc",       # Frame background color
    "font_color": "#3b3f24",     # Text label color
    "font_style": "Trebuchet MS",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#6384a9",      # Button color
    "button_fg": "#dfef87",       # Button text color
    "icon_color": "#d7e2ef",     #Icon color for basic icons
    "button_hover": "#ffffff"

}

haze_theme = {

    "bg_color": "#fbecda",       # Main background color
    "fg_color": "#fbecda",       # Frame background color
    "font_color": "#8d7968",     # Text label color
    "font_style": "Arial Bold",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#b6a393",      # Button color
    "button_fg": "#53453d",       # Button text color
    "icon_color": "#cdc2b9",      # Icon color for basic icons
    "button_hover": "#ffffff"

}
snow_theme = {

    "bg_color": "#b7b9bf",       # Main background color
    "fg_color": "#b7b9bf",       # Frame background color
    "font_color": "#22496e",     # Text label color
    "font_style": "Verdana",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#6683a2",      # Button color
    "button_fg": "#64647c",       # Button text color
    "icon_color": "#FFFAFA",       # Icon color for basic icons
    "button_hover": "#ffffff"
}

tstorm_theme = {

    "bg_color": "#2c3b6a",       # Main background color
    "fg_color": "#2c3b6a",       # Frame background color
    "font_color": "#c4eafc",     # Text label color
    "font_style": "Tahoma",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#6384a9",      # Button color
    "button_fg": "#c4eafc",       # Button text color
    "icon_color": "#7DF9FF",       # Icon color for basic icons
    "button_hover": "#ffffff"
 
}

#Warning: May cause uncontrollable vomiting. Dont say you werent warned.
pink_theme = {

    "bg_color": "#f9cee7",       # Main background color
    "fg_color": "#f9cee7",       # Frame background color
    "font_color": "#cf62b4",     # Text label color
    "font_style": "Arial bold",   # Font family
    "font_size": 15,             # Font size
    "button_bg": "#f4b8da",      # Button color
    "button_fg": "#e68bcf",       # Button text color
    "icon_color": "#cf62b4",       # Icon color for basic icons
    "button_hover": "#ffffff"

}

def weather_decides_theme(icon):
    icon_to_theme = {
        "01d": sunny_theme,
        "01n": moon_theme,
        "02d": partly_cloudy_theme,
        "02n": cloudy_theme,
        "03d": partly_cloudy_theme,
        "03n": partly_cloudy_theme,
        "04d": partly_cloudy_theme,
        "04n": partly_cloudy_theme,
        "09d": rain_theme,
        "09n": rain_theme,
        "10d": rain_theme,
        "10n": rain_theme,
        "11d": tstorm_theme,
        "11n":tstorm_theme,
        "13d": snow_theme,
        "13n": snow_theme,
        "50d": haze_theme,
        "50n": haze_theme
    }
    return icon_to_theme.get(icon, default_theme)
    
  