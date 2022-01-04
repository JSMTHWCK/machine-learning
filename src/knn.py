import math
import copy
from matrix import *    

class KNC:
    def __init__(self,k):
        self.k = k
    
    def fit(self,data,classification):
        self.data = data
        self.classification = classification
    
    def compute_distance(self,observation):
        distances = []
        for i in self.data:
            distances.append(0)
        for row in self.data:
            for i in range(0,len(self.data[0])):
                x = (observation[i] - row[i]) **2
                distances[self.data.index(row)] += math.sqrt(x)
        return roundarray(distances,3)
    
    def classify(self,observation):
        distances = self.compute_distance(observation)
        dist_copy = copy.copy(distances)
        closest = sorted(dist_copy)
        print('a')
        print(closest)
        indexes = []
        for i in range(0,len(closest)):
            index = distances.index(closest[i])
            indexes.append(index)
        classifications = []
        for i in indexes:
            classifications.append(self.classification[i])

        counts = {}
        for each in classifications:
            if each not in counts:
                counts[each] = 1
            else:
                counts[each] += 1
            answer = max(counts,key=counts.get)
            return answer