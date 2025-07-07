#theme selector 
'''
The code for theme selection in the GUI. Will have light and dark modes. If 
I have time will add a them to switch based on the weather conditions.

'''
def getTheme():
    #Code here    
    pass

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

rain_theme = {}
sunny_theme = {}
cloudy_theme = {}
haze_theme = {}
snow_theme = {}