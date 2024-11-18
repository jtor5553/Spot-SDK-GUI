import tkinter as tk
from subprocess import call

ROBOT_IP = "192.168.80.3"


def runHelloSpot():
    call(["python", r"C:\Users\jose3\OneDrive\Desktop\Spot\spot-sdk-4.0.3\python\examples\hello_spot\hello_spot.py", 
          "192.168.80.3",
        ])
    
    
root = tk.Tk()

#Box Size
root.geometry("500x500")
root.title("Spot GUI")

#Header
label = tk.Label(root, text = "Spot Programs", font = ('Arial', 28))
label.pack(padx=0, pady=0)

#Test Button
test = tk.Button(root, text="Test", font =('arial', 16))
test.place(x= 150, y= 150, height =100, width=150)
test.config(command=runHelloSpot)



root.mainloop()