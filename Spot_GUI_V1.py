import tkinter as tk
from tkinter import ttk, StringVar, messagebox
from tkinter import *
import subprocess, subprocess, sys, os
from tkinter import PhotoImage
from PIL import Image, ImageTk
from bosdyn.client.lease import LeaseClient



generalPath = os.path.join("spot-sdk-4.0.3", "python", "examples")
requiredFiles = "requirements.txt"
current_process = None


#Installs Requirements.txt file for estop
def installForEstop():

    current_directory = os.path.dirname(os.path.abspath(__file__))  
    parent_directory = os.path.dirname(current_directory)  
    
    requirements_path = os.path.join(parent_directory, generalPath, 'estop', requiredFiles)
    print(f"Looking for requirements.txt at: {requirements_path}")
    
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")

        # Install dependencies
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            print("installed successfully.")
        else:
            print(f"Error during installation: {result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")


#Insalls all the requirements from the txt file
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
    elif install in ["Get Front Left Image", "Get Front Left Image", "Get Front Right Image"]:
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
        # Run the pip install command
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)
        
        # Check if the installation was successful
        if result.returncode == 0:
            status_label.config(text="Dependencies Installed succesfully")
        else:
            status_label.config(text ="Failed to install dependencies{result.stderr}")
    else:
        print(f"Error: requirements.txt not found at {requirements_path}")    

#Terminates any example
lease_client = None
lease = None

def stopProgram():
    global current_process, status_label, lease_client, lease
    if current_process:
        try:
            current_process.terminate()
            current_process.wait()  # Wait for the process to terminate
            current_process = None
            status_label.config(text="Program Stopped")
            print("Process terminated successfully.")

            # Releases the lease after stopping the process
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

#Starts the Estop
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


#User decides what program to run from the dropdown menu
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

#Username and passowrd input for spot
def run_with_inputs(username, password, ip):
    if not username or not password or not ip:
        messagebox.showerror("Input Error", "All fields must be filled out!")
        return

    os.environ['BOSDYN_CLIENT_USERNAME'] = username
    os.environ['BOSDYN_CLIENT_PASSWORD'] = password

    global IP
    IP = ip  

    #Prints values to verify inputs
    print(f"Username: {username}, Password: {password}, IP: {ip}")

    #Closes the login window and opens the main interface
    login_window.destroy()  
    mainInterface()

#Text display for every function
def selectedEvent(event):
    canvas.delete("label_text")
    canvas.delete("text_box")

    selected_option = clicked.get()

    box_x1, box_y1 = 10, 175  # Top-left coordinates
    box_x2, box_y2 = 300, 300  # Bottom-right coordinates

    canvas.create_rectangle(box_x1, box_y1, box_x2, box_y2, fill="white", outline="black", tags="text_box")

    # Display appropriate text over the white box
    if selected_option == 'Hello Spot':
        canvas.create_text(153, 225, text="  Spot will stand up, strike a\npose, stand tall, sit down, and\ncapture an image from a\ncamera", fill="black", font=("Arial", 16), tags="label_text")
    elif selected_option == 'Directory':
        canvas.create_text(155, 225, text="  This example demonstrates how\nto use Spot’s Directory Client to\nlist, register, update, and remove\ninformation about API services.", fill="black", font =("Arial", 14), tags="label_text")
    elif selected_option in ["Get Robot State", "Get Robot Hardware", "Get Robot Metrics"]:
        canvas.create_text(155, 225, text="  Demonstrates how to query the\nrobot state service for the\nhardware config, the current robot\nstate, or the robot metrics.", fill="black", font=("Arial", 14), tags="label_text")
    elif selected_option in ["Get Front Left Image", "Get Front Left Image", "Get Front Right Image"]:
        canvas.create_text(155, 225, text="  Can be used to create popup\nwindows which show a live preview\nof the image sources specified.", fill="black", font=("Arial", 13), tags="label_text")
    elif selected_option == "Get World Objects":
        canvas.create_text(155, 235, text=" Demonstrates how to use the world\n object service to list the objects\n Spot can detect, and filter\nthese lists for specific objects\nor objects after a certain time stamp. ", fill="black", font=("Arial", 13), tags="label_text")
    elif selected_option in ["Get Fron", "Get Front Left Image", "Get Front Right Image"]:
        canvas.create_text(155, 225, text="  Can be used to create popup\nwindows which show a live preview\nof the image sources specified.", fill="black", font=("Arial", 13), tags="label_text")
    elif selected_option == 'Get Mission State':
        canvas.create_text(153, 225, text="  Demonstrates how to retrieve\ninformation about the state of the\ncurrently-running mission.", fill="black", font=("Arial", 14), tags="label_text")
    elif selected_option == 'Time Sync':
        canvas.create_text(160, 225, text=" Demonstrates how to use the timesync service\nto establish time sync between your computer\nand the robot’s clock. Specifically, it creates\na TimeSyncEndpoint, which can be used to\nestablish timesync as well as determine the\nclockskew or round trip time.", fill="black", font=("Arial", 10), tags="label_text")
    elif selected_option == 'Comms Test':
        canvas.create_text(155, 215, text="  Demonstrates how to use the SDK to\nperform comms testing. This is meant to\nbe run on a CORE I/O during an\nAutowalk mission.", fill="black", font=("Arial", 11), tags="label_text")
    elif selected_option in ["IR Enable", "IR Disable"]:
        canvas.create_text(158, 225, text="  Demonstrates how to use the\nIREnableDisableServiceClient to\nenable/disable the robot’s IR light\nemitters in the body and hand sensors.", fill="black", font=("Arial", 12), tags="label_text")
    elif selected_option == 'Reset Safety Stop':
        canvas.create_text(160, 225, text=" Resets the primary and redundant\nsafety stops on a robot configured\nfor Safety-Related Stopping\nFunction (SRSF)", fill="black", font=("Arial", 12), tags="label_text")
    elif selected_option == 'Spotlight':
        canvas.create_text(153, 225, text="  Will allow Spot to respond to a light\nshining in its front left camera", fill="black", font=("Arial", 12), tags="label_text")
    elif selected_option == 'Visualizer':
        canvas.create_text(153, 225, text=" Visualizes Spot’s perception scene\nin a consistent coordinate frame.\nIt demonstrates:", fill="black", font=("Arial", 12), tags="label_text")
    elif selected_option == 'WASD':
        canvas.create_text(153, 225, text=" Creates an interface for operating\nSpot with your keyboard", fill="black", font=("Arial", 12), tags="label_text")
    else:
        canvas.create_text(145, 200, text="No Description found.", fill="black", font=("Arial", 16), tags="label_text")


#Main
def mainInterface():
    global status_label, clicked, current_process, canvas
    root = tk.Tk()

    #GUI Size
    root.geometry("500x500")
    root.title("Spot GUI")

    #Loads the background image
    current_directory = os.path.dirname(os.path.abspath(__file__))
    bg_image_path = os.path.join(current_directory, "Spot_GUI_Background.png")  

    original_image = Image.open(bg_image_path)
    resized_image = original_image.resize((500, 500))
    bg_image = ImageTk.PhotoImage(resized_image)

    #Creates a canvas for the background image
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack(fill="both", expand=True)

    #Sets the background image on the canvas
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Add header on the canvas
    canvas.create_text(250, 30, text="Spot Programs", font=('Arial', 28), fill="white")

    # Options for Dropdown
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
        "Visualizer",
        "Spotlight",
        "WASD"
    ]

    # Programs Dropdown Menu
    clicked = StringVar()
    clicked.set(options[0])
    programs = tk.OptionMenu(root, clicked, *options, command= selectedEvent)
    programs_window = canvas.create_window(150, 130, width=225, height=60, window=programs)

    # Run Button
    run = tk.Button(root, text="Run", font=('arial', 16), command=runSelectedProgram, background='#2dcc67')
    canvas.create_window(400, 150, width=150, height=100, window=run)

    # Stop Button
    stop = tk.Button(root, text="Stop Program", font=('arial', 16), command=stopProgram, background='#cc622d')
    canvas.create_window(400, 400, width=150, height=100, window=stop)

    # Start EStop Button
    eStop = tk.Button(root, text="Start EStop", font=('arial', 16), command=startEStop, background='#b81d1d')
    canvas.create_window(400, 275, width=150, height=100, window=eStop)

    # Current status of program label
    status_label = tk.Label(root, text="", font=('Arial', 12), fg="blue", background="white")
    canvas.create_window(250, 75, window=status_label)

    root.mainloop()



# Create the login window
def createLoginWindow():
    global login_window
    login_window = tk.Tk()

    login_window.geometry("400x300")
    login_window.title("Login Window")

    tk.Label(login_window, text="Username:").pack(pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:").pack(pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    tk.Label(login_window, text="IP Address:").pack(pady=10)
    ip_entry = tk.Entry(login_window)
    ip_entry.pack(pady=5)

    def on_login():
        username = username_entry.get()
        password = password_entry.get()
        ip = ip_entry.get()
        run_with_inputs(username, password, ip)

    # Login button
    login_button = tk.Button(login_window, text="Login", command=on_login)
    login_button.pack(pady=20)

    login_window.mainloop()

# Start with login window
createLoginWindow()


