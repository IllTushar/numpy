import numpy as np


def insertion_and_deletion():
    arr = np.array([1, 2, 5, 3, 4])
    print(np.insert(arr, 3, 87))
    print(np.delete(arr, 3, 0))


if __name__ == '__main__':
    insertion_and_deletion()
