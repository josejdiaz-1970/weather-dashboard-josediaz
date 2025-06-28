#weather_gui.py

import tkinter as tk

class WGUI():

    def __init__(self, root, controller):

        self.root = root
        self.controller = controller

        root.title("My Weather App")
        root.geometry("800x400")
        root.configure(bg="#36A1E4")
       
        self.citybutton = tk.Button(text="Enter a City")
        self.citybutton.pack()   



        