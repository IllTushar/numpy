import numpy as np


def split_join_array():
    a = np.array([9, 22, 34, 33, 34])
    b = np.array([3, 29, 22, 88, 33])
    # add element horizontal
    print(np.hstack((a, b)))
    # add element vertical
    print(np.vstack((a, b)))
    c = np.array_split(a, 2)
    print(c[0])


if __name__ == '__main__':
    split_join_array()
