
import time  # This program is just a basic clock
start = input('Input time H:MM: ')
start = start.split(':')
hour = int(start[0])
minute = int(start[1])
while True:
    if minute == 59:
        hour +=1
        minute = -1
    if hour == 13:
        hour = 1
    time.sleep(1)
    minute += 1
    
    if len(str(minute)) == 1:
        current = (str(hour)+':'+'0'+str(minute))
    else:
        current = (str(hour)+':'+str(minute))
    print(current)