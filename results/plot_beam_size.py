#!/usr/bin/env python
import sdds, sys
import matplotlib.pyplot as plt 

file_name = sys.argv[1]

x = sdds.SDDS(0) # create an SDDS-interface object
x.load(file_name) # open an SDDS file named <file_name>

# x.columnName - a list of columns in the file
# x.columnData - column data

s = x.columnData[0][0]  # 0th column corresponds to "s" - as can be seen from print x.columnName
Sx = x.columnData[53][0]
Sy = x.columnData[55][0]

Sx_micro=[i*1e6 for i in Sx]
Sy_micro=[i*1e6 for i in Sy]

plt.figure() # creates a new figure
plt.plot(s, Sx_micro, label=r'$\sigma_x$')
plt.plot(s, Sy_micro, label=r'$\sigma_y$')
plt.xlabel('s [m]')
plt.ylabel(r'$\sigma$ [$\mu$m]')
plt.title('Beam size')
leg=plt.legend(loc='best')
#plt.show()
plt.savefig("beam-size.png")


