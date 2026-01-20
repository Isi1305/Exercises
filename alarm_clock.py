# In this file I tried recreating the simple alarm clock from Jabromen (Jeff Bromen) as practice.
# I only know the import random so far from all the imports given.

import datetime # current date/time, comparing timestamps and generating timestamps
import os # Contact with the Operating System, Query files & folders, build paths and read environment variables
import time # Let time "pass by" or measure it, take breaks or measure durations
import random # Generates randomness
import webbrowser # Opens Websites, URLs

if not os.path.isfile("youtube_alarm_videos.txt"):
  print("Creating 'youtube_alarm_videos.txt'")
  with open("youtube_alarm_videos.txt", "w") as alarm_file:
    alarm_file.write("https://www.youtube.com/watch?v=OLtT69fZIS0&list=RDOLtT69fZIS0&start_radio=1")

def 
