# In this file I tried recreating the simple alarm clock from Jabromen (Jeff Bromen) as practice.
# I only know the import random so far from all the imports given.

import datetime # current date/time, comparing timestamps and generating timestamps
import os # Contact with the Operating System, Query files & folders, build paths and read environment variables
import time # Let time "pass by" or measure it, take breaks or measure durations
import random # Generates randomness
import webbrowser # Opens Websites, URLs

if not os.path.isfile("youtube_alarm_videos.txt"): # Testing if a file exists
  print("Creating 'youtube_alarm_videos.txt'")
  with open("youtube_alarm_videos.txt", "w") as alarm_file: # Opens file to write
    alarm_file.write("https://www.youtube.com/watch?v=OLtT69fZIS0&list=RDOLtT69fZIS0&start_radio=1") # Writes link into file

def check_input(alarm_time):
  if len(alarm_time) == 1: # Hour
    if alarm_time[0] < 24 and alarm_time[0] >= 0: # tests if the hour is between 0 and 23
      return True
  if len(alarm_time) == 2: #Hour and minute
    if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
    alarm_time[1] < 60 and alarm_time[1] >= 0:
      return True
  elif len(alarm_time) == 3: # Hour, minute and second
    if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
    alarm_time[1] < 60 and alarm_time[1] >= 0 and \
    alarm_time[2] < 60 and alarm_time[2] >= 0:
      return True
    return False

print("Set a time.")
while True:
  alarm_input = input()
  try:
    alarm_time = [int(n) for n in alarm_input.split(":")]
    if check_input(alarm_time):
      break
    else:
      raise ValueError
  except ValueError:
    print("Error: Enter time in HH:MM or HH:MM:SS format")

seconds_hms = [3600, 60, 1] # Number of secinds in an hour, minute and second
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Get the current time
now = datetime.datetime.now() 
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

time_diff_seconds = alarm_seconds - current_time_seconds # Calculates the number of seconds til alarm goes off

if time_diff_seconds < 0: # If time difference is negative, set alarm for next day
  time_diff_seconds += 86400 # Number of seconds in a day

print(f"Alarm set to go off in {datetime.timedelta(seconds=time_diff_seconds)}")

time.sleep(time_diff_seconds) # Sleep until the alarm goews off

print("Wake up!")

# Loads list of possible URLs
with open("youtube_alarm_videos.txt", "r") as alarm_file:
  videos = alarm_file.readlines()

# Opens a random video
webbrowser.open(random.choice(videos))
