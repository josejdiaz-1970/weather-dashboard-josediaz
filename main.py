#main.py 

import api
from weather_gui import WGUI
import tkinter as tk

class App():
    
    def __init__(self, root):

        self.root = root
        self.gui = WGUI(self.root, self)
        
if __name__ == "__main__": 
    root = tk.Tk()
    app = App(root)
    root.mainloop()







