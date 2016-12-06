import numpy as np


import numpy as np

# Set up matplotlib and use a nicer set of plot parameters
import matplotlib
matplotlib.rc_file("../../templates/matplotlibrc")
import matplotlib.pyplot as plt


#Get FITS Images
from astropy.utils.data import download_file

#Used in manipulating fits files
from astropy.io import fits


image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )

hdu_list = fits.open(image_file)
hdu_list.info()

image_data = hdu_list[0].data

print(type(image_data))
print(image_data.shape)


hdu_list.close()

plt.imshow(image_data, cmap='grey')
plt.colorbar()

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

print(type(image_data.flat))

NBINS = 1000
histogram = plt.hist(image_data.flat, NBINS)

from matplotlib.colors import LogNorm

plt.imshow(image_data, cmap='gray', norm=LogNorm())

# I chose the tick marks based on the histogram above
cbar = plt.colorbar(ticks=[5.e3,1.e4,2.e4])
cbar.ax.set_yticklabels(['5,000','10,000','20,000'])


