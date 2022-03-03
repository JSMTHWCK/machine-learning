from kmc import *
import matplotlib
import matplotlib.pyplot as plt

x_axis = [x for x in range(1,18)]
y_axis = [0 for a in x_axis]
data = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]

def rss(a,b):
    assert len(a) == len(b), 'unequal length'
    tot = 0
    for i in range(len(a)):
        tot += (a[i] - b[i])**2
    return tot ** 0.5

for a in range(1,len(x_axis)+1):
    clusters = {}
    for i in range(1,a+1):
        clusters[i] = []
    for j in range(0,len(data)):
        clusters[(j%len(clusters))+1].append(j)
    #clustering works now
    km = KMeans(clusters,data)
    km.run()

    for intry in list(km.cluster.keys()):
        #returns 1,2,3 ... 
        for i in km.cluster[intry]:
            y_axis[a-1] += rss(data[i],km.midpoint[intry-1])
  
plt.plot(x_axis,y_axis)


plt.savefig('tests.png')