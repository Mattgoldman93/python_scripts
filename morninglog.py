#!/usr/bin/env python3

import calendar
import os
import log_config
from datetime import date

def writeNewLines(file, numLines):
    for _ in range(numLines):
        file.write("\n")
def writeGratitudes(file, n):
    file.write("### {} Gratitudes:".format(n))
    writeNewLines(f,1)
    for i in range(n):
        file.write("{}.".format(i + 1))
        writeNewLines(f,1)

my_date = calendar.datetime.date.today()
today = date.today()
day_name = calendar.day_name[my_date.weekday()]
filename = str(my_date) + "_am-log.md"
full_path = log_config.folder_path + filename
f = open(full_path, "a")
header = "# Morning Log for {}, {}".format(day_name, today.strftime("%m/%d/%Y"))
f.write(header)
writeNewLines(f, 1)
if log_config.morning_routines:
    f.write("## Morning Routines")
    writeNewLines(f, 1)
    for routine in log_config.morning_routines:
        f.write("- [] {}".format(routine))
        writeNewLines(f, 1)

if log_config.morning_questions:
    f.write("## Morning Questions")
    writeNewLines(f, 1)
    for question in log_config.morning_questions:
        f.write("### " + question)
        writeNewLines(f, 3)
writeGratitudes(f, 3)
f.write("### Log: ")
writeNewLines(f, 3)
f.close()
try:
    os.system("code " + full_path)
except:
    os.system("open " + full_path)
