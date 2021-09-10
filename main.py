import sklearn 
import numpy as np
import matplotlib.pyplot as plt
import subprocess
from sklearn import model_selection
from sklearn import linear_model
import webbrowser

failed_command = subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

if failed_command.returncode == 0:
  x=list(range(0,10)) # C creates the list of data between 0-9
  y=[1.8*F+32 for F in x] # F converts the c to f using above generated data
  #y=mx+c
  #F=1.8*C+32
  print("X:",x)
  print("X:",y)

  plt.plot(x,y,"-*r") # plots the graph for the x and y "-" defines the line * defines the point and r represents the color.
 # This shows the plotted graph
 # plt.show()
  ##### TO RUN THE BELOW CODE CLOSE THE GRAPH WINDOW ########
  x=np.array(x).reshape(-1,1)# ML needs array for higher acc so this creates the array
  y=np.array(y).reshape(-1,1)

  # We split train and test, but the sklearn comes inbuit for the spliting
  xTrain,xTest,yTrain,yTest=model_selection.train_test_split(x,y,test_size=0.2) #here 0.2 means20% i.e if we have 10 values it takes 2 values for testing(lower the better not more than 30%)
  model=linear_model.LinearRegression()
  model.fit(xTrain,yTrain) # fits the data into the linear reg model of sklearn
  print("coefficient",model.coef_)# Gives coefficient or the value of m
  print("Intercept",model.intercept_)# Gives intercept is c
  acc=model.score(xTest,yTest) # gets the accurcy of the training data
  print("Accuracy =","{}%".format(acc*100)) #show the accuracy(above 60 is great)
  plt.show() # This shows the plotted graph
else:
  print("Could not install the packages")
  print("----------------------------------------------------")
  no=input("If pip is installed type yes if not press no ")
  op=no.lower()
  if op=="yes" or op=="y":
    webbrowser.open("https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3")
  else:
    webbrowser.open("https://github.com/Namanskshetty/SIMPLE_ML#prerequisite")
  
