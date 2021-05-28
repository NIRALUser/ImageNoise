import numpy as np
import itk
import argparse
from matplotlib import pyplot as plt
import math


parser = argparse.ArgumentParser(description='Compute SNR of an image')

parser.add_argument('--img', type=str, help='Signal image sample', required=True)
parser.add_argument('--img2', type=str, help='Noise image/background sample', default=None)
parser.add_argument('--rescale', type=bool, help='Rescale the images between 0-1', default=True)



def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd), m, sd


args = parser.parse_args()

print("Reading:", args.img)
img = itk.imread(args.img)


img_np = itk.GetArrayViewFromImage(img)

rescale = args.rescale

if rescale:
	img_np = (img_np - np.min(img_np))
	img_np = img_np/(np.max(img_np))

if(args.img2):
	noise = itk.imread(args.img2)
	noise_np = itk.GetArrayViewFromImage(noise)

	if(rescale):
		noise_np = (noise_np - np.min(noise_np))
		noise_np = noise_np/(np.max(noise_np))

	noise_np = img_np - noise_np

	print("signal avg:", np.mean(img_np))
	print("noise avg:", np.mean(noise_np))
	sd_noise = np.std(noise_np)
	print("noise stdev:", sd_noise)

	snr = math.sqrt(2.0)*np.mean(img_np)/sd_noise
	print("snr:", snr)

else:
	snr, m, sd = signaltonoise(img_np.reshape(-1))

	print("mean:", m)
	print("sd:", sd)
	print("snr:", snr)


