import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([1, 2])

# print np.sum(a == b)

print np.sum(a[:min(len(a), len(b))] == b[:min(len(a), len(b))])