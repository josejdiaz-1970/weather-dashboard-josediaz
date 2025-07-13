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
    "font_color": "#E3ECEE",     # Text label color
    "font_style": "Helvetica",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#518D9C",      # Button color
    "button_fg": "#ffffff"       # Button text color
}

# Light Theme
light_theme = {
    "bg_color": "#f0f0f0",
    "fg_color": "#f0f0f0",
    "font_color": "#111111",
    "font_style": "Helvetica",
    "font_size": 14,
    "button_bg": "#e0e0e0",
    "button_fg": "#000000"
}

# Dark Theme
dark_theme = {
    "bg_color": "#242424",       
    "fg_color": "#242424",       
    "font_color": "#f5f5f5",     
    "font_style": "Helvetica",   
    "font_size": 14,             
    "button_bg": "#242424",     
    "button_fg": "#ffffff"      
}

#Future

rain_theme = {
    "bg_color": "#6384A2",       # Main background color
    "fg_color": "#6384A2",       # Frame background color
    "font_color": "#0D2642",     # Text label color
    "font_style": "Courier",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#518D9C",      # Button color
    "button_fg": "#ffffff"       # Button text color
}

sunny_theme = {
    "bg_color": "#F1DEA2",       # Main background color
    "fg_color": "#F1DEA2",       # Frame background color
    "font_color": "#000000",     # Text label color
    "font_style": "Times New Roman",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#FF9A00",      # Button color
    "button_fg": "#000000"       # Button text color
}

moon_theme = {

    "bg_color": "#212e39",       # Main background color
    "fg_color": "#212e39",       # Frame background color
    "font_color": "#edc8a9",     # Text label color
    "font_style": "Bookman Old Style",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#595f72",      # Button color
    "button_fg": "#000000"       # Button text color

}

cloudy_theme = {
    "bg_color": "#84b6e4",       # Main background color
    "fg_color": "#84B6e4",       # Frame background color
    "font_color": "#000000",     # Text label color
    "font_style": "Lucida",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#6384a9",      # Button color
    "button_fg": "#000000"       # Button text color
}

partly_cloudy_theme = {

    "bg_color": "#99b6cc",       # Main background color
    "fg_color": "#99b6cc",       # Frame background color
    "font_color": "#3b3f24",     # Text label color
    "font_style": "Trebuchet MS",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#6384a9",      # Button color
    "button_fg": "#dfef87"       # Button text color

}

haze_theme = {

    "bg_color": "#fbecda",       # Main background color
    "fg_color": "#fbecda",       # Frame background color
    "font_color": "#8d7968",     # Text label color
    "font_style": "Arial Bold",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#c1ad9b",      # Button color
    "button_fg": "#8d7968"       # Button text color

}
snow_theme = {

    "bg_color": "#b7b9bf",       # Main background color
    "fg_color": "#b7b9bf",       # Frame background color
    "font_color": "#22496e",     # Text label color
    "font_style": "Verdana",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#6683a2",      # Button color
    "button_fg": "#64647c"       # Button text color
}

tstorm_theme = {

    "bg_color": "#2c3b6a",       # Main background color
    "fg_color": "#2c3b6a",       # Frame background color
    "font_color": "#c4eafc",     # Text label color
    "font_style": "Tahoma",   # Font family
    "font_size": 14,             # Font size
    "button_bg": "#6384a9",      # Button color
    "button_fg": "#c4eafc"       # Button text color
 
    }

pink_theme = {}

def weather_decides_theme(self, icon):
    
    icon_to_theme = {

        "01d":"sunny_theme",
        "01n":"moon_theme",
        "02d":"partly_cloudy_theme",
        "02n": "cloudy_theme",
        "03d": "cloudy_theme",
        "04d": "cloudy_theme",
        "04n": "cloudy_theme"
    }
    
    pass