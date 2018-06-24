#!/usr/bin/env python
import sdds, sys
import matplotlib.pyplot as plt 
from matplotlib.colors import LogNorm
import numpy as np

automatic_range=False

x_range = [-1200,1200]
y_range = [-1200,1200]
z_range = [-600,600]
xp_range = [-1e-3,1e-3]
p_range = [149.5,150.5]
deltap_range = [-0.5,0.5]

file_name = sys.argv[1]

sdds_object = sdds.SDDS(0) # create an SDDS-interface object
sdds_object.load(file_name) # open an SDDS file named <file_name>

# x.columnName - a list of columns in the file
# x.columnData - column data

x = sdds_object.columnData[0][0]
xp = sdds_object.columnData[1][0]
y = sdds_object.columnData[2][0]
t = sdds_object.columnData[4][0]
p = sdds_object.columnData[5][0]
pmean=np.average(p)
tmean=np.average(t)

x_micro=[i*1e6 for i in x]
y_micro=[i*1e6 for i in y]
z_micro=[(i-tmean)*1e6*3e8*(-1) for i in t]
p_MeV=[i*0.511 for i in p]
deltap_MeV=[(i-pmean)*0.511 for i in p]

plt.figure()
if automatic_range:
		range=None
else:
		range=[x_range, y_range]
plt.hist2d(x_micro, y_micro, range= range,bins=200) # add norm=LogNorm() for log scale
plt.xlabel('x [$\mu$m]')
plt.ylabel('y [$\mu$m]')
plt.title('Transverse beam profile')
plt.colorbar()
plt.savefig("bunch_xy.png")

plt.figure()
if automatic_range:
		range=None
else:
		range=[z_range, x_range]
plt.hist2d(z_micro, x_micro, range=range, bins=200) # add norm=LogNorm() for log scale
plt.xlabel('z [$\mu$m]')
plt.ylabel('x [$\mu$m]')
plt.title('Centroid offsets in x')
plt.colorbar()
plt.savefig("bunch_zx.png")

plt.figure()
if automatic_range:
		range=None
else:
		range=[z_range, xp_range]
plt.hist2d(z_micro, xp, range=range, bins=200) # add norm=LogNorm() for log scale
plt.xlabel('z [$\mu$m]')
plt.ylabel('x\'')
plt.title('Centroid kicks in x')
plt.colorbar()
plt.savefig("bunch_zxp.png")

#
plt.figure()
if automatic_range:
		range=None
else:
		range=[z_range, p_range]
plt.hist2d(z_micro, p_MeV, range=range, bins=200) # add norm=LogNorm() for log scale
plt.xlabel('z [$\mu$m]')
plt.ylabel('p [MeV]')
plt.title('Longitudinal phase space')
plt.colorbar()
plt.savefig("bunch_zp.png")

plt.figure()
if automatic_range:
		range=None
else:
		range=[z_range, deltap_range]
plt.hist2d(z_micro, deltap_MeV, range=range, bins=200) # add norm=LogNorm() for log scale
plt.xlabel('z [$\mu$m]')
plt.ylabel('p-<p> [MeV]')
plt.title('Longitudinal phase space')
plt.colorbar()
plt.savefig("bunch_zdeltap.png")

plt.show()
