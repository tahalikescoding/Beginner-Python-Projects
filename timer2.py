import time
import datetime as dt

timer = input("Timer: ")
ftime = dt.datetime.strptime(timer , "%H:%M:%S").time()
seconds = ftime.hour*3600 + ftime.minute*60 + ftime.second
while seconds>-1:
    hours , remainder = divmod(seconds , 3600)
    minutes , second = divmod(remainder , 60) 
    print(f"\r{hours:02d}:{minutes:02d}:{second:02d}" , end = "")
    time.sleep(1)
    seconds-=1
print()
print("TIMES UP")