import numpy as np
import statistics as stats


def statics_data():
    data = np.array([1, 2, 3, 4])
    print(np.mean(data))
    print(np.var(data))
    print(stats.mode(data))
    print(np.std(data))


if __name__ == '__main__':
    statics_data()
