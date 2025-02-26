# Spot SDK GUI Version 1.30, 2/26/2025

**Overview**
This is a graphical user interface (GUI) built to control Spot, Boston Dynamics' robotic dog. This GUI makes it easier to run the examples from the Spot-SDK. With one click of a button, you can run the examples. It installs the dependencies for you and doesn't require a username or password except when booting. It will also display battery life on the top right so users stay informed. 

**Table of Contents**
*Overview*
*Installation*
*Features*
*How to Use GUI*

**Installation**
*Prerequisites*
Ensure you have Python 3.6-3.10 and PIP installed. If you do not have Python installed, you can download and install it from the official Python website.

**MAKE SURE THAT SPOT_GUI AND SPOT_SDK ARE IN A DIRECTORY TOGETHER. BEST WAY TO DO THIS IS BY DOWNLOADING THERE FOLDER INTO A FOLDER TOGETHER**---IMPORTANT

***INSTALL SPOT_SDK at https://dev.bostondynamics.com/docs/python/quickstart#system-requirements***

**Additional Packages**
***pip**, instrctions above.
**Pillow**, To install Python Pillow on Windows and Mac, open your command prompt, and type "pip install Pillow" - this will use the package installer (pip) included with Python to download and install the Pillow library directly onto your system. 


**Features**
*Battery Monitoring*: View the current battery level of Spot in real time.
*Program Execution*: Run a variety of predefined programs on Spot.
*EStop*: Manually initiate an emergency stop to halt Spot's operations.

**Programs Available**
""""
Hello Spot
Directory Client
Get Robot State
Get Robot Hardware
Get Robot Metrics
Get Front Left Image
Get Front Right Image
Get Mission State
Time Sync
Comms Test
IR Enable/Disable
Reset Safety Stop
Spotlight
WASD
""""

**How to Use GUI**
*Login*: When you start the program you will be prompted to input your Spot credentials (username, password, and IP address).
If they are not correct nothing will work on the GUI and you will get errors.

*E-STOP*: You must start an E-STOP before you try to run any programs. If it is not started you will get an error.

*Select Program*: To choose an example from the dropdown menu simply click on the dropdown menu and you will be given several options to pick from. Under the dropdown menu, there will be a box that explains what each example will do.

*Run Program*: Click on the "Run" button to start the selected program. The status label will update to show the current running program.

*Stop Program*: If you wish to stop a running program or you run into any problems, simply click the "Stop Program" button.

*Battery Status*: The battery status of Spot will be displayed on the top right corner of the GUI. If it is not there was either an error with the credentials or connecting to Spot.



AUTHOR: Jose Torres-Gomez
Email: jgtmpd@umsystem.edu
Linkdin: www.linkedin.com/in/jose-torres-gomez-807b14258

LAB: Autonomous Systems Lab
Director: Kristofferson Culmer, culmerk@missouri.edu
Purpose:This is Jose's first project for the Autonomous Systems Lab it makes it easier for users to run Spot-SDK examples.
