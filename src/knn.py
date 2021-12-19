import math

def calc_minimum(numbers):
    a = numbers[0]
    for n in numbers:
        if n < a:
            a = n
    return a

class KnnClassifier:
    def __init__(self,k):
        self.k = k 
    def fit(self,data,classification):
        self.data = data
        self.classification = classification
    def compute_distance(self,observation):
        distances = []
        for i in self.data:
            distances.append(0)
        