#main.py 

import api
from api import LoadApi, ParseData, SaveData 
from weather_gui import WGUI
import tkinter as tk
from tkinter import messagebox

# save_dir = r'C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\data'

class App():
   
    city = "San Juan,PR" #default city
   
    
    def __init__(self, root):

        self.root = root
        self.api = LoadApi()
        self.gui = WGUI(self.root, self)
        self.save_dir = r'C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\data'
        
    #chatGPT (July, 2025)
    def get_weather(self):
        
        city = self.gui.cityentry.get()
        if not city.strip():
            messagebox.showwarning("Input Required", "Please enter a city.")
            return
        
        raw_data = self.api.getData(city)
        if raw_data:
            parsed = ParseData(raw_data)
            self.gui.display_weather(parsed)
            #save the data
            SaveData(f"{self.save_dir}\\weather_data.csv", parsed, city)

            
                  
     
                       
if __name__ == "__main__": 
    root = tk.Tk()
    app = App(root)
    
    # test = app.gui.cityentry.get()
    # print(f"Current city:{test}")    
    # if not test.strip():  # empty or whitespace-only
    #     print("Input Required")
      
     
    # app.gui.weather_data.insert(tk.END, test, "NO CITY")

    root.mainloop()