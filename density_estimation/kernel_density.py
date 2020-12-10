from sklearn.neighbors import KernelDensity
from cmx import doc
import numpy as np

bandwidth = 0.1

doc @ f"""
The parameter `bandwidth={bandwidth}` is a smoothing parameter.
"""

with doc:
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1, ], [2, 1], [3, 2]])

    kde = KernelDensity(kernel="gaussian", bandwidth=bandwidth)
    kde.fit(X)
    scores = kde.score_samples(X)
    doc.print(scores)
