import tkinter as tk
from tkinter import *
import os
import subprocess

ROBOT_IP = "192.168.80.3"



def runHelloSpot():

    os.environ['BOSDYN_CLIENT_USERNAME'] = 'user2' 
    os.environ['BOSDYN_CLIENT_PASSWORD'] = 'simplepassword'

    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'hello_spot', 'hello_spot.py')

    subprocess.Popen(["python", script_path, "192.168.80.3"])    

root = tk.Tk()

# Box Size and Title
root.geometry("500x500")
root.title("Spot GUI")

# Header
label = tk.Label(root, text="Spot Programs", font=('Arial', 28))
label.pack(padx=0, pady=0)

# Test Button
test = tk.Button(root, text="Test", font=('arial', 16))
test.place(x=150, y=150, height=100, width=150)
test.config(command=runHelloSpot)

root.mainloop()
