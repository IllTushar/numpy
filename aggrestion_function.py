import numpy as np


def aggregation_function():
    arr = np.array([4, 3, 2, 1, 3, 4])
    print(np.mean(arr))
    print(np.max(arr))
    print(np.min(arr))
    print(np.size(arr))
    print(np.cumsum(arr))
    print(np.cumprod(arr))


def twoD_array_aggregation():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])
    c = np.cumprod([arr1, arr2], axis=0)
    print(np.sum(c))


if __name__ == '__main__':
    aggregation_function()
    twoD_array_aggregation()
