import sdds, sys
import numpy as np
from ROOT import TH1F,TCanvas,TGraph,TLegend,TLine

c = 3*(10**8)

file_name = "test1"

def main(var):
	file1 = var+'.w1'
	file2 = var+'.w3'

	file_emit = var+'.fin'

	f1 = sdds.SDDS(0) # create an SDDS-interface object
	f2 = sdds.SDDS(0) # create an SDDS-interface object
	f3 = sdds.SDDS(0)

	f1.load(file1)
	f2.load(file2)
	f3.load(file_emit)

	t1 = np.array(f1.columnData[4][0])
	p_mc1 = np.array(f1.columnData[5][0])
	t2 = np.array(f2.columnData[4][0])
	p_mc2 = np.array(f2.columnData[5][0])

	x1 = np.array(f1.columnData[0][0])
	xp1 = np.array(f1.columnData[1][0])
	x2 = np.array(f2.columnData[0][0])
	xp2 = np.array(f2.columnData[1][0])

	y1 = np.array(f1.columnData[2][0])
	yp1 = np.array(f1.columnData[3][0])
	y2 = np.array(f2.columnData[2][0])
	yp2 = np.array(f2.columnData[3][0])

	t01= 1.*sum(t1)/len(t1)
	t02= 1.*sum(t2)/len(t2)
	z1=np.array([-(x-t01)*c*(10**3) for x in t1])
	z2=np.array([-(y-t02)*c*(10**3) for y in t2])

	p1=np.array([x*0.511 for x in p_mc1])
	p2=np.array([y*0.511 for y in p_mc2])


	c1 = TCanvas('c1','test',800,800)

	c1.Divide(4,2)


	##############z-p
	c1.cd(1)

	gr1 = TGraph(len(z1),z1,p1)
	gr2 = TGraph(len(z2),z2,p2)

	gr1.GetXaxis().SetTitle('z [mm]')
	gr1.GetYaxis().SetTitle('p [MeV]')
	gr1.SetMarkerStyle(1)
	gr2.SetMarkerStyle(1)
	gr2.SetMarkerColor(2)

	gr1.SetTitle('[Z - P]')
	gr1.GetXaxis().SetLimits(min(np.concatenate((z1,z2))),max(np.concatenate((z1,z2))))


	gr1.Draw("ap")
	gr2.Draw("psame")

	######################################### CURRENT
	c1.cd(2)


	n_bins=100
	a=-3.
	b=3.
	h1 = TH1F('h1','Density Current',n_bins, a, b)
	h2 = TH1F('h2','Density Current',n_bins, a, b)

	for i in z1:
		h1.Fill(i)
	for i in z2:
		h2.Fill(i)

	h2.SetLineColor(2)

	h2.GetXaxis().SetTitle('z, [mm]')
	h2.GetYaxis().SetTitle('I, [kA]')

	h1.Scale(0.3*n_bins/(b-a)/50000.)
	h2.Scale(0.3*n_bins/(b-a)/50000.)

	h2.SetMaximum(0.2)

	h2.Draw('hist')
	h1.Draw("histsame")
	#############################################XXXXXXX-PPPPXXXX
	c1.cd(3)

	gr3 = TGraph(len(x1),x1*1000,xp1)
	gr4 = TGraph(len(x2),x2*1000,xp2)

	gr4.GetXaxis().SetTitle('x [mm]')
	gr4.GetYaxis().SetTitle('xp [mm]')
	gr3.SetMarkerStyle(1)
	gr4.SetMarkerStyle(1)
	gr4.SetMarkerColor(2)


	gr4.SetTitle('[X - PX]')

	gr4.Draw("ap")
	gr3.Draw("psame")
	#######################################################YYYYYYYYYYYYY--PYYYYYYYYYYY
	c1.cd(4)

	gr5 = TGraph(len(y1),y1*1000,yp1)
	gr6 = TGraph(len(y2),y2*1000,yp2)

	gr5.GetXaxis().SetTitle('y [mm]')
	gr5.GetYaxis().SetTitle('yp [mm]')
	gr5.SetMarkerStyle(1)
	gr6.SetMarkerStyle(1)
	gr6.SetMarkerColor(2)


	gr5.SetTitle('[Y - PY]')
	gr5.GetXaxis().SetLimits(min(np.concatenate((y1,y2)))*1000,max(np.concatenate((y1,y2)))*1000)

	gr5.Draw("ap")
	gr6.Draw("psame")
	#############################################
	###################################################XXXXXXXXXXXXXXX-YYYYYYYYYYY
	c1.cd(5)

	gr7 = TGraph(len(x1),x1*1000,y1*1000)
	gr8 = TGraph(len(x2),x2*1000,y2*1000)

	gr8.GetXaxis().SetTitle('x [mm]')
	gr8.GetYaxis().SetTitle('y [mm]')
	gr7.SetMarkerStyle(1)
	gr8.SetMarkerStyle(1)
	gr8.SetMarkerColor(2)

	gr8.SetTitle('[X - Y]')
	gr8.GetXaxis().SetLimits(min(z2),max(z2))

	gr8.Draw("ap")
	gr7.Draw("psame")
	#############################################XXXXXXXXx-ZZZZZZZZZZZZ
	c1.cd(7)

	gr9 = TGraph(len(z1),z1,x1*1000)
	gr10 = TGraph(len(z2),z2,x2*1000)
	main.graph1 = TGraph(len(z2),z2,x2*1000)

	gr10.GetXaxis().SetTitle('z [mm]')
	gr10.GetYaxis().SetTitle('x [mm]')
	gr9.SetMarkerStyle(1)
	gr9.SetMarkerStyle(1)
	gr10.SetMarkerColor(2)
	gr10.SetTitle('[Z - X]')


	gr10.GetXaxis().SetLimits(min(np.concatenate((z1,z2))),max(np.concatenate((z1,z2))))
	#gr9.SetMaximum(0.8)
	#gr9.SetMinimum(-0.8)


	gr10.Draw("ap")
	gr9.Draw("psame")
	##############################YYYYYYY-ZZZZZZZZZZZZ
	c1.cd(6)

	gr11 = TGraph(len(z1),z1,y1*1000)
	gr12 = TGraph(len(z2),z2,y2*1000)

	gr12.GetXaxis().SetTitle('z [mm]')
	gr12.GetYaxis().SetTitle('y [mm]')
	gr11.SetMarkerStyle(1)
	gr12.SetMarkerStyle(1)
	gr12.SetMarkerColor(2)

	gr12.SetTitle('[Z - Y]')
	gr12.GetXaxis().SetLimits(min(np.concatenate((z1,z2))),max(np.concatenate((z1,z2))))

	gr12.Draw("ap")
	gr11.Draw("psame")
	#############################################
	#DRAAAWING BETA FUNCTIONS
	#USE plot_beta.py

	input('kerk')

	
main(file_name)


input('kerk')