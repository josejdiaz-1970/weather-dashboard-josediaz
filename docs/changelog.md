# Change log for Weather Dashboard project

## Note:

This file was added so I could keep track of thingd I'm currently working on and their status. Also of changes 
made and why.

6/28/25

1. Created a new diagram for the project. See **TPS25 Capstone diagram ver 1.jpg**. The main reason for this was to consolidate the data storage and acquisition functions into one file but two separate modules. 

6/29/25

1. Created changelog.md in **docs/** folder.
2. Moved diagrams to **screenshots/** folder.

07-01-25

Personalization: Add random quotes based on the weather conditions. Make them funny. Random.
Also, I realized based on my past assignments, that I need make a plan for this app FIRST before coding. So over the next few days I'm focusing on that in addition to getting the core done.

07-04-25

Added some basic GUI components and started to frame out the GUI in MVC style. Needed some help from chatGPT for this.
To Do:

1. Need to get city data to the LoadAPI and then back to the gui window
2. Need to dave data into a csv file: Copy that part from week 10 assignment.

07-05-25

Added save data functionality and fixed a lot of the back and forth with data to and from main.
The core components now all work. A city is entered in weather_gui.py then data is retrieved with api.py into main and passed back to the gui. It is also saved into a running .csv. The GUI is very basic at this time. I could just copy parts from assignments, but I think slogging through it this way helps me learn it better. Especially the MVC method. 

To Do:

1. Fix the gui so that text is not displayed in a text box.
2. Clean up gui so that colors can be switched by theme switcher.

Started to change over the results from one text box to a set of labels.

07-06-25

Started working on the the Themes feature
Currently have dark and light themes as well as a default.
Switched to customtkinter and am currently updating display and themes

To DO:

Rename: Current conditions to Get Weather
Move the data to the left frame?
Add "feels like" temperature
Need to clean up the themes. there are discrepancies in how it displays. 

Completed above items except themes.

Completed:

1. Cleaned UI and now I'm in the process of adding icons. I suck at UI design but got some ideas from UI pages and chatGPT. Picked an overall design.
2. Completed the switchover from tkinter to customtkinter. All except menus which are not implemented in ctk.
3. Completed basic switchover to One Call API 3.0,
4. Added 5-Day forecast. Just basic icons and hi, low temperatures.
5. Removed sunrise, sunset, and time. Replaced with Feels like temperature, UV Index.
6. Combined city into location ocmposite which encompasses city, state (if available), and country.

Need to fix some layout issues with labels. Which go out of whack when temperature gets big.

07-08-25

Just thought of modifying the temperature reading to read both in F and C. In this
format, the F will be big / the C will be small. Except in any other country but the US and UK which will reverse it.

07-09-25

Finished the F/C code and it works. Got the list of countries that primarily use Celsius and implemented
the code changes. Need to work on polishing up the GUI widget placement since there are missing labels 
and errors in placement and the icons.

Idea: Thinking of saving API call statistics and maybe issuing a warning when kyou get too close to the limit. 
Also, color changes in temp/ feels like/ humidity. Maybe. 

07-10-25

"Add to Sayings:"

"Eos d' erchomenē, rhododaktylos, exéphēne"
"When the child of morning, rosy-fingered Dawn, appeared..." - Homer - The Odyssey

Do you know what 'meteorologist' means in English? It means liar.

Lewis Black

Need to address what happens when lat and lon are not found. May also consider implementing an autocomplete function.

UI categories:

        City State Country

        Temperature F/ C

        Description

Feels Like <temp> Wind <dir. marker icon> <speed> mph
Visibility Baromter <pressure> mbar   Humidity %RH

07-11-25

Fixed wind speed and direction display.

07-12-25

Working on GUI but have the following issue:

Need to add color icons

The day_frame is set 5 times to represent the 5 days within the forecast_frame

Issue is that it only colors one of the day_frames

Need to expand summary to two columns


Fixed: When alerts key is not available, wrapped the check for it in a
try: 
   if alerts
except:
   KeyError:
   set alerts to summary    


7-13-25

moved icons to weather_icons.py

Added the rest of the preliminary themes.
Going to make both day and night themes for different conditions.
Started to write the weather selector


