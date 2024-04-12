import pickle
import numpy as np

class Scores: 
    def __init__(self):
        with open("interface/data_np.pkl", "rb") as f:
            self.data:np.ndarray = pickle.load(f)
            self.n = len(self.data)
    
    def put(self, i, j, val):
        if i >= len(self.data) or j >= len(self.data):
            old_data = self.data
            self.data = np.zeros((max(i, j)+1, max(i, j)+1))
            self.data[:len(old_data), :len(old_data)] = old_data
        self.data[max(i, j)][min(i, j)] = val

    def get(self, i, j):
        if i >= len(self.data) or j >= len(self.data):
            return 0.0
        return self.data[max(i, j)][min(i, j)]
    
    def save(self):
        with open("interface/data_np.pkl", "wb") as f:
            pickle.dump(self.data, f)

class Scores_old:
    def __init__(self):
        with open("interface/data.pkl", "rb") as f:
            self.data = pickle.load(f)
            self.n = len(self.data)

    def put(self, i, j, val):
        if i >= len(self.data) or j >= len(self.data):
            for x in range(len(self.data), max(i, j)+1):
                self.data.append([0.0] * x)
                self.n += 1
        self.data[max(i, j)][min(i, j)] = val

    def get(self, i, j):
        if i >= len(self.data) or j >= len(self.data):
            return 0.0
        if i == j:
            return 0.0
        return self.data[max(i, j)][min(i, j)]

    def save(self):
        with open("interface/data.pkl", "wb") as f:
            pickle.dump(self.data, f)


if __name__ == "__main__" :
    old_scores = Scores_old()
    scores = Scores()
    for i in range(old_scores.n + 1) :
        for j in range(old_scores.n + 1) :
            scores.put(i, j, old_scores.get(i, j))
    scores.save()
    pass
