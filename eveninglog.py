import calendar
import os
import log_config
from datetime import date

def writeNewLines(file, numLines):
    for _ in range(numLines):
        file.write("\n")

my_date = calendar.datetime.date.today()
today = date.today()
day_name = calendar.day_name[my_date.weekday()]
filename = str(my_date) + "_pm-log.md"
full_path = log_config.folder_path + filename
f = open(full_path, "a")
header = "# Evening Log for {}, {}".format(day_name, today.strftime("%m/%d/%Y"))
f.write(header)
writeNewLines(f, 1)
if log_config.evening_routines:
    f.write("## Evening Routines")
    writeNewLines(f, 1)
    for routine in log_config.evening_routines:
        f.write("- [] {}".format(routine))
        writeNewLines(f, 1)

if log_config.morning_questions:
    f.write("## Evening Questions")
    writeNewLines(f, 1)
    for question in log_config.evening_questions:
        f.write("### " + question)
        writeNewLines(f, 3)
f.write("### Log: ")
writeNewLines(f, 3)
f.close()
os.system("code " + full_path)