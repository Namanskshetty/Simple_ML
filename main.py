import sklearn 
import numpy as np
import matplotlib.pyplot as plt
import subprocess
failed_command = subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
if failed_command.returncode == 0:
  x=list(range(0,10)) # C creates the list of data between 0-9
  y=[1.8*F+32 for F in x] # F converts the c to f using above generated data
  #y=mx+c
  #F=1.8*C+32
  print("X:",x)
  print("X:",y)

  plt.plot(x,y,"-*r") # plots the graph for the x and y "-" defines the line * defines the point and r represents the color.
  plt.show() # This shows the plotted graph
else:
  print("Could not install the packages")
