import numpy as np


def fileter_sort_search():
    arr = np.array([2, 6, 1, 5])
    # sort the array
    print(np.sort(arr))
    # search element in the array
    search = np.where(arr % 2 == 0)
    print(search)
    # sorted search and find the index in the array
    arr_2 = np.array([1, 2, 3, 4])
    print(np.searchsorted(arr_2, 3))
    # filter the array
    filter_array = arr % 2 == 0
    new_filter = arr[filter_array]
    print(new_filter)


if __name__ == '__main__':
    fileter_sort_search()
