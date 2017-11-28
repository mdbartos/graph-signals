from matplotlib import pyplot as plt
from matplotlib import collections
import mpl_toolkits.mplot3d.art3d as art3d

def Graph3d(x, y, z, **kwargs):
    xmin = kwargs.setdefault('xmin', x.min())
    xmax = kwargs.setdefault('xmax', x.max())
    ymin = kwargs.setdefault('ymin', y.min())
    ymax = kwargs.setdefault('ymax', y.max())
    zmin = kwargs.setdefault('zmin', z.min())
    zmax = kwargs.setdefault('zmax', z.max())

    if 'fig' in kwargs:
        fig = kwargs['fig']
    else:
        fig = plt.figure(figsize=(6,6))
    if 'ax' in kwargs:
        ax = kwargs['ax']
    else:
        ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax._axis3don = False

    for xi, yi, zi in zip(x, y, z):
        if zi >= 0:
            color = 'b'
        else:
            color = 'r'
        line = art3d.Line3D(*zip((xi, yi, 0), (xi, yi, zi)), marker='o',
                            markersize=2, markevery=(1, 1), color=color)
        ax.add_line(line)
    if 'lc' in kwargs:
        ax.add_collection3d(kwargs['lc'])

    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)
    ax.set_zlim3d(zmin, zmax)
    ax.set_facecolor('white')
    ax.view_init(elev=30., azim=300)
    plt.tight_layout()
