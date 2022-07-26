from itertools import permutations as pm
from math import ceil

def middle_permutation(s):
    perm = (["".join(rep) for rep in ((pm(s)))])
    return perm[ceil(len(perm) / 2)]


if __name__ == "__main__":
    string = "abc"
    print(middle_permutation(string))