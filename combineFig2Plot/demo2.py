import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)    
plt.style.use('seaborn-white') # from defaut
plt.rcParams.update({'font.size': 20})
plt.rcParams['savefig.dpi'] = 200
im = plt.imread(get_sample_data('grace_hopper.png'))

fig, ax = plt.subplots(figsize=(20,10))
ax.plot(range(10))

# Place the image in the upper-right corner of the figure
#--------------------------------------------------------
# We're specifying the position and size in _figure_ coordinates, so the image
# will shrink/grow as the figure is resized. Remove "zorder=-1" to place the
# image in front of the axes.
newax = fig.add_axes([1, 1, 0.2, 0.2], anchor='NE', zorder=-1)
newax.imshow(im)
newax.axis('off')

plt.show()
fig.savefig('demo2.png', bbox_inches='tight')