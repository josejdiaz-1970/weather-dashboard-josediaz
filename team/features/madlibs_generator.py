#madlibs_generator.py
#Tps25-Capstone
#Date: 02-Aug-2025

'''
class MadGenerator:
This class is responsible for genrating the final madlib. It pulls in the team files, and selects two random files,
then from those files, it selects two random lines. It uses some data in the two rows as part of the madlib along 
with words selected by the user in the gui.

MadGenerator implements the following methods:

get_unique_file_pair(self): Selects a random pair of files from the team files provided.

get_random_row_from_file(self, filename): Selects a random row from each file selected.

generate_lines(self): Sets selctions to parameters for use by both the gui and other methods.

set_user_inputs(self, noun, verb, adjective, adverb): user inputs are stored from the selections
made at the time that the "generate madlib" button on the UI is pressed.

set_weather_data(self, data1, data2): sets the user inputs dictionary.

generate_madlib(self): Selects a random madlib template from templates.py and generates the madlib 
with all the information acquired

'''

import os
import csv
import random
import datetime

#Import the madlibs template
from team.features.madlib_templates import templates

class MadGenerator:
    def __init__(self, filepath):
        self.filepath = filepath
        self.weather_files = [
            "weather_data_jjd.csv",
            "weather_data_tommy.csv",
            # "weather_data_victoya.csv",
            "weather_reading_margarita.csv",
            "weather_reading_shanna.csv"
        ]

        self.first_file_info = {}
        self.second_file_info = {}

        self.template = None
        self.user_inputs = {}   # Placeholder for nouns, verbs, adjectives, adverbs the user selects
        self.weather1 = {}
        self.weather2 = {}

    def get_unique_file_pair(self):
        return random.sample(self.weather_files, 2)

    def get_random_row_from_file(self, filename):
        full_path = os.path.join(self.filepath, filename)
        try:
            with open(full_path, mode="r", newline="", encoding="utf-8") as f:
                reader = list(csv.DictReader(f))
                if not reader:
                    raise ValueError(f"{filename} is empty or invalid.")
                index = random.randint(0, len(reader) - 1)
                row = reader[index]

                # Normalize keys to lowercase
                normalized_row = {key.lower(): value for key, value in row.items()}

                return {
                    "filename": filename,
                    "row_index": index,
                    "data": {
                        "city": normalized_row.get("city", ""),
                        "temperature": normalized_row.get("temperature", ""),
                        "humidity": normalized_row.get("humidity", ""),
                        "wind_speed": normalized_row.get("wind_speed", "")
                    }
                }
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            return {
                "filename": filename,
                "row_index": -1,
                "data": {}
            }

    def generate_lines(self):
        file1, file2 = self.get_unique_file_pair()
        self.first_file_info = self.get_random_row_from_file(file1)
        self.second_file_info = self.get_random_row_from_file(file2)

       
    def set_user_inputs(self, noun, verb, adjective, adverb): #changed from noun to noun1
        self.user_inputs = {
            "noun1": noun,
            "verb1": verb,
            "adjective1": adjective,
            "adverb1": adverb
        }

    def set_weather_data(self, data1, data2):
        self.weather1 = {
            "city1": data1["city"],
            "temperature1": data1["temperature"],
            "humidity1": data1["humidity"],
            "wind_speed1": data1["wind_speed"]
        }
        self.weather2 = {
            "city2": data2["city"],
            "temperature2": data2["temperature"],
            "humidity2": data2["humidity"],
            "wind_speed2": data2["wind_speed"]
        }

    #Using **to unpack a dictionary into its key/value pairs. Function selects a random template and combines it with the user data
    #stored in dictionaries to generate the madlib.
    #ChatGPT(July, 2025)    
    def generate_madlib(self): #changed from generate
        self.template = random.choice(templates)

        #Chatgpt (July, 2025)
        combined_data = {
            **self.user_inputs,
            **self.weather1,
            **self.weather2
        }

        try:                      
            madlib_full = self.template.format(**combined_data)       

            return madlib_full
        except KeyError as e:
            return f"Missing placeholder data: {e}"        
