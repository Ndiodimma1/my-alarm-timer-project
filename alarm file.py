# An alarm/timer project...

from playsound3 import playsound
import time
import sys

# Defining my list of alarm sounds
alarm_sounds = ["alarm1.mp3", "alarm2.mp3", "alarm3.mp3"]

# creating a custom function for the countdown
def countdown(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # I wish to display the countdown in MM:SS format
        sys.stdout.write(f"\r{minutes_left:02}:{seconds_left:02}")
        sys.stdout.flush()


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = (minutes * 60) + seconds


print("Select an alarm sound:\n1. alarm1.mp3\n2. alarm2.mp3\n3. alarm3.mp3")


choice = int(input("Enter the number of your choice (1-3): ")) - 1


if 0 <= choice < len(alarm_sounds):
    selected_alarm = alarm_sounds[choice]
else:
    print("Invalid choice. Using alarm1.mp3 by default.")
    selected_alarm = alarm_sounds[0]


countdown(total_seconds)

playsound(selected_alarm)

