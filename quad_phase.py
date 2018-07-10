#!/usr/bin/env python
import sdds, sys
import numpy as np
from ROOT import *

file = sdds.SDDS(0)
file.load('QUAD_K_probe.fin')

canv = TCanvas('name','title')

x =np.array(file.parameterData[-1]) #K1
y =np.array(file.parameterData[39])*10**6 #emit

n = len(file.parameterData[-1])

graph = TGraph(n,x,y)

graph.SetMarkerStyle(20)
graph.SetTitle('Final normalized x emitance vs K1 between BC;K1, #frac{1}{M^{2}};#epsilon_{n,x}, mkm')
graph.Draw("AP")


input('done')