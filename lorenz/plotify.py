# modules we need

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import h5py

# Load h5py file
data= h5py.File('lorenz.h5','r')

t=data['1']['t']
x=data['1']['xR']
y=data['1']['yR']
z=data['1']['zR']

N=len(t)


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)
plt.savefig('lorenz_attractor.png')
plt.show()
