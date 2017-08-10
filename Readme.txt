# Digital Life Hacks: About this Repository

This repository is dedicated to miscellaneous projects that I’ve created to make life easier. Each folder is a self-contained project. 

The following sections provide descriptions and deployment information for each of the KiCAD utilities included in this repository. 


## DLH #1: 

Have you ever wanted to automatically send text messages to your friends on their birthdays? Or maybe you wanted to randomly send check-in messages to your long-distance friends every few weeks just to keep in touch?

This script allows you to set up random texts or preset scheduled texts to multiple friends from your computer. Once set-up, sit back and relax and let the scheduler do the sending at the dates and times you specify!

### System Requirements
* Only compatitble with Mac OS
* Should be run using Python 3
* Requires the CronTab module

### How To Use


* Running the .py file will open the textScheduler.xlsm file. Click “ok” to enable macros

* The Unique Tagname field is used to identify the group of scheduled texts, and to allow for future deletion or modification of all tasks with a similar Tagname 

* If you want to set up random messaging to one user, fill out the “Random” tab:
	** Enter the name and number of the recipient
	** Messages will always be sent within the time interval specified
	** The full Date Interval will be split evenly into “n” smaller intervals, where “n” equals the number of messages to send. A message will be sent at a random date within a given smaller interval. 
	** The number of messages per week determines the frequency of messages. This can be a fractional number 
	** The messages will be randomly selected from the message list
	** Note that messages will not be sent to the user on weekends
	 
* If you want to set up messages to multiple users, fill out the Multi_person tab
	** For each line, fill out name, number, date, time and message
	** Incomplete lines will be ignored

* Click Generate, the results will be found under the Autogen_Results tab, and in the separate textSchedule.csv file that will be created/updated in the folder. 



### Compatibility and Versioning

Tested Operating Systems: Tested on Windows 10 and OSX 10.12.4   
Written with Python 3.0



## Authors

* **Brittany Scheid**

## License

This project is free for public use. 


Features: 
- Be able to schedule when a text is sent
- Be able to select text sending frequency and times
- Be able to input multiple numbers for a text
- Be able to select randomly from a list of messages
- Be able to turn on or turn off service


Implementation Ideas: 

1) Use an excel spreadsheet to input names and numbers 
	- Next iteration: you can select from contacts
2) Use an excel spreadsheet to calculate set times and dates based on user preferences

3) Use  

4) Run sendTxt.applescript
