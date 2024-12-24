"# Spot-GUI" 

#Current Features:

"""
Login Window:
Captures username, password, and IP address.
Sets environment variables for Spot's API.

Main Interface:
A dropdown menu for selecting Spot sdks examples like "Hello Spot", "Visualizer", etc.
Buttons to:
Start the selected program.
Stop the running program.
Start Spot's emergency stop (EStop).

Dynamic Installation of Dependencies:
Installs dependencies from a requirements.txt file for the selected program.

Program Execution:
Uses subprocess.Popen to execute selected scripts.
Options for passing specific arguments like camera sources or state types.

Error Handling:
Validates input fields in the login window.
Checks if required scripts and dependencies exist.
Displays error messages if scripts or Python executables are not found.

"""
