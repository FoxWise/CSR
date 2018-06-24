#!/usr/bin/env python
import sdds, sys
import numpy as np
from ROOT import *

file = sdds.SDDS(0)
file.load('alpha_beta.fin')

###############################2D graph

canv = TCanvas('name','title')

graph = TGraph2D()

final = len(file.parameterData[-1])

for n in range (0,final):
	x =float(file.parameterData[-1][n]) #alpha
	y =float(file.parameterData[-2][n]) #beta
	z =float(file.parameterData[39][n]*10**6)
	graph.SetPoint(n, x, y, z)

#canv.SetLogz()

graph.SetTitle('Final normalized x emitance, [#mum];#alpha_{x}, m;#beta_{x}, m')
graph.Draw("COLZ")

#betax = np.array(file.parameterData[-2]).reshape(20,20)
#alphax = np.array(file.parameterData[-1]).reshape(20,20).T
#enx = np.array(file.parameterData[39]).reshape(20,20).T
 


input('done')
#plt.figure() # creates a new figure
#plt.pcolor(alphax[0],betax[0],enx)
#plt.xlabel('Alpha_x [m]')
#plt.ylabel('Beta_x [m]')
#plt.title('Final normalized x emitance')

#plt.show()


