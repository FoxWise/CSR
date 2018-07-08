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


x =np.array(file_phase.columnData[0][0]) #psi
y =np.array(file_emit.parameterData[39])*10**6 #emit

n = len(file_phase.columnData[0][0])
graph = TGraph(n,x,y)

graph.SetMarkerStyle(20)
graph.SetTitle('Final normalized x emitance vs #Delta#Psi between BC;#Psi, rad;#epsilon_{n,x}, mkm')
graph.Draw("AP")


input('done')