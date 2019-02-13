import vtk_visualizer as vv
import numpy as np
import sys
from PyQt5.QtWidgets import *

##internet example
xyz = np.random.rand(1000, 3)
vtkControl = vv.VTKVisualizerControl()
vtkControl.AddPointCloudActor(xyz)
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)
app.exec_()