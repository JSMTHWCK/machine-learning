from kmc import *
import matplotlib
import matplotlib.pyplot as plt

x_axis = [1,2,3,4]
y_axis = [1,2,3,4] #will be the euclid values

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

for a in range(1,len(x_axis)+1):
    clusters = {}
    for i in range(1,a+1):
        clusters[i] = []
    for j in range(0,len(data)):
        clusters[(j%len(clusters))+1].append(j)
    #clustering works now
    km = KMeans(clusters,data)
    km.run()

    



plt.plot(x_axis,y_axis)
plt.savefig('test.png')