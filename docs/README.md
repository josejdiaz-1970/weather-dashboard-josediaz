# weather-dashboard-josediaz
### Jose Diaz
### TPS25 Capstone Project

### Overview:

This program is a weather app for the TPS25 capstone project. It reads weather 
data from an API (https://api.openweathermap.org/data/3.0/onecall) and displays it on the screen. 

### How to use:

*See **user_guide.md***

### Current files:

1. **main.py** - This is the main program which calls the API, gets the data, and transfers it to the GUI.
It is planned that most requests that involve acquisition or storage of data will go through main.

2. **weather_gui.py** - The frontend of the app. Will display data based on the city selected.
And allow for data to be saved to a text file. Once a successful API call is made, data is automatically saved to weather_data.csv

3. **config.py** - Currently not used.

4. **data/** folder - Where all relevant data will be stored. This is where the weather_data.csv will be located.

5. **docs/** folder - This folder weill contain the readme, user guide, and a changelog. The changelog is just like a diary of progress I make throughout the project. 

6. **features/** folder - Future feature files and enhancements will live here. This is where the feature python files will exist.

7. **screenshots/** folder - Screenshots will be placed here. Also here will be the program diagrams. 