from sklearn.neighbors import KernelDensity
from cmx import doc
import numpy as np

with doc:
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1, ], [2, 1], [3, 2]])

    kde = KernelDensity(kernel="gaussian", bandwidth=0.2).fit(X)
    scores = kde.score_samples(X)
    doc.print(scores)

doc @ """
The parameter `bandwidth` is a smoothing parameter.
"""