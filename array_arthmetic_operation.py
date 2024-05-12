import numpy as np


def arithmetic_operations():
    arr1 = np.array([23, 3, 44])
    arr2 = np.array([9, 93, 29])
    print(np.add(arr1, arr2))
    print(np.subtract(arr1, arr2))
    print(np.multiply(arr1, arr2))
    print(np.divide(arr1, arr2))


def specific_operation():
    arr1 = np.array([2, 3, 5])
    arr2 = np.array([3])
    power = np.power(arr1, arr2)
    print(power)
    squre = np.sqrt(power)
    print(squre)


if __name__ == '__main__':
    arithmetic_operations()
    specific_operation()
