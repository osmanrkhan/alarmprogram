import webbrowser

from datetime import datetime, timedelta

print "Set an alarm, friend."

day = raw_input("Gimme a day: ")
month = raw_input("Gimme the month: ")
year = raw_input("Gimme a year: ")
hour = raw_input("Gimme an hour: ")
minute = raw_input("Gimme a minute: ")
seconds = raw_input("Gimme a second: ")
current_time = datetime.now()
date_ur = datetime(int(year), int(month), int(day), int(hour), int(minute), int(seconds), 0)

print date_ur
print current_time


while current_time != date_ur:
	print "\n"
	current_time = datetime.now()
	if current_time == date_ur:
		print "WAKE UP" * 20
		webbrowser.open('https://www.youtube.com/watch?v=GxDQWtXSVpA')

