import datetime
from tkinter import *


# 'root' window is top level window that contains everything alse and does not have a parent
root = Tk()
root.title("Dates") # window title
root.geometry('500x250') # windows size

w = Label(root, text='Cieżko to nazwać', font='45')
w.pack()

upper_frame = Frame(root)
upper_frame.pack()

mid_frame = Frame(root)
mid_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack()

def start_time():
    global start
    start = datetime.datetime.now()
    start_time_label.config(text=f'{start.hour}:{start.minute}:{start.second}')
    stop_time_label.config(text='')

def stop_time():
    global stop
    stop = datetime.datetime.now()
    if stop.date == start.date:
        stop_time_label.config(text=f'{stop.hour}:{stop.minute}:{stop.second}')
    elif stop.date != start.date:
        stop_date = stop.date()
        start_date = start.date()
        stop_time_label.config(text=f'{stop_date}  {stop.hour}:{stop.minute}:{stop.second}')
        start_time_label.config(text=f'{start_date}  {start.hour}:{start.minute}:{start.second}')

l1 = Button(upper_frame, text='Start', background='#50C7C7', command=start_time)
l1.pack(side=RIGHT)

start_time_label = Label(mid_frame, text="")
stop_time_label = Label(mid_frame, text="")
start_time_label.pack()
stop_time_label.pack()

l2 = Button(bottom_frame, text='Stop', background='#5063C7', command=stop_time)
l2.pack(side=LEFT)

# run
if __name__=="__main__":
    root.mainloop()

