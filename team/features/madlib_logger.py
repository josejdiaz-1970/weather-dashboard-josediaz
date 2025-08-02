#madlib_logger.py
#Logs all of the choices made by the user, the randomly selected weather data, and final madlibs

import csv
import os
from datetime import datetime

def log_madlib_session(
    filepath,  # path to the output CSV
    user_words,  # dict: {"Noun": ..., "Verb": ..., etc.}
    file_info1,  # dict with file1 info
    file_info2,  # dict with file2 info
    madlib_text  # final madlib sentence
):
    
    filepath_full = os.path.join(filepath, "madlib_logger.csv")
    file_exists = os.path.isfile(filepath_full)

    with open(filepath_full, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Timestamp", "Noun", "Verb", "Adjective", "Adverb",
            "File1", "Row1", "City1", "Temp1", "Humidity1", "Wind1",
            "File2", "Row2", "City2", "Temp2", "Humidity2", "Wind2",
            "Madlib"
        ])
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Timestamp": datetime.now().isoformat(),
            "Noun": user_words.get("Noun", ""),
            "Verb": user_words.get("Verb", ""),
            "Adjective": user_words.get("Adjective", ""),
            "Adverb": user_words.get("Adverb", ""),
            "File1": file_info1.get("filename", ""),
            "Row1": file_info1.get("row_index", ""),
            "City1": file_info1["data"].get("City", ""),
            "Temp1": file_info1["data"].get("Temperature", ""),
            "Humidity1": file_info1["data"].get("Humidity", ""),
            "Wind1": file_info1["data"].get("Wind_Speed", ""),
            "File2": file_info2.get("filename", ""),
            "Row2": file_info2.get("row_index", ""),
            "City2": file_info2["data"].get("City", ""),
            "Temp2": file_info2["data"].get("Temperature", ""),
            "Humidity2": file_info2["data"].get("Humidity", ""),
            "Wind2": file_info2["data"].get("Wind_Speed", ""),
            "Madlib": madlib_text
        })
