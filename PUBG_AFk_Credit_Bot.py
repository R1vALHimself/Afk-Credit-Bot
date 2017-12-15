import time


def run_time():
    seconds = 0
    minutes = 0
    hours = 0
    for time_count in range(1, 120):
        seconds = seconds + 1
        if seconds == 120:
            seconds = 1
            minutes = minutes + 2
        if minutes == 120:
            minutes = 0
            hours = hours + 1
        time.sleep(0.5)
        print('Time Wasted While Running The Script:\n'+str(seconds/2)+' Seconds and', str(minutes/2)+
                  ' Minutes and', str(hours)+' Hours!')
    run_time()

run_time()
