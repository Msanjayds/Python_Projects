# Enter your the Alarm time in your System Time format 12H/24H 

from datetime import datetime
from playsound import playsound

now = datetime.now()
print(now)

alarm_time = input("Enter alaram time in HH:MM:SS AM/PM \n ")
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]

alarm_period = alarm_time[9:11].upper()

print('setting up alarm...')


while True:
    now = datetime.now()
    curr_hr = now.strftime("%I")
    curr_min = now.strftime("%M")
    curr_sec = now.strftime("%S")
    curr_period = now.strftime("%p")

    
    print(alarm_hour,alarm_min,alarm_sec,alarm_period)
    print(curr_hr,curr_min,curr_sec,curr_period)
    
    if(alarm_hour == curr_hr):
        if(alarm_min == curr_min):
            if(alarm_sec == curr_sec):
                print("Time Up...")
                playsound('audio.mp3')
                break        

print('completed')