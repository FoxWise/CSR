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
	x =float(file.parameterData[-3][n]) #alpha
	y =float(file.parameterData[-4][n]) #beta
	z =float(file.parameterData[39][n]*10**6)
	graph.SetPoint(n, x, y, z)
	print(n,"	",x,"emit",z)

#canv.SetLogz()

graph.SetTitle('Final normalized x emitance before 1st compressor, [#mum];#alpha_{x}, m;#beta_{x}, m')
graph.Draw("COLZ")


col1 = np.array(file.parameterData[-4])
col2 = np.array(file.parameterData[-3])
col3 = np.array(file.parameterData[-2])
col4 = np.array(file.parameterData[-1])
col5 = np.array(file.parameterData[39])*10**6

#here is your data, in two numpy arrays

data = np.array([col1, col2, col3, col4, col5])
data = data.T
#here you transpose your data, so to have it in two columns

datafile_path = "./datafile.txt"
with open(datafile_path, 'w+') as datafile_id:
#here you open the ascii file
	np.savetxt(datafile_id, data, fmt=['%f','%f','%f','%f','%f'])
#here the ascii file is written. 


input('done')
#plt.figure() # creates a new figure
#plt.pcolor(alphax[0],betax[0],enx)
#plt.xlabel('Alpha_x [m]')
#plt.ylabel('Beta_x [m]')
#plt.title('Final normalized x emitance')

#plt.show()


