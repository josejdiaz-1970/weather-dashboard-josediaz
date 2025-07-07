#weather_gui.py

import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, font
from tkinter import messagebox
import features.themes as themes
from datetime import datetime



class WGUI():

    bg_color = "#36A1E4"
    fg_color = "#f5f5f5"
    font_color = "#ffffff"
    font_style = "Bell Gothic Std Black"
    font_size = 16

    #for the notebook tabs
       
    
    def __init__(self, root, controller, theme=themes.default_theme):
                
        style = ttk.Style() 
        
        self.root = root
        self.controller = controller
        self.theme = theme
        
        self.root.title("Jose's Weather App")
        self.root.geometry("800x600+0+0")
        self.root.configure(fg_color= WGUI.bg_color)

        #theme variables
        self.bg_color = theme["bg_color"]
        self.fg_color = theme["fg_color"]
        self.font_color = theme["font_color"]
        self.font_style = theme["font_style"]
        self.font_size = theme["font_size"]
        self.button_bg = theme["button_bg"]
        self.button_fg = theme["button_fg"]

       
        # Add a menu bar and sub-menus - WORKS
        menu_font=font.Font(family="Helvetica", size=16)
        menubar = tk.Menu(self.root, font=menu_font)
        style.configure('Custom.Notebook.Tab', font=menu_font) 

        # Theme Menu
        themesmenu = tk.Menu(menubar, tearoff=0)
        themesmenu.add_command(label="Light Theme", font=menu_font, command=lambda: self.apply_theme(themes.light_theme))
        themesmenu.add_command(label="Dark Theme", font=menu_font, command=lambda: self.apply_theme(themes.dark_theme))
        themesmenu.add_command(label="Let the Weather Decide", font=menu_font, command=lambda: print("Based on current conditions"))
        themesmenu.add_command(label="Default", font=menu_font, command=lambda: self.apply_theme(themes.default_theme))
        
        
        menubar.add_cascade(label="Themes", menu=themesmenu)

        # Settings Menu
        settingsmenu = tk.Menu(menubar, tearoff=0)
        settingsmenu.add_command(label="Preferences", font=menu_font, command=lambda: print("Preferences clicked"))
        menubar.add_cascade(label="Settings", menu=settingsmenu)

        # Help Menu
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", font=menu_font, command=lambda: print("About clicked"))
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Exit
        exitmenu = tk.Menu(menubar, tearoff=0)
        exitmenu.add_command(label="Exit", font=menu_font, command=self.root.destroy)
        menubar.add_cascade(label="Exit", menu=exitmenu)

        # Attach menubar to the window
        self.root.config(menu=menubar)


        #Add a notebook and tabs - Prelim in progress
        notebook = ttk.Notebook(self.root, style='Custom.Notebook.Tab')
        main_tab = ttk.Frame(notebook)
        graphs_tab = ttk.Frame(notebook)
        csv_tab = ttk.Frame(notebook)

        main_tab.grid_rowconfigure(0, weight=1)
        main_tab.grid_rowconfigure(1, weight=1)
        main_tab.grid_rowconfigure(2, weight=1)
        main_tab.grid_rowconfigure(3, weight=1)
        main_tab.grid_rowconfigure(4, weight=1)
        main_tab.grid_rowconfigure(5, weight=1)
        main_tab.grid_rowconfigure(6, weight=1)

        main_tab.grid_rowconfigure(0, weight=1)
        main_tab.grid_columnconfigure(0, weight=1)
        main_tab.grid_columnconfigure(1, weight=2)
        
        csv_tab.grid_rowconfigure(0, weight=1)
        csv_tab.grid_columnconfigure(0, weight=1)


        notebook.add(main_tab, text='Main')
        notebook.add(graphs_tab, text='Graphs')
        notebook.add(csv_tab, text="Saved Data")

        
        notebook.grid(row=0, column=0, sticky='nsew')

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #Create frames -changed parent to notebook
        self.left_frame = ctk.CTkFrame(main_tab, fg_color=self.bg_color, width=150, height=350)
        self.right_frame = ctk.CTkFrame(main_tab, fg_color=self.bg_color, width=650, height=350)
        self.bottom_frame = ctk.CTkFrame(main_tab, fg_color=self.bg_color, height=50)

        self.left_frame.grid_propagate(False)

        # Layout frames
        self.left_frame.grid(row=0, column=0, rowspan=6, sticky="nsew") 
        self.right_frame.grid(row=0, column=1, rowspan=6, columnspan=5, sticky="nsew")
        self.bottom_frame.grid(row=6, column=0, columnspan=6, sticky="nsew")

        #ChatGPT (July, 2025)
        self.left_frame.grid_rowconfigure(0, weight=0)  # Label
        self.left_frame.grid_rowconfigure(1, weight=0)  # Entry
        self.left_frame.grid_rowconfigure(2, weight=0)  # Button
        self.left_frame.grid_rowconfigure(3, weight=1)  # Weather Icon
        self.left_frame.grid_rowconfigure(4, weight=1)  # Mood/Saying
        self.left_frame.grid_rowconfigure(5, weight=1)  # Spacer
        self.left_frame.grid_columnconfigure(0, weight=1)  # Stretch everything

        for i in range(6):
            self.right_frame.grid_rowconfigure(i, weight=1)



                
        # Add widgets to left_frame

        self.citylabel=ctk.CTkLabel(self.left_frame, fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size), text="Enter a city:")
        self.cityentry = ctk.CTkEntry(self.left_frame, width=100)    
        self.citybutton = ctk.CTkButton(self.left_frame, fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size),text="Get Weather",command=self.controller.get_weather)
        self.alertsbox = ctk.CTkTextbox(self.left_frame, fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
        self.weather_icon = ctk.CTkLabel(self.left_frame, text="🌤️", font=("Helvetica", 40))
        self.sayingsbox = ctk.CTkTextbox(self.left_frame, fg_color=self.bg_color, text_color=self.font_color, height=80, font=(self.font_style, self.font_size))
    
        #Add widgets to the right frame
        #Big weather icon goes here
        self.icon_label = ctk.CTkLabel(self.right_frame, text="", width = 100, height=100, fg_color=self.bg_color)

        #Location label
        self.location_label=ctk.CTkLabel(self.right_frame, text="City, Country", font=(self.font_style, self.font_size + 2),text_color=self.font_color, fg_color=self.bg_color)
   
        self.temperature = ctk.CTkLabel(self.right_frame, text="",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))
        self.humidity = ctk.CTkLabel(self.right_frame, text="",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))
        self.wind = ctk.CTkLabel(self.right_frame, text="Wind: ", fg_color = self.bg_color, font = (self.font_style, self.font_size))
        self.pressure = ctk.CTkLabel(self.right_frame, text="",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))
        self.feels_like = ctk.CTkLabel(self.right_frame, text="Feels Like: ", fg_color = self.bg_color, font = (self.font_style, self.font_size))
        self.uv_index = ctk.CTkLabel(self.right_frame, text="UV Index: ",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))
        
        #forecasts to the right frame. Set up Frames and Labels

        self.forecast_frame = ctk.CTkFrame(self.right_frame, fg_color=self.bg_color)
        self.forecast_frame.grid(row=8, column=0, columnspan=2, pady=(10, 0), sticky="ew")

        self.forecast_day_frames = []

        for i in range(5):
            day_frame = ctk.CTkFrame(self.forecast_frame, fg_color=self.bg_color, width=80)
            day_frame.grid(row=0, column=i, padx=5, pady=5, sticky="n")

            label_day = ctk.CTkLabel(day_frame, text="Day", font=(self.font_style, self.font_size - 2), text_color=self.font_color)
            label_icon = ctk.CTkLabel(day_frame, text="⛅", font=(self.font_style, self.font_size + 4), text_color=self.font_color)
            hi_label = ctk.CTkLabel(day_frame, text="88°", fg_color=self.bg_color, text_color=self.font_color)
            lo_label = ctk.CTkLabel(day_frame, text="72°", fg_color=self.bg_color, text_color=self.font_color)

            label_day.grid(row=0, column=0, pady=(2, 0))
            label_icon.grid(row=1, column=0)
            hi_label.grid(row=2, column=0)
            lo_label.grid(row=3, column=0)

            day_frame.grid(row=0, column=i, padx=5, pady=5)
            
            self.forecast_day_frames.append({
                "day": label_day,
                "icon": label_icon,
                "hi": hi_label,
                "lo": lo_label
            })
            

        # Configure widgets
        self.sayingsbox.insert("0.0", "A sunny day keeps the bugs at bay ☀️")
        self.sayingsbox.configure(state="disabled")


        #Add to left as grid
        self.citylabel.grid(row=0, column=0,pady=(10, 5), padx=10, sticky="w")
        self.cityentry.grid(row=1,column=0, pady=(0, 5), padx=10, sticky="ew")    
        self.citybutton.grid(row=2,column=0, pady=(0, 10),padx=10, sticky="ew")

        self.alertsbox.grid(row=3, column=0, pady=(20, 10),sticky="n")
        self.weather_icon.grid(row=4, column=0, pady=(10, 5), padx=10, sticky="n")
        self.sayingsbox.grid(row=5,column=0, padx=10, pady=(5,10), sticky="nsew")

        #Add to right frame as grid
          
        # Top Icon and Location Centered
        self.icon_label.grid(row=0, column=0, columnspan=2, pady=(10, 0), sticky="n")
        self.location_label.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky="n")

        # Two-column Weather Info
        self.temperature.grid(row=2, column=0, sticky="w", padx=20, pady=3)
        self.humidity.grid(row=2, column=1, sticky="w", padx=20, pady=3)

        self.wind.grid(row=3, column=0, sticky="w", padx=20, pady=3)
        self.pressure.grid(row=3, column=1, sticky="w", padx=20, pady=3)

        self.feels_like.grid(row=4, column=0, sticky="w", padx=20, pady=3)
        self.uv_index.grid(row=4, column=1, sticky="w", padx=20, pady=3)

        # Forecast below all data
        self.forecast_frame.grid(row=5, column=0, columnspan=2, pady=(20, 10), padx=10, sticky="ew")          


        # Add widgets to bottom_frame
        
        self.test = ctk.CTkLabel(self.bottom_frame,fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size) ,text="Bottom Frame")
        self.test.pack()

    #Weather display method - Need to add country and city
    def display_weather(self, parsed):
                
        self.location_label.configure(text=parsed.full_location())
        self.temperature.configure(text=f"{parsed.temperature}°F\n")    
       
        self.humidity.configure(text=f"{parsed.humidity} %RH\n")
        self.pressure.configure(text=f"{parsed.pressure} hPa\n")
        self.uv_index.configure(text=parsed.uv)
        self.wind.configure(text=f"{parsed.windspeed} {parsed.direction}")
        

        if hasattr(parsed, "daily"):
            self.display_forecast(parsed.daily)
        else:
            print("No forecast data available")
        

    def apply_theme(self, theme: dict) -> None:

        
        self.bg_color = theme["bg_color"]
        self.fg_color = theme["fg_color"]
        self.font_color = theme["font_color"]
        self.font_style = theme["font_style"]
        self.font_size = theme["font_size"]
        self.button_bg = theme["button_bg"]
        self.button_fg = theme["button_fg"] 

        #root update 
        self.root.configure(fg_color=self.bg_color)

        #Update the widgets
        self.cityentry.configure(fg_color=self.bg_color, font=(self.font_style, self.font_size))
        self.citybutton.configure(fg_color=self.button_bg, text_color=self.button_fg,font=(self.font_style, self.font_size))
                
        self.citylabel.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
        self.citydisplay.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size)
)
        
        self.country.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
       
        self.temperature.configure(fg_color=self.bg_color, text_color=self.font_color)
        self.humidity.configure(fg_color=self.bg_color, text_color=self.font_color)
        self.description.configure(fg_color=self.bg_color, text_color=self.font_color)
        self.pressure.configure(fg_color=self.bg_color, text_color=self.font_color)
        self.windspeed.configure(fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))
        self.winddirection.configure(fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))

        for label in self.desc_labels:
            label.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))

        #Theme the frames
        self.left_frame.configure(fg_color=self.fg_color)
        self.right_frame.configure(fg_color=self.fg_color)


    def display_forecast(self, daily_data):
        for i, day_data in enumerate(daily_data[1:6]):  # skip today, get next 5
            dt = datetime.fromtimestamp(day_data["dt"])
            day_name = dt.strftime("%a")

            icon_code = day_data["weather"][0]["icon"]
            icon = self.get_icon_for_code(icon_code)  # see below

            temp_max = round(day_data["temp"]["max"])
            temp_min = round(day_data["temp"]["min"])

            self.forecast_day_frames[i]["day"].configure(text=day_name)
            self.forecast_day_frames[i]["icon"].configure(text=icon)
            self.forecast_day_frames[i]["hi"].configure(text=f"↑ {temp_max}°")
            self.forecast_day_frames[i]["lo"].configure(text=f"↓ {temp_min}°")

    def get_icon_for_code(self, code):
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