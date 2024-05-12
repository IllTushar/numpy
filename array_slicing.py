import numpy as np


def array_slicing():
    arr = np.array([[10, 20, 30], [40, 50, 60]])
    shape = arr.shape
    # print(arr.size)
    # print row element
    # print(arr[1, :])
    # print index element
    # print(arr[1, 2])
    print(np.ndim(arr))
    


if __name__ == '__main__':
    array_slicing()
