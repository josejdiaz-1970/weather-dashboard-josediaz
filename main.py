#main.py 

import api
from api import LoadApi, ParseData, SaveData 
from weather_gui import WGUI
from features import themes
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# save_dir = r'C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\data'

class App():
   
    city = "San Juan,PR" #default city
   
    
    def __init__(self, root):

        self.root = root
        self.api = LoadApi()
        self.gui = WGUI(self.root, self, theme=themes.default_theme)
        self.save_dir = r'C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\data'
        
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
            #save the data
            SaveData(f"{self.save_dir}\\weather_data.csv", parsed, city)

       
                            
if __name__ == "__main__": 
    # root = tk.Tk()
   
    root = ctk.CTk()
    app = App(root)   
    root.mainloop()