import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from itertools import product, combinations, combinations_with_replacement
import math
import re
import vtk_visualizer as vv
import numpy as np
import sys
from PyQt5.QtWidgets import *

##http://mathworld.wolfram.com/topics/Surfaces.html

def showFigure(filename):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    file_object = None
    try:
      file_object = open(filename, "r")
    except IOError:
        print("     ... file " + filename+" not exits!\n")
        return False
    vtkControl = vv.VTKVisualizerControl()
    a = []

    for line in file_object:
        numbers = (re.findall(r"[-+]?\d*\.\d+|\d+", line))
        x = float(numbers[0])
        y = float(numbers[1])
        z = float(numbers[2])
        a.append([x,y,z])
    
    b = np.array(a)
    vtkControl.AddPointCloudActor(b)
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    app.exec_()
    file_object.close()
#end def

def calculateTorus(R,r):
    file_object  = open("torus.txt", "w") 
    for theta in np.arange(0,2*np.pi,0.05):
        for phi in np.arange(0,2*np.pi,0.05):
                x = (R + r * np.cos(phi)) * np.cos(theta)
                y = (R + r * np.cos(phi)) * np.sin(theta)
                z = r * np.sin(phi)
                file_object.write(str(x)+" "+str(y)+" "+str(z)+"\n")
    file_object.close()
#end def

def calculateDrawTorus(R,r):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    for theta in np.arange(0,2*np.pi,0.4):
        for phi in np.arange(0,2*np.pi,0.4):
            ax.scatter((R + r * np.cos(phi)) * np.cos(theta), 
                    (R + r * np.cos(phi)) * np.sin(theta), 
                    r * np.sin(phi), 
                    color="r", marker='o') 
    plt.show()  
#end def

def calculateTetrahedron():
    file_object  = open("tetrahedron.txt", "w") 
    numbers = []
    for i in np.arange(0,1.1,0.05):
        numbers.append(i)
    for x,y,z in combinations(numbers, 3):
    	file_object.write(str(x)+" "+str(y)+" "+str(z)+"\n")
    file_object.close()
#end def

def calculateDrawTetrahedron():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    numbers = []
    for i in np.arange(0,1.1,0.1):
        numbers.append(i)
    for x,y,z in combinations(numbers, 3):
    	ax.scatter(x, y, z, color="b", marker='o')
    plt.show()
#end def

def calculateTriangle():
    file_object  = open("triangle.txt", "w") 
    numbers = []
    for u in np.arange(0,4,0.05):
        for v in np.arange(0,((4-u)/2),0.05):
            x = u
            y = v
            z = 4-u-2*v
            file_object.write(str(x)+" "+str(y)+" "+str(z)+"\n")
    file_object.close()
#end def

def calculateDrawTriangle():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    for u in np.arange(0,4,0.2):
        for v in np.arange(0,((4-u)/2),0.2):
            ax.scatter(u, v, 4-u-2*v, 
                color="r", marker='o')
    plt.show()
#end def

def calculateCube():
    file_object  = open("cube.txt", "w") 
    numbers = []
    for i in np.arange(0,1.05,0.05):
        numbers.append(i)
    for x,y,z in product(numbers, repeat=3):
        if x == 0 or x == 1 or y == 0 or y == 1 or z == 0 or z == 1:
            file_object.write(str(x)+" "+str(y)+" "+str(z)+"\n")  
    file_object.close()
#end def

def calculateDrawCube():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    numbers = []
    for i in np.arange(0,1.1,0.2):
        numbers.append(i)
    for x,y,z in product(numbers, repeat=3):
        if x == 0 or x == 1 or y == 0 or y == 1 or z == 0 or z == 1:
            ax.scatter(x, y, z, color="b", marker='o')
    plt.show()
#end def

def calculateSphere():
    file_object  = open("sphere.txt", "w")
    for u in np.arange(0, 2*np.pi, 0.1):
        for v in np.arange(0, 2*np.pi, 0.1):
            x = np.cos(u)*np.sin(v)
            y = np.sin(u)*np.sin(v)
            z = np.cos(v)
            file_object.write(str(x)+" "+str(y)+" "+str(z)+"\n")  
    file_object.close()
#end def

def calculateDrawSphere():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    ax.scatter(x, y, z, color="r", marker='o')
    plt.show()
#end def

def calculateCylinder():
    file_object  = open("cylinder.txt", "w")

    for u in np.arange(0, 2*np.pi, 0.1):
        for z in np.arange (0,10,0.1):##danger
            x = np.cos(u)
            y = np.sin(u)
            file_object.write(str(x)+" "+str(y)+" "+str(z)+"\n")

        
    for i in np.arange(1,0,-0.1):
        for u in np.arange(0, 2*np.pi, 0.1):
            x = i*np.cos(u)
            y = i*np.sin(u)
            file_object.write(str(x)+" "+str(y)+" "+str(0)+"\n")
            file_object.write(str(x)+" "+str(y)+" "+str(z)+"\n")

    file_object.close()
#end def

def calculateDrawCylinder():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    u = np.mgrid[0:2*np.pi:40j]
    for z in range (0,40):
        x = np.cos(u)
        y = np.sin(u)
        ax.scatter(x, y, z, color="r", marker='o')
    for i in np.arange(1,-0.1,-0.1):
        x = i*np.cos(u)
        y = i*np.sin(u)
        ax.scatter(x, y, z, color="r", marker='o')
        ax.scatter(x, y, 0, color="r", marker='o')
    plt.show()
#end def

def calculateParaboloid():
    file_object  = open("paraboloid.txt", "w")
    for u in np.arange(0, 2*np.pi, 0.05):
        for v in np.arange(0, np.pi, 0.05):
            x = 1*np.cos(v)*np.cos(u)
            y = 1*np.cos(v)*np.sin(u)
            z = np.cos(v)*np.cos(v)
            file_object.write(str(x)+" "+str(y)+" "+str(z)+"\n")  
    file_object.close()
#end def

def calculateDrawParaboloid():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
    x = 1*np.cos(v)*np.cos(u)
    y = 1*np.cos(v)*np.sin(u)
    z = np.cos(v)*np.cos(v)
    ax.scatter(x, y, z, color="r", marker='o')
    plt.show()
#end def

opc = -1
while opc != 0:
    print(" Menu \n     0. Exit."     
        + "\n   1. Calculated solids."
        + "\n   2. Draw torus."
        + "\n   3. Draw tetrahedron."
        + "\n   4. Draw triangle."
        + "\n   5. Draw cube."
        + "\n   6. Draw sphere."
        + "\n   7. Draw cylinder."
        + "\n   8. Draw paraboloid.")

    opc = int(input("Enter option: "))
    if opc == 0:
        print("     ... Bye!\n")
    elif opc == 1:
        calculateTorus(4,0.5)
        calculateTetrahedron()
        calculateTriangle()
        calculateCube()
        calculateSphere()
        calculateCylinder()
        calculateParaboloid()
    elif opc == 2:
        showFigure("torus.txt")  
    elif opc == 3:
        showFigure("tetrahedron.txt") 
    elif opc == 4:
        showFigure("triangle.txt") 
    elif opc == 5:
        showFigure("cube.txt")  
    elif opc == 6:
        showFigure("sphere.txt")  
    elif opc == 7:
        showFigure("cylinder.txt")  
    elif opc == 8:
        showFigure("paraboloid.txt")  
    elif opc == 9:
        calculateDrawTorus(4,0.5)
    elif opc == 10:
        calculateDrawTetrahedron()
    elif opc == 11:
        calculateDrawTriangle()
    elif opc == 12:
        calculateDrawCube()
    elif opc == 13:
        calculateDrawSphere()
    elif opc == 14:
        calculateDrawCylinder() 
    elif opc == 15:
        calculateDrawParaboloid() 
    else:
        print("     ... please enter a valid option!\n")
    # end switch case
#end while