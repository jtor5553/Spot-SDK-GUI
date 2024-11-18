import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import subprocess
from subprocess import call
from bosdyn.client import create_standard_sdk


ROBOT_IP = "192.168.80.3"
TOKEN_PATH = r"C:\Users\jose3\OneDrive\Desktop\Spot\GUI\spot_token.json"
USERNAME = "user2"
PASSWORD = "simplepassword"


#Generates token so user can be logged in
def generate_token():
    sdk = create_standard_sdk("Spot GUI")
    robot = sdk.create_robot(ROBOT_IP)

    robot.authenticate(USERNAME, PASSWORD)
        
    with open(TOKEN_PATH, "w") as token_file:
         token_file.write(robot.auth.token)  

#Authenticates the token 
def authenticate_with_token():
    sdk = create_standard_sdk("Spot GUI")
    robot = sdk.create_robot(ROBOT_IP)

    with open(TOKEN_PATH, "r") as token_file:
        token = token_file.read().strip()
        
    robot.authenticate_with_token(token)
    return robot

#Starts the Estop in a different terminal
def startEStop():
    subprocess.Popen(["start", "cmd", "/k", "python", r"C:\Users\jose3\OneDrive\Desktop\Spot\spot-sdk-4.0.3\python\examples\estop\estop_gui.py", "192.168.80.3"], shell=True )
    status_label.config(text="EStop started")


#User decides what program to run from the dropdown menu
def runSelectedProgram():
    
    selected = clicked.get()
    
    if selected == "Hello Spot": #Hello Spot
        call(["python", r"C:\Users\jose3\OneDrive\Desktop\Spot\spot-sdk-4.0.3\python\examples\hello_spot\hello_spot.py", "192.168.80.3"])
        status_label.config(text="Hello Spot program is running...")
    elif selected == "Get Image": #Get Image
        status_label.config(text="Not Ready")
        pass
    elif selected == "Get World Objects": #World Objects
        status_label.config(text="Not Ready Either")        
        pass

root = tk.Tk()

#Robot logging in
if not os.path.exists(TOKEN_PATH):
    generate_token()
    robot = authenticate_with_token()

#Box Size
root.geometry("500x500")
root.title("Spot GUI")

#Header
label = tk.Label(root, text = "Spot Programs", font = ('Arial', 28))
label.pack(padx=0, pady=0)

#Options for Dropdown
options = [
    "Hello Spot",
    "Get Image",
    "Get World Objects"
]

#Programs Dropdown Menu
clicked = StringVar()
clicked.set(options[0])
programs = tk.OptionMenu(root, clicked, *options)
programs.pack()
programs.place(x = 50, y = 100, height = 60, width=225)

#Run Button
run = tk.Button(root, text="Run", font =('arial', 16))
run.place(x= 300, y= 100, height =100, width=150)
run.config(background='#2dcc67')
run.config(command=runSelectedProgram)

#Stop Button
stop = tk.Button(root, text="Stop Program", font =('arial', 16))
stop.place(x= 300, y= 350, height = 100, width=150)
stop.config(background='#cc622d')

#Start Estop Button          
eStop = tk.Button(root, text="Start EStop", font =('arial', 16))
eStop.place(x= 300, y= 225, height = 100, width=150)
eStop.config(background='#b81d1d')
eStop.config(command=startEStop)

#Current status of program label
status_label = tk.Label(root, text="", font=('Arial', 12), fg="blue")
status_label.pack(pady=20)
root.mainloop()