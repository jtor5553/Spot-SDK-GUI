import tkinter as tk
from tkinter import ttk, StringVar, messagebox
from tkinter import *
import os
import subprocess
from subprocess import call
import sys

USERNAME = "user2"
PASSWORD = "simplepassword"

#install R for Visualizer
def installForVisualizer():
    # Get the absolute path to the parent directory
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Gets current directory of the script
    parent_directory = os.path.dirname(current_directory)  # Goes up one level to the parent directory
    
    # Now construct the full path to the 'requirements.txt' file
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'visualizer', 'requirements.txt')
    
    # Print the path to verify it
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("Dependencies installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")

# Starts the Estop in a different terminal
def startEStop():
    subprocess.Popen(["start", "cmd", "/k", "python", r"C:\Users\jose3\OneDrive\Desktop\Spot\spot-sdk-4.0.3\python\examples\estop\estop_gui.py", "192.168.80.3"], shell=True)
    status_label.config(text="EStop started")

# User decides what program to run from the dropdown menu
def runSelectedProgram():
    global status_label, clicked 
    selected = clicked.get()
    
    if selected == "Hello Spot":
        # Provide the credentials as arguments to hello_spot.py
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'hello_spot', 'hello_spot.py')
        
        if os.path.exists(script_path):
            subprocess.Popen(["python", script_path, "192.168.80.3", "user2", "simplepassword"])
            status_label.config(text="Hello Spot program is running...")
        else:
            status_label.config(text="Error: 'hello_spot.py' not found")
            
    elif selected == "Get Image":  # Get Image
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'visualizer', 'basic_streaming_visualizer.py')
        
        if os.path.exists(script_path):
            installForVisualizer()

            subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Get Image program is running...")
        else:
            status_label.config(text="Error: 'get_image.py' not found")
    
    elif selected == "Get World Objects":  # World Objects
        status_label.config(text="Not Ready Either")
def login():
    enteredUser = usernameEntry.get()
    enteredPassword = passwordEntry.get()

    if enteredUser == USERNAME and enteredPassword == PASSWORD:
        loginWindow.destroy()
        mainInterface()
    else:           
        messagebox.showerror("login failed", "Invalid User or Password.")            

def mainInterface():
    global status_label, clicked
    root = tk.Tk()

# Box Size
    root.geometry("500x500")
    root.title("Spot GUI")

# Header
    label = tk.Label(root, text="Spot Programs", font=('Arial', 28))
    label.pack(padx=0, pady=0)

# Options for Dropdown
    options = [
        "Hello Spot",
        "Get Image",
        "Get World Objects"
    ]

    # Programs Dropdown Menu
    clicked = StringVar()
    clicked.set(options[0])
    programs = tk.OptionMenu(root, clicked, *options)
    programs.pack()
    programs.place(x=50, y=100, height=60, width=225)

    # Run Button
    run = tk.Button(root, text="Run", font=('arial', 16))
    run.place(x=300, y=100, height=100, width=150)
    run.config(background='#2dcc67')
    run.config(command=runSelectedProgram)

    # Stop Button
    stop = tk.Button(root, text="Stop Program", font=('arial', 16))
    stop.place(x=300, y=350, height=100, width=150)
    stop.config(background='#cc622d')

    # Start Estop Button          
    eStop = tk.Button(root, text="Start EStop", font=('arial', 16))
    eStop.place(x=300, y=225, height=100, width=150)
    eStop.config(background='#b81d1d')
    eStop.config(command=startEStop)

    # Current status of program label
    status_label = tk.Label(root, text="", font=('Arial', 12), fg="blue")
    status_label.pack(pady=20)

    root.mainloop()

    #login Window
loginWindow = tk.Tk()
loginWindow.geometry("300x200")
loginWindow.title("login")

        #Username Box
username = tk.Label(loginWindow, text = "Username")
username.pack(pady = 5)
usernameEntry = tk.Entry(loginWindow)
usernameEntry.pack(pady = 5)

    #Password Box
password = tk.Label(loginWindow, text = "Password")
password.pack(pady = 5)
passwordEntry = tk.Entry(loginWindow, show = "*")
passwordEntry.pack(pady = 5)
loginButton = tk.Button(loginWindow, text = "Login", command = login)
loginButton.pack(pady = 20)
loginWindow.mainloop()

