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
Switched to Erik's Icons. Need to replace the moon icon. I like the default better.
Going to make both day and night themes for different conditions.
Started to write the weather selector

ToDo:

Need to improve the themes, add a separate color for left and right frames.
Need to complete theme selector by weather.
Need to make the color icons 
Night icons are also missing from Eriks Icons. Need to make those.

7-15-25

Moved Summary to Summary Tab, need to expand textbox to take up the whole frame.
Fixed moon icon to use default.

7-16-25

Expanded textbox but I need to center it.

To Do:

Fix funny sayings. Look for an icon mascot.
Write let the weather decide.
Can a command: lambda have more then one statement? No
Move let the weather decide option to Settings: To toggle the Let the weather decide theme.
Add a check option under Settings to toggle themes based on Weather.


Center Alert Summary 
Start working on pulling historical data for Perth Amboy for csv files.
Need to come up with testing scheme. Unit testing, test scripts, etc...
Fix this:
 File "c:\Development\Learning\JTC\Tech Pathways\Weeks\capstone\weather-dashboard-josediaz\weather_gui.py", line 299, in display_weather
    self.alertdetail.insert("0.0", f"Alert Description:\n\n\n {parsed.alertdescription}")
                                                               ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'ParseData' object has no attribute 'alertdescription'. Did you mean: 'description'?

07-20-25

Fixed theme switcher
Started implementing color icons
Started implmenting "Pink theme" Easter Egg"

EasterEgg
use tk.TopLEvel for "pink Theme"

1. User selects pink theme
2. toplevel are you sure?
3. if yes, wait 5 secs, toplevel: ok, dont say I didnt warn you.
4. apply theme. YES!! Embrace the horror! Bwahaha!!...Unless its Feb 14th. In that case, Happy Valentine's Day.
5. Summary: All precipitation will now be Pepto Bismol based.

7-21-25

Resolved to switch to TabView which will fix an issue with ttk.Notebook in a customtkinter window and fonts not being styled
TBD, the whole notebook needs to be converted and I'm afraid of breaking my code. MAy leave this for a weekend.

7-22-25

Attribute: default icon (crying unicorn) by flaticon.com user: Luvdat

rain cloud : iconixar
sun, snow, cloudy, overcast, broken clouds day, fog, thinking emoji: Freepik (http:\\www.freepik.com)
moon: Vectors Market
thunderstorm (both), rain shower day: justicon
rain:Berkhaicon
partly cloudy night: Fantasyou
partly cloudy night 2: Peerapak Takpho
rain night: Plastic Donut
haze: wouldulearn
mist: bqlqn
alert triangle: Andrean Prabowo


7-23-25

Converted tk.notebook to ctk.Tabview. Got it working.
Pulled some data for team project.
Started the sayings.py file.

welcometothejungle - jobs
talentnova

7-24-25

Got picture icons working. Need more of them. Also got the switching to work. 
May add color icons to 5 day as well.

To Do: Need to decide on icons for all weather conditions.

7-26-25

Finished icon selection and integration.
Added warning and thinking emoji icon.
Fixed some minor errors with alert display. 
Imported worldcities.csv for autocomplete function - future
Fix the lat is None or Lat is none error in api.py

To Do:

Team feature
Autocomplete function

Extra: Charts page with historical data imports

Blockers: Current issue with current icon colors for text icons
Fixed
Need to work on cycling thru funny sayings and team project.

7-27-25

Completed sayings.
Completed Easter Egg.
Started Team project
Created word file


ToDo:

Finalize error conditions. 
Add one for misspelled city or consider adding an autocomplete feature with a dropdown menu.
Testing (pytest?)

Historical chart window USer selects length of time to get.

7-28-25

Added basic structure for Madlibs

7-31-25

Working through some parsing errors with madlibs and csvs.

Create a standalone installer. No

8-1-25

Needs a slide deck
Needs to be tagged v1.0 in github. Under releases.
Autocomplete, incorrect city error messsage
Add madlibs widgets to themes
Fix lat none error
Fix emoji error

Reverted to previous build after chatgpt runaround with icons. Will suppress warnings instead.
ToDo:

Change default color of rain button
Change focus color of button on sunny theme