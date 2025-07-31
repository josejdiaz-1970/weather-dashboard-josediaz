# weather-dashboard-josediaz
### Jose Diaz
### TPS25 Capstone Project

## Description:

This program is a weather app for the TPS25 capstone project. It reads weather 
data from an API (https://api.openweathermap.org/data/3.0/onecall) and displays it on the screen. 

## Installation:
None required

## Credits:

### Icons:

Weather icons provided by [Erik Flowers](https://erikflowers.github.io/weather-icons/)
Licensed under the [SIL Open Font License 1.1](https://scripts.sil.org/OFL)
Various other icons are obtained from flaticons.com:

Special thanks to the following artists on flaticon.com:

default icon (crying unicorn): ***Luvdat***
rain cloud : ***iconixar***
sun, snow, cloudy, overcast, broken clouds day, fog, thinking emoji: ***Freepik (http:\\www.freepik.com)***
moon: ***Vectors Market***
thunderstorm (day and night), rain shower day: ***justicon***
rain: flaticon.com user: ***Berkhaicon***
partly cloudy night: ***Fantasyou***
partly cloudy night 2: ***Peerapak Takpho***
rain night: ***Plastic Donut***
haze: ***wouldulearn***
mist: ***bqlqn***
alert triangle: ***Andrean Prabowo***


## Usage:

The application only has a handful of basic controls. Users can select a specific weather theme or let the 
theme be updated based on the weather conditions of the selected city. In addition, users can select between
Erik Flower's Icons and Dynamic Color Icons. Both of these options are selectable in the Menu.

To pull up data for a city. Enter a valid city into the text box on the upper left hand side of the application. Then press get weather.

The following happens:
On the left hand side:
Any alerts are displayed inthe Alrts section. If there is an active alert for your city. Select the Alert Details tab for the full text of the alert.
Below the thinking emoji, a weather related phrase or joke will appear which will update with each weather fetch.

On the right hand side:
An icon representing the current conditions is displayed.
The current weather is selected and displayed. 
A 5-Day forecast is displayed.


## Current files:

1. **main.py** - This is the main program which calls the API, gets the data, and transfers it to the GUI.
It is planned that most requests that involve acquisition or storage of data will go through main.

2. **weather_gui.py** - The frontend of the app. Will display data based on the city selected.
And allow for data to be saved to a text file. Once a successful API call is made, data is automatically saved to weather_data.csv

3. **config.py** - Currently not used.

4. **data/** folder - Where all relevant data will be stored. This is where the weather_data.csv will be located.

5. **docs/** folder - This folder will contain the readme, user guide, and a changelog. The changelog is just like a diary of progress I make throughout the project. 

6. **features/** folder - Future feature files and enhancements will live here. This is where the feature python files will exist.

7. **screenshots/** folder - Screenshots will be placed here. Also here will be the program diagrams. 