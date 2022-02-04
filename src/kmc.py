import math
import matrix
class KMeans:
    def __init__(self,initial_clusters,data):
        self.initial_clusters = initial_clusters
        self.cluster_copy = self.initial_clusters.copy()
        self.data = data


    def findmidpoint(self,cluster_index):
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

    def eucledian(self,midpoint,index,cluster_num):
        euclid = []
        euclid_average = 0

        for b in range(len(self.data[index])):
            euclid_average += (self.data[index][b] - midpoint[cluster_num][b]) **2

        euclid_average = math.sqrt(euclid_average)
        return euclid_average
        #just finished equlid, need to figure out which is best

    def run(self):
        clusters = {}
        midpoint = []
    #keys are cluster numbers
    #values are data_point_indecies
        cluster_numbers = list(self.cluster_copy.keys())
        datapoint_indecies = list(self.cluster_copy.values())
        
        for cluster_index in range(len(datapoint_indecies)):
            midpoint.append(self.findmidpoint(cluster_index))

        #finding midpoints with euclidean algorithm

        for i in range(len(midpoint)):
            clusters[i+1] = []

        for i in range(len(self.data)):
            euclid = []
            for cluster_num in range(len(midpoint)):
                euclid.append(self.eucledian(midpoint,i,cluster_num))
            
            min_val = min(euclid)
            clusters[euclid.index(min_val) + 1].append(i)

        if clusters != self.cluster_copy:
            self.cluster_copy = clusters
            self.run()
        else:
            self.cluster = clusters
            for item in range(len(midpoint)):
                midpoint[item] = matrix.roundarray(midpoint[item],3)
            self.midpoint = midpoint

