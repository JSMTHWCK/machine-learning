import math
class KMeans:
    def __init__(self,initial_clusters,data):
        self.initial_clusters = initial_clusters
        self.cluster_copy = self.initial_clusters.copy()
        self.data = data
    
    def run(self):
        clusters = {}
        midpoint = []
        #finding midpoint
        for item in range(len(list(self.cluster_copy.values()))):
            average = []
            for i in range(len(self.data[0])):
                average.append(0)
            for index in list(self.cluster_copy.values())[item]:
                for a in range(len(self.data[index])):
                    average[a] += self.data[index][a]
            for a in range(len(average)):
                average[a] = average[a] / len(list(self.cluster_copy.values())[item])
            midpoint.append(average)
        #midpoint found
        #finding midpoints with euclidean algorithm
        for i in range(len(midpoint)):
            clusters[i+1] = []
        for i in range(len(self.data)):
            euclid = []
            for a in range(len(midpoint)):
                euclid_average = 0
                for b in range(len(self.data[i])):
                    euclid_average += (self.data[i][b] - midpoint[a][b]) **2
                euclid_average = math.sqrt(euclid_average)
                euclid.append(euclid_average)
            #just finished equlid, need to figure out which is best

            min_val = min(euclid)
            clusters[euclid.index(min_val) + 1].append(i)
        if clusters != self.cluster_copy:
            print('l')
            self.cluster_copy = clusters
            self.run()
        else:
            self.cluster = clusters
        

