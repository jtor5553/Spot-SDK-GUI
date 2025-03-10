import tkinter as tk
import bosdyn.client
from tkinter import ttk, StringVar, messagebox
from tkinter import *
import subprocess, sys, os
from tkinter import PhotoImage
from PIL import Image, ImageTk
from bosdyn.client.lease import LeaseClient
from bosdyn.client.robot_state import RobotStateClient
from tkmacosx import Button
import atexit
import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"


#Global variables
generalPath = os.path.join("spot-sdk-4.0.3", "python", "examples")
requiredFiles = "requirements.txt"
current_process = None
IP = None

#Ensures clean shutdown of gRPC connections
def shutdown_grpc():
    bosdyn.client.util.cleanup()

atexit.register(shutdown_grpc)

#Verify robot connection
def verify_robot_connection(robot):
    try:
        robot.authenticate(os.environ['BOSDYN_CLIENT_USERNAME'], os.environ['BOSDYN_CLIENT_PASSWORD'])
        return True
    except Exception as e:
        print(f"Failed to authenticate with the robot: {e}")
        return False

#Displays the battery percentage of Spot on the top right of the GUI
def check_battery_status(root):
    global battery_label, IP
    
    username = os.environ.get('BOSDYN_CLIENT_USERNAME')
    password = os.environ.get('BOSDYN_CLIENT_PASSWORD')
    
    if not username or not password or not IP:
        battery_label.config(text="Invalid Log-In")
        root.after(60000, check_battery_status, root)  
        return

    try:
        sdk = bosdyn.client.create_standard_sdk("Battery Check")
        robot = sdk.create_robot(IP)
        if not verify_robot_connection(robot):
            battery_label.config(text="Authentication Failed")
            return
        
        state_client = robot.ensure_client(RobotStateClient.default_service_name)
        robot_state = state_client.get_robot_state()

        battery_states = robot_state.battery_states
        
        if battery_states:
            battery_percentage = battery_states[0].charge_percentage.value
            battery_label.config(text=f"Battery: {battery_percentage}%")
        else:
            battery_label.config(text="Battery info unavailable")

    except Exception as e:
        battery_label.config(text=f"Error fetching battery info: {str(e)}")
        print(f"gRPC error: {e}")

    root.after(60000, check_battery_status, root)

# Installs Requirements.txt file for estop
def installForEstop():
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, generalPath, 'estop', requiredFiles)
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")

# Installs all the requirements from the txt file
def installForALL():
    global status_label, clicked, current_process
    install = clicked.get()

    if install == "Hello Spot":
        exampleInstall = "hello_spot"
    elif install == "Visualizer":
        exampleInstall = "visualizer"
    elif install == "Directory":
        exampleInstall = "directory"
    if install in ["Get Robot State", "Get Robot Hardware", "Get Robot Metrics"]:
        exampleInstall = "get_robot_state"
    elif install in ["Get Front Left Image", "Get Front Right Image"]:
        exampleInstall = "get_image"
    elif install == "Get World Objects":
        exampleInstall = "get_world_objects"
    elif install == "Comms Test":
        exampleInstall = "comms_test"
    elif install == "Time Sync":
        exampleInstall = "time_sync"
    elif install == ["IR Enable", "IR Disable"]:
        exampleInstall = "disable_ir_emission"
    elif install == "Reset Safety Stop":
        exampleInstall = "reset_safety_stop"
    elif install == "Visualizer":
        exampleInstall = "visualizer"
    elif install == "Get Mission State":
        exampleInstall = "get_mission_state"
    elif install == "Spotlight":
        exampleInstall = "spot_light"
    elif install == "WASD":
        exampleInstall = "wasd"
    else:
        status_label.config(text="Couldn't Install Dependencies")
        return
    
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, generalPath, exampleInstall, requiredFiles)
    status_label.config(text="Looking for Program requirements")    

    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        if result.returncode == 0:
            status_label.config(text="Dependencies Installed succesfully")
        else:
            status_label.config(text ="Failed to install dependencies{result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")    

# Terminates any example with the press of the "Stop" Button
lease_client = None
lease = None

def stopProgram():
    global current_process, status_label, lease_client, lease
    if current_process:
        try:
            current_process.terminate()
            current_process.wait()  
            current_process = None
            status_label.config(text="Program Stopped")
            print("Process terminated successfully.")

            if lease_client and lease:
                lease_client.return_lease(lease)
                print("Lease returned.")
                lease = None
                lease_client = None
        except Exception as e:
            status_label.config(text=f"Error stopping process: {str(e)}")
            print(f"Error stopping process: {str(e)}")
    else:
        status_label.config(text="No program is currently running")
        print("No program is currently running")

# Starts the Estop
def startEStop():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    script_path = os.path.join(parent_directory, generalPath, 'estop', 'estop_gui.py')
        
    if os.path.exists(script_path):
        installForEstop()
        subprocess.Popen([sys.executable, script_path, IP])
        status_label.config(text="EStop started")
    else:
        status_label.config(text="E-stop not found")

# User decides what program to run from the dropdown menu
def runSelectedProgram():
    global status_label, clicked, current_process
    selected = clicked.get()

    location = None
    script = None
    state = None
    camera = None
    eOr = None

    if selected == "Hello Spot":
        location = "hello_spot"
        script = "hello_spot.py"
    elif selected == "Visualizer":
        location = "visualizer"
        script = "basic_streaming_visualizer.py"
    elif selected == "Get World Objects":
        location = "get_world_objects"
        script = "get_world_objects.py"
    elif selected == "Directory":
        location = "directory"
        script = "directory_modification.py"
    elif selected == "Get Robot State":
        location = "get_robot_state"
        script = "get_robot_state.py"
        state = 'state'
    elif selected == "Get Robot Hardware":
        location = "get_robot_state"
        script = "get_robot_state.py"
        state = 'hardware'
    elif selected == "Get Robot Metrics":
        location = "get_robot_state"
        script = "get_robot_state.py"
        state = 'metrics'
    elif selected == "Get Front Left Image":
        location = "get_image"
        script = "image_viewer.py"
        camera = "frontleft_fisheye_image"
    elif selected == "Get Front Right Image":
        location = "get_image"
        script = "image_viewer.py"
        camera = "frontright_fisheye_image"
    elif selected == "Get Mission State":
        location = "get_mission_state"
        script = "get_mission_state.py"
    elif selected == "Time Sync":
        location = "time_sync"
        script = "time_sync_client.py"
    elif selected == "Comms Test":
        location = "comms_test"
        script = "client.py"
    elif selected == "IR Enable":
        location = "disable_ir_emission"
        script = "disable_ir_emission.py"
        eOr = "--enable"
    elif selected == "IR Disable":
        location = "disable_ir_emission"
        script = "disable_ir_emission.py"
        eOr = "--disable"
    elif selected == "Reset Safety Stop":
        location = "reset_safety_stop"
        script = "reset_primary_safety_stop.py"
    elif selected == "Spotlight":
        location ="spot_light"
        script ="spot_light.py"
    elif selected == "WASD":
        location ="wasd"
        script = "wasd.py"
    else:
        status_label.config(text="Couldn't Find Example")
        return
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    script_path = os.path.join(parent_directory, generalPath, location, script)
    
    print(f"Selected: {selected}, Script Path: {script_path}")  

    if location != "NULL" and script != "NULL":
        installForALL()  

        if location == "get_robot_state" and state != None :
                try:
                    current_process = subprocess.Popen([sys.executable, script_path, IP, state])
                    status_label.config(text=f"Running {selected}...")
                except FileNotFoundError:
                    messagebox.showerror("Error", "Python executable not found.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to execute the script: {str(e)}")
        if location == "get_image" and camera != None:
                try:
                    current_process = subprocess.Popen([sys.executable, script_path, IP, "--image-sources", camera])
                    status_label.config(text=f"Running {selected}...")
                except FileNotFoundError:
                    messagebox.showerror("Error", "Python executable not found.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to execute the script: {str(e)}")
        if location == "disable_ir_emission" and eOr != None:
                try:
                    current_process = subprocess.Popen([sys.executable, script_path, IP, eOr])
                    status_label.config(text=f"Running {selected}...")
                    print(f"Current Process: {current_process}")
                except FileNotFoundError:
                    messagebox.showerror("Error", "Python executable not found.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to execute the script: {str(e)}")
        else:
            try:
                current_process = subprocess.Popen([sys.executable, script_path, IP])
                status_label.config(text=f"Running {selected}...")
            except FileNotFoundError:
                messagebox.showerror("Error", "Python executable not found.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to execute the script: {str(e)}")
    else:
        messagebox.showerror("Error", "Script not found.")

#Text display for every function
def selectedEvent(event):
    canvas.delete("label_text")
    canvas.delete("text_box")

    selected_option = clicked.get()

    box_x1, box_y1 = 10, 175  
    box_x2, box_y2 = 300, 300  

    canvas.create_rectangle(box_x1, box_y1, box_x2, box_y2, fill="white", outline="black", tags="text_box")

    if selected_option == 'Hello Spot':
        canvas.create_text(153, 225, text="  Spot will stand up, strike a\npose, stand tall, sit down, and\ncapture an image from a\ncamera", fill="black", font=("Arial", 16), tags="label_text")
    elif selected_option == 'Directory':
        canvas.create_text(155, 225, text="  This example demonstrates how\nto use Spot’s Directory Client to\nlist, register, update, and remove\ninformation about API services.", fill="black", font =("Arial", 14), tags="label_text")
    elif selected_option in ["Get Robot State", "Get Robot Hardware", "Get Robot Metrics"]:
        canvas.create_text(155, 225, text="  Demonstrates how to query the\nrobot state service for the\nhardware config, the current robot\nstate, or the robot metrics.", fill="black", font=("Arial", 14), tags="label_text")
    elif selected_option in ["Get Front Left Image", "Get Front Right Image"]:
        canvas.create_text(155, 225, text="  Can be used to create popup\nwindows which show a live preview\nof the image sources specified.", fill="black", font=("Arial", 13), tags="label_text")
    elif selected_option in ["Get Fron", "Get Front Left Image", "Get Front Right Image"]:
        canvas.create_text(155, 225, text="  Can be used to create popup\nwindows which show a live preview\nof the image sources specified.", fill="black", font=("Arial", 13), tags="label_text")
    else:
        canvas.create_text(115, 200, text="No Description found.", fill="black", font=("Arial", 16), tags="label_text")

#Main GUI
def mainInterface():
    global status_label, battery_label, clicked, current_process, canvas, IP
    root = tk.Tk()

    root.geometry("500x500")
    root.title("Spot GUI")

    current_directory = os.path.dirname(os.path.abspath(__file__))
    bg_image_path = os.path.join(current_directory, "Spot_GUI_Background.png")  

    original_image = Image.open(bg_image_path)
    resized_image = original_image.resize((500, 500))
    bg_image = ImageTk.PhotoImage(resized_image)

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(250, 30, text="Spot Programs", font=('Arial', 28), fill="white")

    options = [
        "Hello Spot",
        "Directory",
        "Get Robot State",
        "Get Robot Hardware",
        "Get Robot Metrics",
        "Get Front Left Image",
        "Get Front Right Image",
        "Get World Objects",
        "Get Mission State",
        "Time Sync",
        "Comms Test",
        "IR Enable",
        "IR Disable",
        "Reset Safety Stop",
        "Spotlight",
        "WASD"
    ]

    clicked = StringVar()
    clicked.set(options[0])
    programs = tk.OptionMenu(root, clicked, *options, command= selectedEvent)
    programs_window = canvas.create_window(150, 130, width=225, height=60, window=programs)

    run = tk.Button(root, text="Run", font=('arial', 16), command=runSelectedProgram, bg='#050505', fg='#2dcc67')
    canvas.create_window(400, 150, width=150, height=100, window=run)

    stop = tk.Button(root, text="Stop Program", font=('arial', 16), command=stopProgram, bg="#050505",fg='#cc622d')
    canvas.create_window(400, 400, width=150, height=100, window=stop)

    eStop = tk.Button(root, text="Start EStop", font=('arial', 16), command=startEStop, background='#b81d1d')
    canvas.create_window(400, 275, width=150, height=100, window=eStop)

    status_label = tk.Label(root, text="", font=('Arial', 12), fg="blue", background="white")
    canvas.create_window(250, 75, window=status_label)
    
    battery_label = tk.Label(root, text="", font=('Arial', 12), fg="red", background="white")
    canvas.create_window(435, 35, window=battery_label)

    #Adds login fields to the main GUI 
    username_label = tk.Label(root, text="Username:")
    username_label.place(x=10, y=400)
    username_entry = tk.Entry(root)
    username_entry.place(x=80, y=400)

    password_label = tk.Label(root, text="Password:")
    password_label.place(x=10, y=430)
    password_entry = tk.Entry(root)
    password_entry.place(x=80, y=430)

    ip_label = tk.Label(root, text="IP Address:")
    ip_label.place(x=10, y=460)
    ip_entry = tk.Entry(root)
    ip_entry.place(x=80, y=460)

    login_button = tk.Button(root, text="Login", command=lambda: on_login(username_entry, password_entry, ip_entry, username_label, password_label, ip_label, login_button))
    login_button.place(x=220, y=430)

    def on_login(username_entry, password_entry, ip_entry, username_label, password_label, ip_label, login_button):
        username = username_entry.get()
        password = password_entry.get()
        ip = ip_entry.get()

        if not username or not password or not ip:
            messagebox.showerror("Input Error", "All fields must be filled out!")
            return

        os.environ['BOSDYN_CLIENT_USERNAME'] = username
        os.environ['BOSDYN_CLIENT_PASSWORD'] = password

        global IP
        IP = ip  

        print(f"Username: {username}, Password: {password}, IP: {ip}")

        username_label.place_forget()
        username_entry.place_forget()
        password_label.place_forget()
        password_entry.place_forget()
        ip_label.place_forget()
        ip_entry.place_forget()
        login_button.place_forget()

        #Starts checking battery status after login
        check_battery_status(root)

    root.mainloop()

if __name__ == "__main__":
    mainInterface()