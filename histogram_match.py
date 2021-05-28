import itk
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms
import argparse
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


parser = argparse.ArgumentParser(description='Matches the histogram of two images')

parser.add_argument('--img', type=str, help='Source image', required=True)
parser.add_argument('--ref', type=str, help='Reference image, the source will be matched against this reference image', required=True)
parser.add_argument('--out', type=str, help='Output image', default='out.nrrd')
parser.add_argument('--view', type=bool, help='View histograms', default=False)
parser.add_argument('--rescale', type=bool, help='Rescale the images between 0-1', default=True)


args = parser.parse_args()

print("Reading:", args.img)
img = itk.imread(args.img)

print("Reading:", args.ref)
ref = itk.imread(args.ref)


img_np = itk.GetArrayViewFromImage(img)
ref_np = itk.GetArrayViewFromImage(ref)

rescale = args.rescale
if rescale:
	img_np = (img_np - np.min(img_np))
	img_np = img_np/(np.max(img_np))

	ref_np = (ref_np - np.min(ref_np))
	ref_np = ref_np/(np.max(ref_np))

matched_np = match_histograms(img_np, ref_np)


if args.view:
	sns.histplot([img_np.reshape(-1), ref_np.reshape(-1), matched_np.reshape(-1)])
	plt.show()


print("Writing:", args.out)
matched = itk.image_from_array(matched_np)

itk.imwrite(matched, args.out)