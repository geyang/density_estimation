
The parameter `bandwidth=0.1` is a smoothing parameter.

```python
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1, ], [2, 1], [3, 2]])

kde = KernelDensity(kernel="gaussian", bandwidth=bandwidth)
kde.fit(X)
scores = kde.score_samples(X)
doc.print(scores)
```

```
[0.97553365 0.97553365 0.97553365 0.97553365 0.97553365 0.97553365]
```
