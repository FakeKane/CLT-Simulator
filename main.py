# Distribution types: Uniform, Normal, Skewed Left (moderately), Skewed Right, Bimodal

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
data = []


def gen_norm(n):
    return np.random.normal(0, 2, n)


def gen_uniform(n):
    return np.random.uniform(-np.sqrt(12), np.sqrt(12), n)


def gen_skewed(n):
    lst_skew = np.random.chisquare(2, n)

    for i in range(len(lst_skew)):
        lst_skew[i] = lst_skew[i] - 2

    return lst_skew


def gen_bimod(n):
    lst1 = np.random.normal(-4 / np.sqrt(5), 2 / np.sqrt(5), n / 2)
    lst2 = np.random.normal(4 / np.sqrt(5), 2 / np.sqrt(5), n / 2)
    out = np.concatenate([lst1, lst2])
    return out


def gen_pop(n, distr):
    data = []
    if distr == 1:
        data = gen_norm(n)
    elif distr == 2:
        data = gen_uniform(n)
    elif distr == 3:
        data = gen_skewed(n)
    elif distr == 4:
        data = gen_bimod(n)
    return data


def draw(data, addnorm, sample_size):
    n, bins, patches = plt.hist(data, 50, normed=1, facecolor='green', alpha=0.5)
    if addnorm:
        y = mlab.normpdf(bins, 0, 2 / np.sqrt(sample_size))
        plt.plot(bins, y, 'r--')
    plt.title("Konsler's Cookies Profit Percentage")
    plt.show()


def sample(pop, samp_size):
    samp = []

    for i in range(samp_size):
        samp += [pop[random.randint(0, len(pop) - 1)]]
    return samp


def mean(data):
    agg = 0.0
    for i in data:
        agg += i

    return agg / (len(data))


def main():
    distr_type = 1
    sample_size = 30
    sample_num = 1000
    pop_size = 1000000
    pop = gen_pop(pop_size, distr_type)  # Yo
    data = []
    for i in range(sample_num):
        data += [mean(sample(pop, sample_size))]
    draw(data, distr_type == 1, sample_size)
main()
