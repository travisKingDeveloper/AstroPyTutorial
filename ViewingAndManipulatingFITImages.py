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
input("Press Enter to continue...")
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))
print(type(image_data.flat))
NBINS = 1000
from matplotlib.colors import LogNorm
plt.imshow(image_data, cmap='gray', norm=LogNorm())

# I chose the tick marks based on the histogram above
cbar = plt.colorbar(ticks=[5.e3,1.e4,2.e4])
cbar.ax.set_yticklabels(['5,000','10,000','20,000'])
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
plt.colorbar()

outfile = 'stacked_M13_blue.fits'

hdu = fits.PrimaryHDU(final_image)
hdu.writeto(outfile, clobber=True)