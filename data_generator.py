import numpy as np

class DataGenerator:
    def __init__(self, n_traces=5000, points=50, seed=42):
        self.n_traces = n_traces
        self.points = points
        np.random.seed(seed)

    def generate(self):
        labels = np.random.randint(0, 2, self.n_traces)
        traces = np.random.normal(0, 0.8, (self.n_traces, self.points))
        for i in range(self.n_traces):
            if labels[i] == 1:
                traces[i, 25:28] += 1.0
        return traces, labels
