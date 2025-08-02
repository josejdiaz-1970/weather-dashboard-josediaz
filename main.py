#main.py 

import os
import api
from api import LoadApi, ParseData, SaveData 
from weather_gui import WGUI 

from features import themes
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

#For picture icons
from PIL import Image, ImageTk

#For the sayings
from features import sayings, sayings_manager

from team.features import madlibs_generator


class App():
    
    
    def __init__(self, root):

        self.root = root
      
        #Have to create this first before the gui otherwise it fails.
        self.sayings_manager = sayings_manager.SayingsManager(sayings.SAYINGS_BY_WEATHER, wrap_width=42)
        
        self.save_dir = r'C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\data'

        self.icon="" 

        #ChatGPT (August, 2025) - Just for order of operations.
        self.gui = WGUI(self.root, self, theme=themes.default_theme)  # create GUI first
        self.api = LoadApi(error_handler=self.gui.show_error)  # now pass instance method
       
           
    def update_quote(self, icon_code: str):
        # Map icon -> weather key 
        weather_key = sayings.ICON_TO_SAYINGS_KEY.get(icon_code, "default")
        quote = self.sayings_manager.get_quote(weather_key)
        wrapped, font_size = self.sayings_manager.format_for_label(quote)
        
        return quote    
        
    #chatGPT (July, 2025)
    def get_weather(self):
        
        city = self.gui.cityentry.get()
        if not city.strip():
            messagebox.showwarning("Input Required", "Please enter a city.")
            return
        
        raw_data, geodata = self.api.getData(city)
       
        if raw_data:
            
            city = geodata[0]["name"]
            state = geodata[0].get("state", "")
            country = geodata[0]["country"]    

            parsed = ParseData(raw_data, city=city, state=state, country=country)
            self.gui.display_weather(parsed)            
            self.icon=parsed.icon_code
            self.update_theme_based_on_toggle()
            
            #save the data
            SaveData(f"{self.save_dir}\\weather_data.csv", parsed, city)
           
            #Save the data for the group feature
            SaveData(f"{self.save_dir}\\weather_data_jjd.csv", parsed, city)
       

    def update_theme_based_on_toggle(self): 

        #Get the current status of the toggle boolean    
        if self.gui.use_weather_themes.get():            
            self.gui.apply_theme(themes.weather_decides_theme(self.icon))
        else:
            # Use default selected theme (e.g. light/dark)
            if "d" in self.icon: 
                self.gui.apply_theme(themes.light_theme) 
            elif "n" in self.icon:    
                self.gui.apply_theme(themes.dark_theme) 

    #For future color icons
    def get_flat_icon(self, code):
        
        icon_path = os.path.join("assets", "icons_flat", f"{code}.png")
        if not os.path.exists(icon_path):
            icon_path = os.path.join("assets", "icons_flat", "default.png")

        if code=="thinking" or code=="warning":
            icon_size = {"thinking": (80, 80),
                         "warning": (25, 25)
                        }      
                
            img = ctk.CTkImage(Image.open(icon_path), size=(icon_size[code]))
        
        else:       
            img = ctk.CTkImage(Image.open(icon_path), size=(200, 200)) #Need to fix image
       
        return img
    
                               
if __name__ == "__main__": 
       
    root = ctk.CTk()
    app = App(root)   
    root.mainloop()