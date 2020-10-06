```python
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1, ], [2, 1], [3, 2]])

kde = KernelDensity(kernel="gaussian", bandwidth=0.2).fit(X)
scores = kde.score_samples(X)
doc.print(scores)
```

```
[-0.41075698 -0.41075698 -0.41076071 -0.41075698 -0.41075698 -0.41076071]
```
