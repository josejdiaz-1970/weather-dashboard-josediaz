#weather_gui.py

import tkinter as tk
from tkinter import messagebox


class WGUI():

    
    def __init__(self, root, controller):
        
        self.root = root
        self.controller = controller
       
        self.root.title("Jose's Weather App")
        self.root.geometry("800x400")
        self.root.configure(bg="#36A1E4")

        
        #Create frames

        left_frame = tk.Frame(self.root, bg='#1e3d59', width=200, height=350)
        right_frame = tk.Frame(self.root, bg='#f5f5f5', width=600, height=350, bd=2, relief='groove')
        bottom_frame = tk.Frame(self.root, bg='#d1e0e0', height=50)

        # Layout frames
        left_frame.grid(row=0, column=0, sticky="nsw")
        right_frame.grid(row=0, column=1, sticky="nsew")
        bottom_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Add widgets to left_frame

        #Replace with clickable icon and bubble pop up that says: Current conditions
        self.citybutton = tk.Button(left_frame, bg = '#1e3d59', fg='#f5f5f5',text="Current Conditions:",command=self.controller.get_weather)
        self.citybutton.grid(row=3, column=0, padx=10, pady=10, sticky="ne")
        self.citylabel=tk.Label(left_frame, bg = '#1e3d59', fg='#f5f5f5', text="Enter a City")
        self.cityentry = tk.Entry(left_frame, width=20)
        self.citylabel.grid(row=1, column=0) 
        self.cityentry.grid(row=2, column=0, padx=10, pady=10, sticky="ne")

        # Add widgets to right_frame
        self.weather_data = tk.Text(master=right_frame, wrap="word", width=60, height=20)
        self.weather_data.pack(padx=10, pady=10)

        # Add widgets to bottom_frame
        self.test = tk.Label(bottom_frame, text="Bottom Frame")
        self.test.pack()

    #Weather display method
    def display_weather(self, parsed):
        self.weather_data.delete(1.0, tk.END)  # clear old output
        output = (
            f"Temperature: {parsed.temperature}°F\n"
            f"Description: {parsed.description}\n"
            f"Humidity: {parsed.humidity}%\n"
            f"Pressure: {parsed.pressure} hPa\n"
            f"Sunrise: {parsed.sunup.strftime('%H:%M:%S')}\n"
            f"Sunset: {parsed.sundown.strftime('%H:%M:%S')}\n"
        )
        self.weather_data.insert(tk.END, output)    