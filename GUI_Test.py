import tkinter as tk
from tkinter import ttk, StringVar, messagebox
from tkinter import *
import os
import subprocess
import sys

USERNAME = "user2"
PASSWORD = "simplepassword"

os.environ['BOSDYN_CLIENT_USERNAME'] = 'user2' 
os.environ['BOSDYN_CLIENT_PASSWORD'] = 'simplepassword'



current_process = None

#Installs Requirements.txt file for programs
def installForEstop():


    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'estop', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForHelloSpot():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'hello_spot', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")       
def installForDirectory():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'directory', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForVisualizer():
    # Get the absolute path to the parent directory
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'visualizer', 'requirements.txt')  
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForGetRobotState():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'get_robot_state', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForGetImage():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'get_image', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForGetWorldObjects():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'get_world_objects', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForGetMissionState():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'get_mission_state', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForTimeSync():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'time_sync', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForCommsTest():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'comms_test', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForIREnableDisable():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'disable_ir_emission', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")
def installForResetSafetyStop():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'reset_safety_stop', 'requirements.txt')
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")

def stopProgram():
    global current_process, status_label
    if current_process:
        current_process.terminate()
        current_process = None
        status_label.config(text="Program Stopped")
    else:
        status_label.config(text="No program is currently running")
# Starts the Estop in a different terminal
def startEStop():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'estop', 'estop_gui.py')
        
    if os.path.exists(script_path):
        installForEstop()

        subprocess.Popen([ "cmd", "/k", "python", script_path, "192.168.80.3"])
        status_label.config(text="EStop started")
# User decides what program to run from the dropdown menu
def runSelectedProgram():
    global status_label, clicked, current_process
    selected = clicked.get()
    
    if selected == "Hello Spot":
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'hello_spot', 'hello_spot.py')
        
        if os.path.exists(script_path):
            installForHelloSpot()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Hello Spot program is running...")
        else:
            status_label.config(text="Error: 'hello_spot.py' not found")

    elif selected == "Visualizer":  # Get Image
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'visualizer', 'basic_streaming_visualizer.py')
        
        if os.path.exists(script_path):
            installForVisualizer()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Visualizer is running...")
        else:
            status_label.config(text="Error: 'visualizer.py' not found")
    
    elif selected == "Get World Objects":  # World Objects
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'get_world_objects', 'get_world_objects.py')

        if os.path.exists(script_path):
            installForGetWorldObjects()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Get World Objects is running...")
        else:
            status_label.config(text="Error: 'get_world_objects.py' not found")
    elif selected == "Directory": 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'directory', 'directory_modification.py')

        if os.path.exists(script_path):
            installForDirectory()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Directory program is running...")
        else:
            status_label.config(text="Error: 'directory_modification.py' not found")
    elif selected == "Get Robot State":
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'get_robot_state', 'get_robot_state.py')

        if os.path.exists(script_path):
            installForGetRobotState()

            state = state_var.get() 
            current_process = subprocess.Popen(["python", script_path, "192.168.80.3", state]) 
            status_label.config(text=f"Getting Robot State: {state}")
        else:
            status_label.config(text="Error: 'get_robot_state.py' not found") 
    elif selected == "Get Image": 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'get_image', 'get_image.py')

        if os.path.exists(script_path):
            installForGetImage()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="GetImage program running...")
        else:
            status_label.config(text="Error: 'get_image.py' not found")
    elif selected == "Get Mission State": 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'get_mission_state', 'get_mission_state.py')

        if os.path.exists(script_path):
            installForGetMissionState()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Get Mission State program is running...")
        else:
            status_label.config(text="Error: 'get_mission_state.py' not found")
    elif selected == "Time Sync": 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'time_sync', 'time_sync_client.py')

        if os.path.exists(script_path):
            installForTimeSync()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Time Synce is running...")
        else:
            status_label.config(text="Error: 'time_sync_client.py' not found")
    elif selected == "Comms Test": 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'comms_test', 'client.py')

        if os.path.exists(script_path):
            installForCommsTest()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Comms Test is running...")
        else:
            status_label.config(text="Error: 'client.py' not found")
    elif selected == "IR Enable/Disable": 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'disable_ir_emission', 'disable_ir_emission.py')

        if os.path.exists(script_path):
            installForIREnableDisable()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="IR is running...")
        else:
            status_label.config(text="Error: 'disable_ir_emission.py' not found")
    elif selected == "Reset Safety Stop": 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        script_path = os.path.join(parent_directory, 'spot-sdk-4.0.3', 'python', 'examples', 'reset_safety_stop', 'reset_primary_safety_stop.py')

        if os.path.exists(script_path):
            installForResetSafetyStop()

            current_process = subprocess.Popen(["python", script_path, "192.168.80.3"])
            status_label.config(text="Reseting Safety Stop...")
        else:
            status_label.config(text="Error: 'reset_safety_stop.py' not found")
# Log in barrier
def login():
    enteredUser = usernameEntry.get()
    enteredPassword = passwordEntry.get()

    if enteredUser == USERNAME and enteredPassword == PASSWORD:
        loginWindow.destroy()
        mainInterface()
    else:           
        messagebox.showerror("login failed", "Invalid User or Password.")            

#Main
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
        "Directory",
        "Get Robot State",
        "Get Image",
        "Get World Objects",
        "Get Mission state",
        "Time Sync",
        "Comms Test",
        "IR Enable/Disable",
        "Reset Safety Stop",
        "Visualizer"
    ]

    # Programs Dropdown Menu
    clicked = StringVar()
    clicked.set(options[0])
    programs = tk.OptionMenu(root, clicked, *options)
    programs.pack()
    programs.place(x=50, y=100, height=60, width=225)

    state_var = StringVar() 
    state_dropdown = ttk.Combobox(root, textvariable=state_var) 
    state_dropdown['values'] = ("state", "hardware", "metrics") 
    state_dropdown.set("Select State") 
    state_dropdown.place(x=50, y=200)
    
    # Run Button
    run = tk.Button(root, text="Run", font=('arial', 16))
    run.place(x=300, y=100, height=100, width=150)
    run.config(background='#2dcc67')
    run.config(command=runSelectedProgram)

    # Stop Button
    stop = tk.Button(root, text="Stop Program", font=('arial', 16))
    stop.place(x=300, y=350, height=100, width=150)
    stop.config(command= stopProgram)
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

#log in Window
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

