import numpy as np
from scipy.stats import pearsonr

class CPAAnalyzer:
    def compute(self, traces, labels):
        corr = np.zeros(traces.shape[1])
        for i in range(traces.shape[1]):
            corr[i], _ = pearsonr(traces[:, i], labels)
        return 0.5 + np.max(abs(corr)) * 0.25
