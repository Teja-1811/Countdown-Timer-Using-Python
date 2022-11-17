from tkinter import *
import time as ti
from datetime import time as dt
from threading import *

class CountDown:

    def __init__(self,window):

        #Window Properties
        self.window=window
        self.window.title("CountDown Timer")
        self.window.geometry("400x460")
        self.window.configure(bg="black")
        self.window.resizable(width=False,height=False)
        self.pause=False

        #creating the CountDown Timer
        countdown=Label(self.window,text="CountDown Timer",
                        bg="black",fg="white",height=2,
                        font=("Times New Roman",20,"bold italic"))
        countdown.pack()

        #Creating the clock
        self.current_time=Frame(self.window,bg="white",
                                height=32,width=280)
        self.current_time.place(x=60,y=60)

        current_time_label=Label(self.window,text="Current Time   ",
                                 bg="black",fg="#D2125F",
                                 font=("Times New Roman",15,"bold"))
        current_time_label.place(x=62,y=62)

        #Creating the class for current time

        def clock():
            clock_time=ti.strftime(f"%H : %M : %S   %p")
            current_time.config(text=clock_time)
            current_time.after(1000,clock)
        current_time=Label(self.window,bg="black",fg="red",
                           font=("Times New Roman",15,"italic"))
        current_time.place(x=194,y=62)
        clock()

        #Set Time
        set_time=Label(self.window,text="Set Timer",bg="black",
                       fg="white",font=("Times New Roman",18,"bold"))
        set_time.place(x=145,y=100)

        #Labels  --> Hours,Minutes and Seconds

        hours_label=Label(self.window,text="Hours : ",bg="black",
                          fg="white",font="Times 14 bold")
        hours_label.place(x=20,y=135)
        minutes_label=Label(self.window,text="Minutes : ",bg="black",
                            fg="white",font="Times 14 bold")
        minutes_label.place(x=120,y=135)
        seconds_label=Label(self.window,text="Seconds : ",bg="black",
                            fg="white",font="Times 14 bold")
        seconds_label.place(x=235,y=135)

        #Declaring the hours,minutes and seconds variables
        #They returns the data from the entry widgets
        self.hours=IntVar()
        self.minutes=IntVar()
        self.seconds=IntVar()

        #Taking input from the user by using Entry Widget (hours, minutes, seconds)
        self.hours_entry=Entry(self.window,textvariable=self.hours,
                               width=2,
                          relief=FLAT,fg="Green",bg="White",
                          font="Times 14 italic")
        self.hours_entry.place(x=90,y=136)
        self.minutes_entry=Entry(self.window,textvariable=self.minutes,
                                 width=2,
                            relief=FLAT,fg="Green",bg="White",
                            font="Times 14 italic")
        self.minutes_entry.place(x=205,y=136)
        self.seconds_entry=Entry(self.window,textvariable=self.seconds,
                                 width=2,
                            relief=FLAT,fg="Green",bg="White",
                            font="Times 14 italic")
        self.seconds_entry.place(x=320,y=136)

         #Inserting the place_holders in Entry Widgets
        self.hours_entry.insert(0,00)
        self.minutes_entry.insert(0,00)
        self.seconds_entry.insert(0,00)

        #Remove place_holders from entry widget when user click on it

        def hours_click(event):
            self.hours_entry.delete(0,"end")

        def minutes_click(event):
            self.minutes_entry.delete(0,"end")

        def seconds_click(event):
            self.seconds_entry.delete(0,"end")

        #Calling the Events when user click on Entry widgets

        self.hours_entry.bind("<1>",hours_click)
        self.minutes_entry.bind("<1>",minutes_click)
        self.seconds_entry.bind("<1>",seconds_click)

        #Tkinter Set Buttion
        #Set Time Button
        #When the user press this button, Reset and Start Buttons will appear

        set_button=Button(self.window,text="Set",bg="Blue",
                          fg="White",width=5,bd=5,relief=GROOVE,
                          font=("Arial",12,"bold"),command=self.Set)
        set_button.place(x=150,y=200)

        #Exit Button
        #When the user press this button, Then window will Terminate

        exit_button=Button(self.window,text="Exit",bg="Red",fg="Black",
                           width=6,bd=4,relief=RIDGE,font=("Arial",12,"bold"),
                           command=self.Exit)
        exit_button.place(x=160,y=420)

         #Definig the Set function for assigning time

    def Set(self):
        
        #self.user_input_errors_frame=Frame(self.window,bg="black").pack()
        
        self.user_input_error_label=Label(self.window,
                                          bg="black",
                                         fg="darkred",font=("Times",14))
        self.user_input_error_label.place(x=80,y=165)

        try:
            Time=dt(self.hours.get(),self.minutes.get(),self.seconds.get())
            hours=Time.hour
            minutes=Time.minute
            seconds=Time.second
            self.total_seconds=hours*3600+minutes*60+seconds
        except Exception as ex:
            error=ex
            self.value_error_label=Label(self.window,
                                     bg="black",text=error,
                                    fg="darkred",font=("Times",14))
            self.value_error_label.place(x=40,y=165)
            #self.value_error_label.after(5000,self.value_error_label.destroy)
            self.reset_button=Button(self.window,text="Reset",
                            width=7,bd=5,relief=GROOVE,
                                 font=("Arial",12,"bold")
                                 ,command=self.Reset)
            self.reset_button.place(x=140,y=200)
            pass
        
        try:
            if hours==0 and minutes==0 and seconds==0:
                self.user_input_error_label.configure(text="Please enter valid time to set timer")
                self.reset_button=Button(self.window,text="Reset",
                            width=7,bd=5,relief=GROOVE,
                                    font=("Arial",12,"bold")
                                    ,command=self.Reset)
                self.reset_button.place(x=140,y=200)

            else:
                #Start Button for start Countdown
                self.start_button=Button(self.window,text="Start",bg="Green",
                                    fg="White",bd=3,width=8,relief=SUNKEN,
                                    font=("Arial",12,"bold"),command=self.Run)
                self.start_button.place(x=30,y=250)

                #Pause Button
                #it pauses the running timer
                self.pause_button=Button(self.window,text="Pause",bg="#DAD414",
                                bd=3,width=8,relief=SUNKEN,
                                font=("Arial",12,"bold"),command=self.Pause_time)
                self.pause_button.place(x=270,y=250)
        except:
            pass

    #Definig the Start function to start countdown

    def Start(self):
        self.reset_button=Button(self.window,text="Reset",
                            width=7,bd=5,relief=GROOVE,
                                 font=("Arial",12,"bold")
                                 ,command=self.Reset)
        self.reset_button.place(x=140,y=200)
        self.time_frame=Frame(self.window,bg="black").place(x=130,y=340)
        self.timer_label=Label(self.time_frame,
                              bg="black",fg="#FFE054",
                               font=("Times New Roman",18,"bold italic"))
        self.timer_label.place(x=80,y=300)
        self.time_up_label=Label(self.time_frame,bg="black",
                                 fg="#EC248C",
                                 font=("Helvetica",25,"bold italic"))
        self.time_up_label.place(x=130,y=340)
        self.pause=False
        while self.total_seconds>-1:
            minute,second=divmod(self.total_seconds,60)

            hour=0
            if minute>60:
                hour,minute=divmod(minute,60)

            #Displaying the Timer
            self.timer_label.configure(text="Time Left : {:02d} : {:02d} : {:02d}"
                                       .format(hour,minute,second))
            ti.sleep(1)
            self.total_seconds-=1

            if self.pause == True:
                break
            if self.total_seconds==0:
                self.time_up_label.config(text="Time Up!...")

    #Creating a thread to run the start function
    def Threading(self):
        self.x=Thread(target=self.Start,daemon=True)
        self.x.start()

    #Creating the Pause button function
    def Pause_time(self):
        self.pause=True

        minute,second=divmod(self.total_seconds,60)
        hour = 0
        if minute > 60:
            hour,minute=divmod(minute,60)

    #It will change the start button to Resume button
    def Resume(self):
        self.start_button.config(text="Resume",bg="Orange")

    #Creating the exit button function
    def Exit(self):
        self.window.destroy()

    #Combining the two functions
    #it will return the resume button and then
    #start function will executing
    def Run(self):
        self.Resume()
        self.Threading()

    #Creating the Reset button function
    #It will clear all the running functions
    
    def Reset(self):
        try:
            #ideleting the current values entered by the user 
            self.hours_entry.delete(0,END)
            self.minutes_entry.delete(0,END)
            self.seconds_entry.delete(0,END)

            #Assigning the place_holders in entry lables again
            self.hours_entry.insert(0,"00")
            self.minutes_entry.insert(00,"00")
            self.seconds_entry.insert(0,"00")

            #Destroying the error labels
            try:
                self.user_input_error_label.destroy()
                self.value_error_label.destroy()
            except:
                pass
            self.reset_button.destroy()
            try:
                self.start_button.destroy()
                self.pause_button.destroy()
            except:
                pass
            try:
                self.timer_label.destroy()
                self.time_up_label.destroy()
            except:
                pass
            try:
                self.time_frame.destroy()
            except Exception as ex:
                print(ex)
                pass
            
        except:
            pass

window=Tk()
obj=CountDown(window)
window.mainloop()
