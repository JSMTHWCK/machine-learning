import math
import math
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
                #print(observation[i])
                #print(row[i])
                x = (observation[i] - row[i]) **2
                distances[self.data.index(row)] += math.sqrt(x)
        return distances
    def classify(self,observation,all_classification = False):
        class_copy = self.classification
        distances = self.compute_distance(observation)
        dist_copy = list(distances)
        class_copy = list(self.classification)
        count = {}
        for i in range(self.k):
            mindex = dist_copy.index(min(dist_copy))
            if class_copy[mindex] not in count:
                count[class_copy[mindex]]= 1
            else:
                count[class_copy[mindex]]+= 1
            class_copy.pop(mindex)
            dist_copy.pop(mindex)

        if all_classification == True:
            return count
        answer = max(count,key=count.get)
        return answer
        #a = list(count.values()).index(max(list(count.values)))
            #finds all distances
        
