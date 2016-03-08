#!/usr/bin/env python

import csv
from scipy.cluster.vq import kmeans, vq
from numpy import vstack
import pickle

f = open('kddcup.testdata.unlabeled_10_percent.csv', 'rb')
rows = []

# read csv data 
reader = csv.reader(f)
for row in reader:
    row = [float(r) for r in row]
    rows.append(row)        
f.close()

# kmeans
data = vstack(rows)
centroids, dist = kmeans(data, 23)
print centroids

# save centroids to file
f = open('centroids.csv','wb')
f.write(pickle.dumps(centroids))
f.close()

