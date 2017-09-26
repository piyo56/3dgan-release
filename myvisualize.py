import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

m = scipy.io.loadmat("output/chair_demo.mat")
voxels = m['voxels']

# array[x, y, z] = prob -> indices array where prob > 0.5
for i in range(voxels.shape[0]):
    fig = plt.figure(figsize=(4, 3))
    ax = fig.add_subplot("111", projection='3d')
    indices = np.argwhere(voxels[i,0] > 0.5)
    x, y, z = indices[:, 0], indices[:, 1], indices[:, 2]
    ax.scatter(x, y, z, color='r', s=2)
    ax.set_xlim(0, 64)
    ax.set_ylim(0, 64)
    ax.set_zlim(0, 64)

plt.show()
