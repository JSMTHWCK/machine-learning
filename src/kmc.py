import math
class KMeans:
    def __init__(self,initial_clusters,data):
        self.initial_clusters = initial_clusters
        self.cluster_copy = self.initial_clusters.copy()
        self.data = data


    def midpoint(self,cluster_index):
        datapoint_indecies = list(self.cluster_copy.values())
        average = []            
        for i in range(len(self.data[0])):
            average.append(0)

        for index in datapoint_indecies[cluster_index]:

            for a in range(len(self.data[index])):
                average[a] += self.data[index][a]

        for a in range(len(average)):
            average[a] = average[a] / len(datapoint_indecies[cluster_index])
        return average

    def eucledian(self,midpoint,index):
        euclid = []

        for a in range(len(midpoint)):
            euclid_average = 0

            for b in range(len(self.data[index])):
                euclid_average += (self.data[index][b] - midpoint[a][b]) **2

            euclid_average = math.sqrt(euclid_average)
            euclid.append(euclid_average)
        return euclid
        #just finished equlid, need to figure out which is best

    def run(self):
        clusters = {}
        midpoint = []
    #keys are cluster numbers
    #values are data_point_indecies
        cluster_numbers = list(self.cluster_copy.keys())
        datapoint_indecies = list(self.cluster_copy.values())
        
        for cluster_index in range(len(datapoint_indecies)):
            midpoint.append(self.midpoint(cluster_index))

        #finding midpoints with euclidean algorithm

        for i in range(len(midpoint)):
            clusters[i+1] = []

        for i in range(len(self.data)):
            euclid = self.eucledian(midpoint,i)
            
            min_val = min(euclid)
            clusters[euclid.index(min_val) + 1].append(i)

        if clusters != self.cluster_copy:
            self.cluster_copy = clusters
            self.run()
        else:
            self.cluster = clusters
        

