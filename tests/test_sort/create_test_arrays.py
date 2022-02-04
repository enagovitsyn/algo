import numpy as np
from tqdm import tqdm
import pickle
import matplotlib.pyplot as plt


def create_array(n=10):
    return np.random.randint(-100, high=100, size=n).tolist()


def create_test(count_test=1000):
    generic_arrays = [create_array(x) for x in np.random.randint(10, high=1000, size=count_test)]
    test_arrays = [(x, sorted(x)) for x in tqdm(generic_arrays)]
    return test_arrays


def save_test_arrays(test_arrays):
    with open("./test_arrays.pkl", 'wb') as f:
        pickle.dump(test_arrays, f)


def main():
    test_arrays = create_test()
    fig, ax = plt.subplots()
    ax.hist(list(map(lambda s: len(s[0]), test_arrays)))
    plt.show()
    save_test_arrays(test_arrays)


if __name__ == "__main__":
    main()
