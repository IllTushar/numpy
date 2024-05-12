import numpy as np


def array_inspect():
    arr = np.array([[0, 10, 5], [40, 98, 33]])
    # print size of the array
    print(arr.size)
    # print n x m matrix
    print(arr.shape)
    # print n dimension matrix
    print(arr.ndim)
    # print array type
    print(type(arr))
    # change the type of array
    print(arr.astype(str))


if __name__ == '__main__':
    array_inspect()
