import numpy as np

import matplotlib.pyplot as plt

from astropy.utils.data import download_file
from astropy.io import fits

# I chose the tick marks based on the histogram above
image_list = [download_file('http://data.astropy.org/tutorials/FITS-images/M13_blue_000' + n + '.fits', cache=True) \
              for n in ['1', '2', '3', '4', '5']]

# The long way
image_concat = []
for image in image_list:
    image_concat.append(fits.getdata(image))

# The short way
# image_concat = [ fits.getdata(image) for image in IMAGE_LIST ]

# The long way
final_image = np.zeros(shape=image_concat[0].shape)

for image in image_concat:
    final_image += image

# The short way
#final_image = np.sum(image_concat, axis=0)

plt.imshow(final_image, cmap='gray', vmin=2.e3, vmax=3.e3)
plt.show()

outfile = 'stacked_M13_blue.fits'

hdu = fits.PrimaryHDU(final_image)
hdu.writeto(outfile, clobber=True)