import numpy as np
from scipy import cluster
from PIL import Image
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
parser.add_argument('--k', dest='k', required=True, type=int)
args=parser.parse_args()
img=Image.open(args.input)
data=np.asfarray(img)
data=data/255
a=data.shape[0]
b=data.shape[1]
data=data.reshape(a*b, 3)
centroid, label=cluster.vq.kmeans2(data, minit='++', k=args.k)
data=[centroid[i] for i in label]
data=np.array(data).reshape(a,b,3)
im = Image.fromarray((np.ceil( data*255)).astype(np.uint8))
im.save(args.output)
