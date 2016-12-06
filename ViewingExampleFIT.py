import numpy as np

import matplotlib.pyplot as plt

from astropy.utils.data import download_file
from astropy.io import fits
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )

hdu_list = fits.open(image_file)
hdu_list.info()

image_data = hdu_list[0].data

hdu_list.close()
image_data = fits.getdata(image_file)

plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.show()
input("Press Enter to continue...")
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

print(type(image_data.flat))
from matplotlib.colors import LogNorm
plt.imshow(image_data, cmap='Accent', norm=LogNorm())
plt.show()
input("Press Enter to continue...")