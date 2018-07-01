#!/usr/bin/env python
import sdds, sys
import numpy as np
from ROOT import *

file_emit = sdds.SDDS(0)
file_phase = sdds.SDDS(0)
file_emit.load('phase_adv.fin')
file_phase.load('M_pars.sdds')

###############################2D graph

canv = TCanvas('name','title')

graph = TGraph()

final = len(file_emit.parameterData[39])

for n in range (0,final):
	x =float(file_phase.columnData[0][n]) #alpha
	y =float(file.parameterData[39][n])*10**6 #beta
	graph.SetPoint(n, x, y)
	print(n,"	",x,"emit",z)

graph.SetTitle('Final normalized x emitance before 1st compressor, [#mum];#Psi, m;#Emit_{x}, mkm')
graph.Draw("AP")


input('done')