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

# save_dir = r'C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\data'

class App():
   
    # city = "" #default city
   
    
    def __init__(self, root):

        self.root = root
        self.api = LoadApi()
        self.gui = WGUI(self.root, self, theme=themes.default_theme)
        self.save_dir = r'C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\data'

        self.icon="" 
        
        
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
    def get_flat_icon(code):
        
        icon_path = os.path.join("assets", "icons_flat", f"{code}.png")
        if not os.path.exists(icon_path):
            icon_path = os.path.join("assets", "icons_flat", "default.png")
    
        img = Image.open(icon_path)
        img = img.resize((64, 64), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)
                            
if __name__ == "__main__": 
    # root = tk.Tk()
   
    root = ctk.CTk()
    app = App(root)   
    root.mainloop()