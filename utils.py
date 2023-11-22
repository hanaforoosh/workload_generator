from itertools import chain, combinations
def get_powerset(in_list):
    subsets = chain.from_iterable(
        combinations(in_list, r) for r in range(len(in_list) + 1)
    )
    powerset = [set(subset) for subset in subsets]
    powerset.remove(set())
    return powerset