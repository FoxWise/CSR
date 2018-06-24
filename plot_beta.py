#!/usr/bin/env python
import sdds, sys
import numpy as np
from ROOT import TCanvas,TGraph,TLegend,TLine


file_name = sys.argv[1]

x = sdds.SDDS(0) # create an SDDS-interface object
x.load(file_name) # open an SDDS file named <file_name>

# x.columnName - a list of columns in the file
# x.columnData - column data

s = np.array(x.columnData[0][0])  # 0th column corresponds to "s" - as can be seen from print x.columnName
betax = np.array(x.columnData[1][0])
betay = np.array(x.columnData[7][0])

canv = TCanvas('name',r'$\beta-functions$')

grx = TGraph(len(s),s,betax)
gry = TGraph(len(s),s,betay)

grx.GetXaxis().SetTitle('s [m]')
gry.GetXaxis().SetTitle('s [m]')

grx.GetYaxis().SetTitle(r'$\beta_{x,y} [m]$')
gry.GetYaxis().SetTitle(r'$\beta_{x,y} [m]$')

grx.SetTitle(r'$\beta_x$')
gry.SetTitle(r'$\beta_y$')

gry.SetLineColor(2)

#grx.Draw('AL')
#gry.Draw('Lsame')

gry.Draw('AL')
grx.Draw('Lsame')

canv.BuildLegend()
input('you r briliant')