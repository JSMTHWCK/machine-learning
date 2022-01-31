class KMeans:
    def __init__(self,initial_clusters,data):
        self.initial_clusters = initial_clusters
        self.data = data
    
    def run(self):
        clusters = []
        midpoint = []
        #finding midpoint
        for item in range(len(list(self.initial_clusters.values()))):
            average = [0,0,0,0]
            for index in list(self.initial_clusters.values())[item]:
                for a in range(len(self.data[index])):
                    average[a] += self.data[index][a]
            for a in range(len(average)):
                average[a] = average[a] / len(list(self.initial_clusters.values())[item])
            midpoint.append(average)
        #midpoint found
        #finding midpoints with euclidean algorithm

        #done
        self.clusters = clusters

