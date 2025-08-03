#citylist.py
#Tps25-Capstone
#Date: 02-Aug-2025

'''
class Cities:
Parses a list of cities from worldcities.csv and make it availble to the combobox selector in weather_gui.py
through main.

Cities implements the following methods:

load_city_names(): Loads cities from worldcities.csv, creates a pandas dataframe and sorts them. Also only selects unique
names. Returns the sorted dataframe.


'''


#Inputs:

import os
import csv
import pandas as pd

class Cities():
    def __init__(self, filepath):
        
        self.file_path_csv = filepath


    def load_city_names(self, csv_path="worldcities.csv"):
        try:
            full_file_path = os.path.join(self.file_path_csv ,csv_path)
            df = pd.read_csv(full_file_path)

            df["formatted_name"] = df.apply(
            lambda row: f"{row['city']}, {row['admin_name']}, {row['country']}" if row["admin_name"] 
            else f"{row['city']}, {row['country']}", 
            axis=1)

            return sorted(set(df["formatted_name"].unique()))



            # return sorted(set(df["city"].dropna().unique()))
       
        except Exception as e:
           if self.error_handler:
               self.error_handler("City Data Error", f"Unable to load city data:\n{e}")
           return []
