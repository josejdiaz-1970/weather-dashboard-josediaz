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
            "weather_data_victoya.csv",
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

        print("First File Info:", self.first_file_info) #TESTING
        print("Second File Info:", self.second_file_info) #TESTING


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

    def generate_madlib(self): #changed from generate
        self.template = random.choice(templates)

        combined_data = {
            **self.user_inputs,
            **self.weather1,
            **self.weather2
        }

        try:
            return self.template.format(**combined_data)
        except KeyError as e:
            return f"Missing placeholder data: {e}"        

    def log_madlib(self, user_words: dict, madlib_text: str, output_csv="madlib_log.csv"):
        log_path = os.path.join(self.filepath, output_csv)

        data = {
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "First File": self.first_file_info.get("filename", ""),
            "First City": self.first_file_info.get("data", {}).get("city", ""),
            "Second File": self.second_file_info.get("filename", ""),
            "Second City": self.second_file_info.get("data", {}).get("city", ""),
            "User Words": user_words,
            "Completed Madlib": madlib_text
        }

        # First, check if the file exists
        file_exists = os.path.isfile(log_path)

        try:
            with open(log_path, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())

                if not file_exists:
                    writer.writeheader()

                writer.writerow(data)

        except Exception as e:
            print(f"Logging failed: {e}")


# --- TEST CODE: Run this file directly to try it ---
if __name__ == "__main__":
    csv_folder_path = r"C:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\team\data"

    madlib = MadGenerator(filepath=csv_folder_path)
    madlib.generate_lines()

    # Example access
    print("\nSummary:")
    for i, info in enumerate([madlib.first_file_info, madlib.second_file_info], 1):
        print(f"File {i}: {info['filename']} (row {info['row_index']})")
        print("Data:", info['data'])