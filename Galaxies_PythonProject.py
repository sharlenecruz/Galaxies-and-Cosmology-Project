
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#FILTERING OUT DATA

data = np.loadtxt("C:/Users/Sharlene/Documents/USF/Galaxies_Cosmology/CruzGonzalez/2dF_Data.txt", skiprows=1, usecols= (1,2,4,7))
print "original size of data:", len(data)
filter_qual = data[:,3] >= 3.00
qual_data = data[filter_qual]
print "after filtering bad quality:", len(qual_data)

filter_z = qual_data[:,2] <= 0.100
qual_zdata = qual_data[filter_z]
print "after filtering bad redshift(z):", len(qual_zdata)


#PLOT CALCULATIONS

theta = qual_zdata [:,0]
phi = qual_zdata[:,1]
z_red = qual_zdata[:,2]
r = ((2.99*10**8)*(z_red))/(70*10**3)
x = np.multiply(np.multiply(r,np.sin(phi)),np.cos(theta))
y = np.multiply(np.multiply(r,np.sin(phi)),np.sin(theta))
z = np.multiply(r,np.cos(phi))


#FINDING MASS

minra = np.amin(qual_zdata[:,0])
maxra = np.amax(qual_zdata[:,0])
ra = maxra - minra
maxz = np.amax(z_red)
c= 2.99*10**8
velocity = maxz*c
H=70*10**3
Mass = (ra*(velocity**2))/H
Mass_kg = Mass*(10**(12))*(1.99*10**(30))


#FINDING VOLUME

maxdec = np.amax(qual_zdata[:,1])
mindec = np.amin(qual_zdata[:,1])
dec = maxdec - mindec
radius = np.amax(r)
c = 2.99*10**8
H = 70*10**3
Volume = (2*dec*((radius)**3))/3 

#FINDING MASS DENSITY

Mass_Density = (Mass)/(Volume)

#PRINTING VALUES NEEDED

print "minra = ", np.amin(qual_zdata[:,0])
print "maxra = ", np.amax(qual_zdata[:,0])
print "mindec = ", np.amin(qual_zdata[:,1])
print "maxdec = ", np.amax(qual_zdata[:,1])
print "maxz = ", (maxz)
print "radius = ", np.amax(r)
print "dec = ", maxdec - mindec
print "ra = ", (ra)
print "Mass of Universe Slice = ", (Mass_kg), "kg"
print "Volume of Universe Slice = ", (2*dec*((radius)**3))/3, "Mpc"
print "Mass Density of Universe Slice = ", (Mass_Density)

#MAKING THE 3-D PLOT

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, zdir='z', s=1, c='r', depthshade=True)
ax.set_xlabel('X (Mpc)')
ax.set_ylabel ('Y (Mpc)')
ax.set_zlabel('Z (Mpc)')
plt.show()
