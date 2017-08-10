import os
import csv
from crontab import CronTab
import subprocess


#Update schematic file with .csv
def CSVToCrontab(dirpath,csvFilename):

    #loads 2d array from .csv file
    with open("textSchedule.csv", 'rU') as f:
        reader= csv.reader(f)
        filearray = list(reader)

        print(filearray)

    CSVToCrontabHelper(dirpath, filearray)
    return filearray
     

def CSVToCrontabHelper(dirpath, filearray):
    
    #remove old jobs with same ID
    for set_job in my_cron:
        if set_job.comment== filearray[1][group_id]:
            my_cron.remove(set_job)
            my_cron.write()
        
    for i in range(1, len(filearray)):
        if filearray[i][isWeekend] == "True":
            continue
        job= my_cron.new(command='osascript '+ dirpath + '/sendTxt.applescript ' + filearray[i][number] + ' "'+filearray[i][message]+'"', comment=filearray[i][group_id])
        job.minute.on(filearray[i][minute])
        job.hour.on(filearray[i][hour])
        job.day.on(filearray[i][day])
        job.month.on(filearray[i][month])
        my_cron.write()
        

def removeMessagesById(id_str):

    #remove old jobs with same ID
    for set_job in my_cron:
        if set_job.comment== id_str:
            my_cron.remove(set_job)
            my_cron.write()
    


if __name__== "__main__":

    #Define Indices
    minute=1
    hour=2
    day=3
    month=4
    isWeekend=5
    name=6
    number=7
    group_id=8
    message=9

    print('Open File then click "generate"')

    #Open Excel File
    os.system("open -a 'Microsoft Excel.app' 'textScheduler.xlsm'")
    dirPath=os.getcwd()
    my_cron=CronTab(user=os.environ['HOME'].split('/')[-1])

    setSchedule=input("Set text schedule with data from textSchedule.csv (y/n)? ")
    if setSchedule=="y":
        filearray=CSVToCrontab(dirPath, 'textSchedule.csv')

    print('Current Crontab jobs are as follows: ')
    for set_job in my_cron:
        print(set_job)

   #Allow Users to Cancel Scheduled Jobs
    cancel=""
    while(cancel!="e"):
        cancel=input("Input ID of schedules you want to cancel, or type 'e' to exit: ")
        if cancel=="e":
            break
        removeMessagesById(cancel)
        
        print('Current Crontab jobs are as follows: ')
        for set_job in my_cron:
            print(set_job)
        
   


