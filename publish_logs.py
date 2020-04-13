import os
import log_config
import calendar


my_date = calendar.datetime.date.today()

os.chdir(log_config.folder_path)
os.system("git add .")
os.system("git commit -m " + "\"publish logs for " + str(my_date) +"\"")
os.system("git push -u origin master")