import numpy as np

import matplotlib.pyplot as plt

from astropy.io import fits
hdu_list = fits.open('stacked_M13_blue.fits')
hdu_list.info()

image_data = hdu_list[0].data

plt.imshow(image_data, cmap='Blues')
plt.colorbar()
plt.show()
input("Press Enter to continue...")

hdu_list.close()