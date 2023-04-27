from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

objects = OrderedDict()
objects[0] = (1,1)
objects[1] = (10,10)


inputCentroids = np.zeros((3, 2), dtype='int')

inputCentroids[0] = (1,2)
inputCentroids[1] = (5,5)
inputCentroids[2] = (10,12)

objectIDs = list(objects.keys())
objectCentroids = list(objects.values())


D = dist.cdist(np.array(objectCentroids), inputCentroids)

rows = D.min(axis=1).argsort()
cols = D.argmin(axis=1)[rows]

a = zip(rows, cols)

print(D)
print(rows)
print(cols)
print(D.shape[0])
print(D.shape[1])

