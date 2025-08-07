#weather_gui.py
#Tps25-Capstone
#Date: 02-Aug-2025
'''
class WGUI:
The main class for the gui. It basically encompasses all of the functionality of the displays for the weather app.
The class uses customtkinter for most of its windows and widgets. Tkinter is only used for tk.Menu, to which 
customtkinter currently has no equivalent. Since the functionality of this application is mostly visual,
this is tends to be the largest file. The class represents the UI component in a mostly MVC architecture.

WGUI implements the following methods:

on_enter(), on_leave(): For button functionality of hover. Background color changes but text color does not.

update_suggestions(): This method updates the city entry and display combobox.

display_weather(): responsible for updating the widgets based on the data acquired from the API.

about(): Displays credits.

get_pink(): Easter egg, flair or whatever. Responsible for the hideous pink theme. Have your eye bleach nearby.

apply_theme(): Applies the theme to widgets based on the selected theme. Updates dynamically. Takes a theme dictionary 
and applies the color preferences to the widgets.

toggle_icon_theme(): Toggles between dynamic (color icons) and text based icons.

display_forecast(): Displays the 5-day forecast at the bottom right pane of the main window.

show_error(): responsible for showing errors in the gui as pop up windows.

generate_madlib(): Generates the madlib incorporating user selections on the drop downs in 
the madlibs page. If user doesnt select anything, it will use defaults.

'''



import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, font
from tkinter import messagebox
import features.themes as themes
import features.weather_icons as icons
from datetime import datetime

#for team feature
import team.features.word_library as wl
from team.features.madlibs_generator import MadGenerator as MG

#To log the final madlib and other data to a csv file.
from team.features.madlib_logger import log_madlib_session

import warnings

class WGUI():     
    
    def __init__(self, root, controller, theme=themes.default_theme, cities=None):
                
        style = ttk.Style() 
        
        self.root = root
        self.controller = controller
        self.theme = theme
        self.city_list = cities

        self.root.title("Jose's Weather App")
        self.root.geometry("800x800+0+0")
        
        #theme variables changed to self.theme
        self.bg_color = self.theme["bg_color"]
        self.fg_color = self.theme["fg_color"]
        self.font_color = self.theme["font_color"]
        self.font_style = self.theme["font_style"]
        self.font_size = self.theme["font_size"]
        self.button_bg = self.theme["button_bg"]
        self.button_fg = self.theme["button_fg"]
        self.icon_color = self.theme["icon_color"]
        self.button_bg = self.theme["button_bg"]
        self.button_hover = self.theme["button_hover"]

        #Flag to apply theme based on weather conditions
        self.use_weather_themes = tk.BooleanVar(value=False)
        #Toggle for dynamic themes
        self.dynamic_icons_enabled = tk.BooleanVar(value=False)
        self.thinking_icon = self.controller.get_flat_icon("thinking") #Fixes a glitch in the icon image

        #Instance for Madlibs generator
        self.mad_generator = MG(filepath=r"C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\team\data")
       
        #About 
        self.info_text = None

        #If statement to check if window is created before styling info_text. ChatGPT(August, 2025)
        if self.info_text is not None and self.info_text.winfo_exists():
           
            self.info_text.configure(
                fg_color=self.bg_color,
                text_color=self.font_color,
                font=(self.font_style, self.font_size)
            )

        #Warning supress
        warnings.filterwarnings("ignore", category=UserWarning, module="customtkinter")

        # Add a menu bar and sub-menus - WORKS
        menu_font=font.Font(family="Arial", size=16)
        menubar = tk.Menu(self.root, font=menu_font)
        

        # Theme Menu
        themesmenu = tk.Menu(menubar, tearoff=0)
        themesmenu.add_command(label="Light Theme", font=menu_font, command=lambda: self.apply_theme(themes.light_theme))
        themesmenu.add_command(label="Dark Theme", font=menu_font, command=lambda: self.apply_theme(themes.dark_theme))
        themesmenu.add_command(label="Rain Theme", font=menu_font, command=lambda: self.apply_theme(themes.rain_theme))
        themesmenu.add_command(label="Sunny Theme", font=menu_font, command=lambda: self.apply_theme(themes.sunny_theme))
        themesmenu.add_command(label="Moon Theme", font=menu_font, command=lambda: self.apply_theme(themes.moon_theme))
        themesmenu.add_command(label="Partly Cloudy Theme", font=menu_font, command=lambda: self.apply_theme(themes.partly_cloudy_theme))
        themesmenu.add_command(label="Cloudy Theme", font=menu_font, command=lambda: self.apply_theme(themes.cloudy_theme))
        themesmenu.add_command(label="Haze Theme", font=menu_font, command=lambda: self.apply_theme(themes.haze_theme))
        themesmenu.add_command(label="Snow Theme", font=menu_font, command=lambda: self.apply_theme(themes.snow_theme))
        themesmenu.add_command(label="Thunderstorm Theme", font=menu_font, command=lambda: self.apply_theme(themes.tstorm_theme))     
        themesmenu.add_command(label="Pink Theme", font=menu_font, command=self.get_pink)#self.apply_theme(themes.pink_theme)) #Change to command=get_pink    


        # themesmenu.add_command(label="Let the Weather Decide", font=menu_font, command=self.theme_based_on_weather == True) #make it a setting
        themesmenu.add_command(label="Default", font=menu_font, command=lambda: self.apply_theme(themes.default_theme))
        
        
        menubar.add_cascade(label="Themes", menu=themesmenu)

        # Settings Menu
        settingsmenu = tk.Menu(menubar, tearoff=0)
        settingsmenu.add_checkbutton(label="Dynamic Icon Theme", font=menu_font, variable=self.dynamic_icons_enabled, command=self.toggle_icon_theme)
        settingsmenu.add_checkbutton(label="Use Weather-Based Themes", font=menu_font, variable=self.use_weather_themes, command=controller.update_theme_based_on_toggle)
        menubar.add_cascade(label="Settings", menu=settingsmenu)
        
        # Help Menu
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", font=menu_font, command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Exit
        exitmenu = tk.Menu(menubar, tearoff=0)
        exitmenu.add_command(label="Exit", font=menu_font, command=self.root.destroy)
        menubar.add_cascade(label="Exit", menu=exitmenu)

        # Attach menubar to the window
        self.root.config(menu=menubar)

        #Add TabView to replace tk.notebook
        self.tabview = ctk.CTkTabview(self.root, width=800, height=800, corner_radius=5)
        self.tabview.grid(row=0, column=0, padx=0, pady=0)
      
        #Tab button configuration
        self.tabview._segmented_button.configure(
            fg_color=self.bg_color, 
            text_color=self.font_color,
            selected_color = self.button_bg,
            selected_hover_color= self.bg_color,
            unselected_color = self.fg_color,
            font=(self.font_style, self.font_size)            
        )
        # Add tabs
        self.main_tab = self.tabview.add("Main")
        self.summary_tab = self.tabview.add("Alert Details")
        self.madlibs_tab = self.tabview.add("Madlibs")

        
        # Resize behavior
        self.tabview.rowconfigure(0, weight=1)
        self.tabview.columnconfigure(0, weight=1)
            
        self.main_tab.grid_rowconfigure(0, weight=1)
        self.main_tab.grid_rowconfigure(1, weight=1)    

        # self.main_tab.grid_rowconfigure(0, weight=1)
        # self.main_tab.grid_rowconfigure(1, weight=1)
        # self.main_tab.grid_rowconfigure(2, weight=1)
        # self.main_tab.grid_rowconfigure(3, weight=1)
        # self.main_tab.grid_rowconfigure(4, weight=1)
        # self.main_tab.grid_rowconfigure(5, weight=1)
        # self.main_tab.grid_rowconfigure(6, weight=1)
     
        #Left frame goes in here
        self.main_tab.grid_columnconfigure(0, weight=1) 

        #Right frame will take up these 3 columns
        self.main_tab.grid_columnconfigure(1, weight=1)
        self.main_tab.grid_columnconfigure(2, weight=0)
        self.main_tab.grid_columnconfigure(3, weight=1)

        self.madlibs_tab.grid_rowconfigure(0, weight=1)
        self.madlibs_tab.grid_columnconfigure(0, weight=1)


        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1, uniform="a")

        #testing maintab color
        self.main_tab.configure(fg_color=self.bg_color)

        #Create frames -changed parent to notebook
        self.left_frame = ctk.CTkFrame(self.main_tab, fg_color=self.bg_color, width=250, height=350, border_width=0)
        self.spacer_left = ctk.CTkFrame(self.main_tab, fg_color=self.bg_color,height=350, border_width=0)  # or fg_color="transparent"
        self.spacer_right = ctk.CTkFrame(self.main_tab, fg_color=self.bg_color, height=350, border_width=0)
       
        # self.right_frame_outer = ctk.CTkFrame(self.main_tab, fg_color=self.fg_color, width=560, height=350)
        self.right_frame = ctk.CTkFrame(self.main_tab, fg_color=self.bg_color, width=570, height=350, border_width=0)
        self.bottom_frame = ctk.CTkFrame(self.main_tab, fg_color=self.bg_color, height=100, border_width=0)

        #Add alerts details_frame to summary tab
        self.alertdetails_frame = ctk.CTkFrame(self.summary_tab, fg_color = self.bg_color, width=800, height=800)
        self.alertdetails_frame.grid_propagate(False)

        #Add madlibs_frame to madlibs_tab
        self.madlibs_frame = ctk.CTkFrame(self.madlibs_tab, fg_color = self.bg_color, width=800, height=800)
        self.madlibs_frame.grid_propagate(False)

        self.left_frame.grid_propagate(False)
        
        self.left_frame.configure(width=250)

        # Layout frames
        self.left_frame.grid(row=0, column=0, rowspan=7, padx=0, pady=0, sticky="nsw") #nsew
        # self.right_frame.grid(row=0, column=1, rowspan=7, columnspan=5, sticky="nsew")
        self.spacer_left.grid(row=0, column=1, rowspan=7, padx=0, pady=0, sticky="nsew")
        
        self.right_frame.grid(row=0, column=2, rowspan=7, padx=0, pady=0, sticky="nsew") #set row to 1 , nsew
        self.spacer_right.grid(row=0, column=3, rowspan=7, padx=0, pady=0,sticky="nsew")
   
        self.bottom_frame.grid(row=7, column=0, columnspan=6, padx=0, pady=0, sticky="nsew")

        self.alertdetails_frame.grid(row=0, column=0, sticky="nsew")
        self.alertdetails_frame.grid_rowconfigure(0, weight=1)
        self.alertdetails_frame.grid_columnconfigure(0, weight=1)
        self.madlibs_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #ChatGPT (July, 2025)
        self.left_frame.grid_rowconfigure(0, weight=0)  # Label
        self.left_frame.grid_rowconfigure(1, weight=0)  # Entry
        self.left_frame.grid_rowconfigure(2, weight=0)  # Button
        self.left_frame.grid_rowconfigure(3, weight=0)  #Alert Label
        self.left_frame.grid_rowconfigure(4, weight=1)  # Weather Icon
        self.left_frame.grid_rowconfigure(5, weight=1)  # Mood/Saying
        self.left_frame.grid_rowconfigure(6, weight=1)  # Spacer
        self.left_frame.grid_columnconfigure(0, weight=0, minsize=250)  # Stretch everything

        for i in range(8):
            self.right_frame.grid_rowconfigure(i, weight=1)

        self.right_frame.grid_columnconfigure(1, weight=1) 
        self.right_frame.grid_columnconfigure(2, weight=1) 
        self.right_frame.grid_columnconfigure(3, weight=1) 
        #Madlibs Frame row and column configure
        
        for i in range(4):
            self.madlibs_frame.grid_columnconfigure(i, weight=1)

        # To center the right frame
        self.spacer_left.configure(width=125)
        self.spacer_right.configure(width=125)
        
        

        #MAIN TAB        
        # Add widgets to left_frame

        self.citylabel=ctk.CTkLabel(self.left_frame, fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size), text="Enter a city:")
        
        #changed to combobox for autocomplete functionality
        self.cityentry = self.city_combobox = ctk.CTkComboBox(self.left_frame, variable="",
                                                              values=self.city_list[:500],
                                                              fg_color=self.bg_color,
                                                              text_color=self.font_color,
                                                              font=(self.font_style, 
                                                              self.font_size),

                                                              )
        
        self.cityentry.bind("<KeyRelease>", self.update_suggestions)

        
        self.citybutton = ctk.CTkButton(self.left_frame, 
                                        fg_color=self.bg_color, 
                                        text_color=self.font_color,
                                        hover_color=self.button_hover,
                                        border_width=2,
                                        border_color = self.font_color,
                                        font=(self.font_style, self.font_size),
                                        text="Get Weather",
                                        command=self.controller.get_weather,
                                        hover=True                                        
                                        )
        
        self.citybutton.bind("<Enter>", self.on_enter)        
        self.citybutton.bind("<Leave>", self.on_leave)
        
        self.alertslabel = ctk.CTkLabel(self.left_frame, image=self.controller.get_flat_icon("warning"), text=" Alerts!", text_color=self.font_color,font=(self.font_style, self.font_size), compound="left")
        self.alertsbox = ctk.CTkTextbox(self.left_frame, fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
        self.weather_icon = ctk.CTkLabel(self.left_frame, text="", image=self.thinking_icon) 
        self.sayingsbox = ctk.CTkTextbox(self.left_frame, fg_color=self.bg_color, text_color=self.font_color, height=80, font=(self.font_style, self.font_size), wrap="word")
    
        #Add widgets to the right frame
      
        #Big weather icon goes here
        self.icon_label = ctk.CTkLabel(self.right_frame, text="🌤️", width = 100, height=100, bg_color=self.button_bg, fg_color=self.bg_color, text_color=self.icon_color, font=("Weather Icons", self.font_size + 90))

        #Location label
        self.location_label=ctk.CTkLabel(self.right_frame, text="City, Country", font=(self.font_style, self.font_size + 2),text_color=self.font_color, fg_color=self.bg_color)
        self.description=ctk.CTkLabel(self.right_frame, text="Description", font=(self.font_style, self.font_size - 2),text_color=self.font_color, fg_color=self.bg_color)
        self.temperature_first = ctk.CTkLabel(self.right_frame, text="",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size + 30))
        self.temperature_second = ctk.CTkLabel(self.right_frame, text="",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size - 2))
        self.humidity = ctk.CTkLabel(self.right_frame, text="Humidity: ",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))
        self.wind = ctk.CTkLabel(self.right_frame, text="Wind: ", fg_color = self.bg_color, font = (self.font_style, self.font_size))
        self.visibility = ctk.CTkLabel(self.right_frame, text="Visibility: ",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))        
        self.pressure = ctk.CTkLabel(self.right_frame, text="Barometer: ",fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size))
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
            label_icon = ctk.CTkLabel(day_frame, text="⛅", font=("Weather Icons", self.font_size + 4), text_color=self.font_color)
            hi_label = ctk.CTkLabel(day_frame, text="88°", fg_color=self.bg_color, text_color=self.font_color)
            lo_label = ctk.CTkLabel(day_frame, text="72°", fg_color=self.bg_color, text_color=self.font_color)

            label_day.grid(row=0, column=0, pady=(2, 0))
            label_icon.grid(row=1, column=0)
            hi_label.grid(row=2, column=0)
            lo_label.grid(row=3, column=0)

            self.forecast_day_frames.append({
                "frame": day_frame,
                "day": label_day,
                "icon": label_icon,
                "hi": hi_label,
                "lo": lo_label
            })

          

        # Configure widgets
        self.sayingsbox.insert("0.0", self.controller.update_quote(self.icon_label))
        self.sayingsbox.configure(state="disabled")

        #Bottom Frame 
        self.summary = ctk.CTkLabel(self.bottom_frame,fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size) ,text="Summary:")
        #ALERTS TAB
        #Alerts details textbox for Alert Details tab
        self.alertdetail = ctk.CTkTextbox(self.alertdetails_frame,fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size + 3),width=780, height=780, wrap="word")

        #ADDED 7/28/25
        #Madlibs textbox for Madlibs tab
        self.madlibs_title = ctk.CTkLabel(self.madlibs_frame,text="Random files, Random rows Weather MadLibs", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size + 10))
        
        #Comboboxes for nouns, verbs,etc...
        self.madlibs_nounlabel_1 = ctk.CTkLabel(self.madlibs_frame, text="Please select a noun", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_noun_1=ctk.CTkComboBox(self.madlibs_frame, 
                                              values=wl.NOUNS, 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              font=(self.font_style, self.font_size)                                              
                                             )     
        
        self.madlibs_nounlabel_2 = ctk.CTkLabel(self.madlibs_frame, text="Select another noun", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_noun_2=ctk.CTkComboBox(self.madlibs_frame, 
                                              values=wl.NOUNS, 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              font=(self.font_style, self.font_size)
                                             )     

        self.madlibs_verblabel_1 = ctk.CTkLabel(self.madlibs_frame, text="Select a verb", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_verb_1=ctk.CTkComboBox(self.madlibs_frame, 
                                              values=wl.VERBS, 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              font=(self.font_style, self.font_size)
                                             )     
        
        self.madlibs_verblabel_2 = ctk.CTkLabel(self.madlibs_frame, text="Select another verb", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_verb_2=ctk.CTkComboBox(self.madlibs_frame, 
                                              values=wl.VERBS, 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              font=(self.font_style, self.font_size)
                                             )     


        self.madlibs_adverblabel_1 = ctk.CTkLabel(self.madlibs_frame, text="Select an adverb", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_adverb_1=ctk.CTkComboBox(self.madlibs_frame, 
                                              values=wl.ADVERBS, 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              font=(self.font_style, self.font_size)
                                             )     
        
        self.madlibs_adverblabel_2 = ctk.CTkLabel(self.madlibs_frame, text="Select another adverb", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_adverb_2=ctk.CTkComboBox(self.madlibs_frame, 
                                              values=wl.ADVERBS, 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              font=(self.font_style, self.font_size)
                                             )  

        self.madlibs_adjectivelabel_1 = ctk.CTkLabel(self.madlibs_frame, text="Select an adjective", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_adjective_1=ctk.CTkComboBox(self.madlibs_frame, 
                                              values=wl.ADJECTIVES, 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              font=(self.font_style, self.font_size)
                                             ) 
        
        self.madlibs_adjectivelabel_2 = ctk.CTkLabel(self.madlibs_frame, text="Select another adjective", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_adjective_2=ctk.CTkComboBox(self.madlibs_frame, 
                                              values=wl.ADJECTIVES, 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              font=(self.font_style, self.font_size)
                                             ) 


        #To show what files and rows were randomly chosen.        
        self.madlibs_first_file = ctk.CTkLabel(self.madlibs_frame, text="First file: ", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_second_file = ctk.CTkLabel(self.madlibs_frame, text="Second file: ",fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_first_row = ctk.CTkLabel(self.madlibs_frame, text="Selected row: ", fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        self.madlibs_second_row = ctk.CTkLabel(self.madlibs_frame, text="Selected row: ",fg_color=self.bg_color,text_color=self.font_color,font=(self.font_style, self.font_size))
        
        #Generate the madlib using all the selected words and the random weather data.
        self.madlibs_generate = ctk.CTkButton(self.madlibs_frame, 
                                              text="Generate Madlib", 
                                              fg_color=self.bg_color,
                                              text_color=self.font_color,
                                              border_width=2,
                                              border_color = self.font_color,
                                              hover_color=self.button_hover,
                                              font=(self.font_style, self.font_size +5),
                                              command=self.generate_madlib,
                                              hover=True
                                              
                                              )
        
        self.madlibs_generate.bind("<Enter>", self.on_enter)
        self.madlibs_generate.bind("<Leave>", self.on_leave)

    
        #In this box I want to create comboboxes for nouns, verbs, etc... based on the number needed for the template      
        self.madlibs_box = ctk.CTkTextbox(self.madlibs_frame,
                                          fg_color=self.bg_color,
                                          text_color=self.font_color,
                                          font=(self.font_style, self.font_size+10),
                                          height=200, 
                                          wrap="word"                                          
                                         ) 

        

        self.madlibs_box.configure(state="disabled")



        #Add to madlibs as a grid

        # Title centered across all columns
        self.madlibs_title.grid(row=0, column=0, columnspan=4, pady=(20, 10), sticky="ew")

        # Row 1: Nouns
        self.madlibs_nounlabel_1.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.madlibs_noun_1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.madlibs_nounlabel_2.grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.madlibs_noun_2.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        # Row 2: Verbs
        self.madlibs_verblabel_1.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.madlibs_verb_1.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.madlibs_verblabel_2.grid(row=2, column=2, padx=5, pady=5, sticky="e")
        self.madlibs_verb_2.grid(row=2, column=3, padx=5, pady=5, sticky="w")

        # Row 3: Adverbs
        self.madlibs_adverblabel_1.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.madlibs_adverb_1.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.madlibs_adverblabel_2.grid(row=3, column=2, padx=5, pady=5, sticky="e")
        self.madlibs_adverb_2.grid(row=3, column=3, padx=5, pady=5, sticky="w")

        # Row 4: Adjectives
        self.madlibs_adjectivelabel_1.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.madlibs_adjective_1.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.madlibs_adjectivelabel_2.grid(row=4, column=2, padx=5, pady=5, sticky="e")
        self.madlibs_adjective_2.grid(row=4, column=3, padx=5, pady=5, sticky="w")

        # Row 5: Generate Button centered
        self.madlibs_generate.grid(row=5, column=1, columnspan=2, pady=(20, 40), sticky="ew")

        # Row 6: File Info (split across top-left and right)
        self.madlibs_first_file.grid(row=6, column=0, columnspan=2, padx=5, pady=2, sticky="w")
        self.madlibs_second_file.grid(row=6, column=2, columnspan=2, padx=5, pady=2, sticky="w")

        # Row 7: Selected rows
        self.madlibs_first_row.grid(row=7, column=0, columnspan=2, padx=5, pady=2, sticky="w")
        self.madlibs_second_row.grid(row=7, column=2, columnspan=2, padx=5, pady=2, sticky="w")

        # Row 8: Final madlib output box
        self.madlibs_frame.grid_rowconfigure(8, weight=1)  # let it expand
        self.madlibs_box.grid(row=8, column=0, columnspan=4, padx=10, pady=(10, 5), sticky="nsew")

        #Add to left as grid
        self.citylabel.grid(row=0, column=0,pady=(10, 5), padx=10, sticky="w")
        self.cityentry.grid(row=1,column=0, pady=(0, 5), padx=10, sticky="ew")    
        self.citybutton.grid(row=2,column=0, pady=(0, 10),padx=10, sticky="ew")

        self.alertslabel.grid(row=3, column=0, pady=(20, 10),sticky="n")
        self.alertsbox.grid(row=4, column=0, pady=(20, 10),sticky="n")
        self.weather_icon.grid(row=5, column=0, pady=(10, 5), padx=10, sticky="n")
        self.sayingsbox.grid(row=6,column=0, padx=10, pady=(5,10), sticky="nsew")

        #Add to right frame as grid
          
        # Top Icon and Location Centered
        self.icon_label.grid(row=0, column=0, columnspan=2, pady=(10, 0), sticky="n")
        self.location_label.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky="s")
        self.description.grid(row=2, column=0, columnspan=2, pady=(0, 15), sticky="n")
        #Add description label here

        # Two-column Weather Info
        self.temperature_first.grid(row=3, column=0, sticky="e", padx=20, pady=3)
        self.temperature_second.grid(row=3, column=1, sticky="w",padx=10)
       
        self.humidity.grid(row=4, column=0, sticky="nw", padx=20, pady=3)
        self.feels_like.grid(row=4, column=1, sticky="nw", padx=20, pady=3)

        self.wind.grid(row=5, column=0, sticky="nw", padx=(20), pady=3)
        self.visibility.grid(row=5, column=1, sticky="nw",padx=20, pady=3)
        self.pressure.grid(row=6, column=0, sticky="nw", padx=20, pady=3)        
        self.uv_index.grid(row=6, column=1, sticky="nw", padx=20, pady=3)

        # Forecast below all data
        self.forecast_frame.grid(row=7, column=0, columnspan=2, pady=(20, 10), padx=10, sticky="ew")       


        # Add widgets to bottom_frame
        self.summary.grid(row=0, columnspan=3, sticky="nsew")
        self.alertdetail.grid(row=0, column=0, sticky="nsew")

    #Event methods for buttons
    def on_enter(self, event):
        if isinstance(event.widget, ctk.CTkButton):           
            event.widget.configure(fg_color=self.button_hover, text_color="#000000", text=event.widget.cget("text_color"))
            

    def on_leave(self, event):
        if isinstance(event.widget, ctk.CTkButton):
            event.widget.configure(fg_color=self.button_bg, text_color=self.button_fg)
        

    #New for cityentry combobox
    def update_suggestions(self, event):
        typed = self.city_combobox.get().lower()

        if typed == "":
            matches = self.city_list
        else:
            matches = [city for city in self.city_list if city.lower().startswith(typed)] #if typed in city_lower()

        # Avoid freezing from too many results
        matches = matches[:100]

        self.cityentry.configure(values=matches)
        
        # if matches:

        if matches:
            
            self.cityentry.event_generate("<Down>") 

       
        # Keep what user typed (manually reset it because CTkComboBox overwrites it)
        self.city_combobox.set(typed)




    #Weather display method
    def display_weather(self, parsed):

        #LEFT FRAME UPDATE
        self.alertsbox.delete("0.0", "end") #clear the textbox first
        
        self.alertsbox.insert("0.0", f"{parsed.alerts}") #⚠️

        #RIGHT FRAME UPDATE
                
        if self.dynamic_icons_enabled.get():
            icon = self.controller.get_flat_icon(parsed.icon_code)
            self.icon_label.configure(text="")
            self.icon_label.configure(image=icon)
        else:
            icon = icons.get_icons(parsed.icon_code)
            self.icon_label.configure(image="")
            self.icon_label.configure(text=icon)
        
        self.current_icon_code = parsed.icon_code #added to make it work with main   

            
        self.location_label.configure(text=parsed.full_location())
       
        self.temperature_first.configure(text=f"{parsed.temperature_first}°F\n")  
      

        #Check if the first temperature is Fahrenheit by checking the FThenC flag set in api.parseData
        if parsed.FthenC:
            self.temperature_first.configure(text=f"{parsed.temperature_first}°F\n")
            self.temperature_second.configure(text=f"{parsed.temperature_second}°C\n")
        else:
            self.temperature_first.configure(text=f"{parsed.temperature_first}°C\n")
            self.temperature_second.configure(text=f"{parsed.temperature_second}°F\n")   

        self.description.configure(text=f"{parsed.description}")    
        self.humidity.configure(text=f"Humidity: {parsed.humidity}%RH\n")
        self.pressure.configure(text=f"Barometer: {parsed.pressure} mbar\n")
        self.visibility.configure(text=f"Visibility: {parsed.visibility} ft\n", anchor="nw")
        self.uv_index.configure(text=f"UV Index: {parsed.uv}\n")
        self.feels_like.configure(text=f"Feels Like: {parsed.feels_like}°F\n")
        self.wind.configure(text=f"Wind: {parsed.windspeed} mph {parsed.wind_deg_to_cardinal(parsed.direction)}", anchor="nw")

        #Added to update the sayingsbox. tag_configure by ChatGPT(July, 2025)    
        self.sayingsbox.configure(state="normal")      # unlock editing
        self.sayingsbox.delete("1.0", "end")           # clear existing text
        self.sayingsbox.insert("1.0", self.controller.update_quote(parsed.icon_code))    
        self.sayingsbox.tag_add("center", "1.0", "end") # center text
        self.sayingsbox.configure(state="disabled")    # lock editing

        if hasattr(parsed, "daily"):
            self.display_forecast(parsed.daily)
        else:
            print("No forecast data available")
        
        #Bottom Frame
        self.summary.configure(text=f"Summary: {parsed.summary}")

        #Alerts details
        self.alertdetail.delete("0.0", "end")
        if hasattr(parsed, "alertdescription"):
            self.alertdetail.insert("0.0", f"⚠️ Alert Description:\n\n\n {parsed.alertdescription}")

    def about(self):
        self.info_window = ctk.CTkToplevel(fg_color=self.fg_color) 
        self.info_window.title("Jose's Weather App")
        self.info_window.geometry("600x450")


        def on_close():
            self.info_text = None
            self.info_window.destroy()

        self.info_window.protocol("WM_DELETE_WINDOW", on_close)

        self.info_marquis=ctk.CTkLabel(master=self.info_window, text="Weather App by Jose J. Diaz\nJuly and August of 2025",
                              fg_color=self.fg_color,
                              text_color=self.font_color,
                              font=(self.font_style, self.font_size+7))
        
        self.info_text=ctk.CTkTextbox(master=self.info_window,
                              fg_color=self.fg_color,
                              text_color=self.font_color,
                              font=(self.font_style, self.font_size),
                                          width=600, height=420, 
                                          wrap="word"
                             )  
        
        self.info_text._textbox.tag_configure("left-justify", justify='left')
        
        self.info_text.insert("0.0", """\
                              
                              world cities csv from Kaggle: 
                              (https://www.kaggle.com/datasets/juanmah/world-cities)  

                              Default (text-based) icons: Erik Flower's icons 
                              (https://erikflowers.github.io/weather-icons/)

                              Color icons: All come from flaticon.com by deifferent users.

                              default icon (crying unicorn) by flaticon.com user: Luvdat  
                              rain cloud : iconixar 
                              sun, snow, cloudy, overcast, broken clouds day, 
                              fog, thinking emoji: Freepik (http:\\www.freepik.com) 
                              moon: Vectors Market 
                              thunderstorm (both), rain shower day: justicon 
                              rain:Berkhaicon 
                              partly cloudy night: Fantasyou 
                              partly cloudy night 2: Peerapak Takpho 
                              rain night: Plastic Donut 
                              haze: wouldulearn 
                              mist: bqlqn 
                              alert triangle: Andrean Prabowo
                              """           
                              ) 
        
        self.info_text._textbox.tag_add("left-justify", "0.0", "end-1c")

        self.info_text.configure(state="disabled")
        
        
        self.info_marquis.pack(padx=20, pady=5)
        self.info_text.pack(padx=5, pady=5, fill="both", expand=True, side="left")
        self.info_window.wm_transient(self.root)  # Tie to main window
        self.info_window.lift()                   # Bring to front
        self.info_window.focus_force()            # Give focus
        self.info_window.grab_set()   

        # self.info_window.after(4000, self.info_text.destroy)



    def get_pink(self):

        pinkWarning = ctk.CTkToplevel(fg_color="#F1FFAB") 
        pinkWarning.title("PINK THEME WARNING!")   
        pinkWarning.geometry("400x400")

        pink_text_font = ctk.CTkFont(family="Malgun Gothic", size=16, weight="bold")
        pink_text = ctk.CTkTextbox(
                                   master=pinkWarning, 
                                   fg_color="#F8FFD3",
                                   text_color="#000000", 
                                   width=380, 
                                   height=380, 
                                   corner_radius=10,
                                   font=pink_text_font,                                    
                                   wrap="word"
                                )
       
          
       
        pink_text.insert("0.0", "The pink theme is horrific nightmare " \
                                "fuel not meant for weather conditions or any other conditions"
                                " for that matter. That being said, if you REALLY want to see this" \
                                " Lovecraftian horror of color, then press the button. " \
                                "But, dont blame me later for any side effects. Personally, I blame Victoya Venise. " \
                                "She 'inspired' this theme.")
        
       
        pink_text.configure(state="disabled")

              
        def activate_pink():

            self.apply_theme(themes.pink_theme)

            #second message after themes applied
            def update_text():

                pink_text.configure(state="normal")
                pink_text.delete("1.0", "end")
                pink_text.insert("0.0", "Bwahahahaha!!. Feast your eyes on the horror.\n"
                                    "Todays forecast calls for Pepto Bismol rain, and rosy fingered dawns, "
                                    "and probably some ill tempered bass... For good measure.\n\n"
                                    "OR...\nEnjoy and Happy Valentine's Day or something."
                                )
                pink_text.configure(state="disabled")
                
                # Schedule popup close 4 seconds after message appears
                pinkWarning.after(4000, pinkWarning.destroy)

            pinkWarning.after(3000, update_text)
            


        # pink_button = ctk.CTkButton(master=pinkWarning,
        #                             text=f"Open Pink Theme 😨",
        #                             text_color="#FFFFFF",
        #                             bg_color="#964242",
        #                             hover_color="pink",
        #                             font=("Arial", 16),
        #                             command=activate_pink                                    
        #                         )

        pink_button = ctk.CTkButton(
        master=pinkWarning,
        text="Open Pink Theme 😨",
        text_color="#FFFFFF",
        fg_color="#964242",        # <- This controls the button face
        hover_color="pink",        # <- On hover
        font=("Arial", 16),
        command=activate_pink
        )

        pink_button.pack(side="bottom", padx=10, pady=10)      
        pink_text.pack(padx=20, pady=20)
        

        #Window in focusing and bring-to-front code.ChatGPT (July, 2025) 
        # --- Ensure the window pops in front ---
        pinkWarning.wm_transient(self.root)  # Tie to main window
        pinkWarning.lift()                   # Bring to front
        pinkWarning.focus_force()            # Give focus
        pinkWarning.grab_set()               # Make modal (blocks other windows)       


    def apply_theme(self, theme: dict) -> None:

        
        self.bg_color = theme["bg_color"] # Main background color
        self.fg_color = theme["fg_color"] # Frame background color
        
        self.font_color = theme["font_color"] # Text Label color
        self.font_style = theme["font_style"] # Font family
        self.font_size = theme["font_size"] # Font size
        self.button_bg = theme["button_bg"] #Button Color
        self.button_fg = theme["button_fg"] #Button Text Color
        self.icon_color = theme["icon_color"] #Icon color - Forgot this. chatgpt helped me fix it. (chatgpt, July, 2025)
        self.button_bg = self.theme["button_bg"]
        self.button_hover = self.theme["button_hover"]
        #root update 
        self.root.configure(fg_color=self.bg_color)

        #tabs update
        self.tabview._segmented_button.configure(
            fg_color=self.bg_color, 
            text_color=self.font_color,
            selected_color = self.button_bg, 
            selected_hover_color= self.bg_color,
            unselected_color = self.fg_color          
        )

        #MAIN TAB
        self.main_tab.configure(fg_color=self.bg_color)
        
        #LEFT FRAME AND WIDGETS
        self.left_frame.configure(fg_color=self.fg_color) #Change future
        
        self.cityentry.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
        self.citybutton.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size), border_color = self.font_color)
        
        self.citylabel.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
        self.alertslabel.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))  
        self.alertsbox.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))        
        self.sayingsbox.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size)) 

        #RIGHT FRAME AND WIDGETS

        self.spacer_left.configure(fg_color=self.fg_color)
        self.spacer_right.configure(fg_color=self.fg_color)
        self.right_frame.configure(fg_color=self.fg_color)
        self.forecast_frame.configure(fg_color=self.fg_color)
        self.icon_label.configure(fg_color=self.bg_color, text_color=self.icon_color) 
        
    
        #forecast window
        #chatgpt (July, 2025)
        for frame_data in self.forecast_day_frames:

            frame_data["frame"].configure(fg_color=self.fg_color)
            frame_data["day"].configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
            frame_data["icon"].configure(fg_color=self.bg_color, text_color=self.icon_color, font=("Weather Icons", self.font_size + 4))
            frame_data["hi"].configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
            frame_data["lo"].configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))

                
        self.desc_labels = [
            self.location_label,
            self.description,
            self.temperature_second,
            self.humidity,
            self.pressure,
            self.uv_index,
            self.feels_like,
            self.visibility,
            self.wind,
            self.summary

        ]

        
        # Temperature first is set separately so that the font size can be changed.
        self.temperature_first.configure(fg_color=self.bg_color, text_color=self.font_color,font=(self.font_style, self.font_size + 30))
       
        for label in self.desc_labels:            
            label.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))

        #Bottom Frame and widgets
        self.bottom_frame.configure(fg_color=self.fg_color)

        #Alerts page
        self.alertdetails_frame.configure(fg_color=self.fg_color)
        self.alertdetail.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))
    
        #Madlibs page
        self.madlibs_title.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size + 10))
    
        madlibs_dropdowns = [
            self.madlibs_adjective_1,
            self.madlibs_adjective_2,
            self.madlibs_adjectivelabel_1,
            self.madlibs_adjectivelabel_2,
            self.madlibs_adverb_1,
            self.madlibs_adverb_2,
            self.madlibs_adverblabel_1,
            self.madlibs_adverblabel_2,
            self.madlibs_noun_1,
            self.madlibs_noun_2,
            self.madlibs_nounlabel_1,
            self.madlibs_nounlabel_2,
            self.madlibs_verb_1,
            self.madlibs_verb_2,
            self.madlibs_verblabel_1,
            self.madlibs_verblabel_2,            
            self.madlibs_first_file,
            self.madlibs_first_row,
            self.madlibs_second_file,
            self.madlibs_second_row
        ]

        for item in madlibs_dropdowns:
            item.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size))

        self.madlibs_generate.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size), border_color = self.font_color)
        self.madlibs_frame.configure(fg_color=self.fg_color)
        self.madlibs_box.configure(fg_color=self.bg_color, text_color=self.font_color, font=(self.font_style, self.font_size + 10))
        
        #About page
        if hasattr(self, "info_text") and self.info_text is not None and self.info_text.winfo_exists():
            self.info_text.configure(fg_color=self.font_color, text_color=self.bg_color, font=(self.font_style, self.font_size))

       
    def toggle_icon_theme(self):
        enabled = self.dynamic_icons_enabled.get()
        print("Dynamic icon theme is now", "enabled" if enabled else "disabled")
    
        # Update the current weather display:
        if hasattr(self, "current_parsed_data"):
            self.display_weather(self.current_parsed_data)


    def display_forecast(self, daily_data):
        for i, day_data in enumerate(daily_data[1:6]):  # skip today, get next 5
            dt = datetime.fromtimestamp(day_data["dt"])
            day_name = dt.strftime("%a")

            icon_code = day_data["weather"][0]["icon"]
            
            icon = icons.get_icons(icon_code)
            temp_max = round(day_data["temp"]["max"])
            temp_min = round(day_data["temp"]["min"])

            self.forecast_day_frames[i]["day"].configure(text=day_name)
            self.forecast_day_frames[i]["icon"].configure(text=icon)
            self.forecast_day_frames[i]["hi"].configure(text=f"↑ {temp_max}°")
            self.forecast_day_frames[i]["lo"].configure(text=f"↓ {temp_min}°")  

    def show_error(self, message: str, title: str="Oops! An unexpected error occurred."):
        messagebox.showerror(title, message)   

    def generate_madlib(self):
        # 1. Get user words from ComboBoxes
        user_words = {
            "noun1": self.madlibs_noun_1.get(),
            "noun2": self.madlibs_noun_2.get(),
            "verb1": self.madlibs_verb_1.get(),
            "verb2": self.madlibs_verb_2.get(),
            "adverb1": self.madlibs_adverb_1.get(),
            "adverb2": self.madlibs_adverb_2.get(),
            "adjective1": self.madlibs_adjective_1.get(),
            "adjective2": self.madlibs_adjective_2.get()
        }

        # 2. Generate the madlib using MadGenerator instance
        self.mad_generator.user_inputs = user_words
        self.mad_generator.generate_lines()  # selects weather1 and weather2
        madlib_text = self.mad_generator.generate_madlib()

        #Generate weather data
        data1 = self.mad_generator.first_file_info["data"]
        data2 = self.mad_generator.second_file_info["data"]
        
        self.mad_generator.set_weather_data(data1, data2)

        # Generate madlib
        madlib_text = self.mad_generator.generate_madlib()

        # Show it in GUI
        self.madlibs_first_file.configure(text=f"First file: {self.mad_generator.first_file_info.get('filename', "None")}",wraplength = 300, anchor="w")
        self.madlibs_first_row.configure(text=f"Selected row: {self.mad_generator.first_file_info.get('row_index', "None")}", wraplength = 300, anchor="w")
        self.madlibs_second_file.configure(text=f"Second file: {self.mad_generator.second_file_info.get('filename', "None")}")
        self.madlibs_second_row.configure(text=f"Selected row: {self.mad_generator.second_file_info.get('row_index', "None")}")

        self.madlibs_box.configure(state="normal")
        self.madlibs_box.delete("1.0", "end")
        self.madlibs_box.insert("1.0", madlib_text)
        self.madlibs_box.configure(state="disabled")

        # 4. Log to CSV
        madlib_text = self.mad_generator.generate_madlib()

        log_madlib_session(
            filepath=self.mad_generator.filepath,
            file_info1=self.mad_generator.first_file_info,   
            file_info2=self.mad_generator.second_file_info,
            user_words=self.mad_generator.user_inputs,
            madlib_text=madlib_text
            )