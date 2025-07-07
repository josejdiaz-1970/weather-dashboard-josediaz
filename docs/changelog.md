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



