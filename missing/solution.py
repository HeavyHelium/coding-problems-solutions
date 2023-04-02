import random

def print_missing(lst: list[int], n_range) -> list[int]: 
    n: int = len(lst)
    res: list[int] = [] # this is used for testing, 
                        # does not affect the space complexity

    for i in range(0, n):
        # put those smaller than n to their places
        while lst[i] < n and lst[i] != i:
            j = lst[i]
            lst[i] = lst[j]
            lst[j] = j

    # print those in the lower half missing

    for i in range(0, n):
        if lst[i] != i:
            #print(f"missing {i}")
            res.append(i)
    for i in range(0, n):
        # put those arr[i]: n <= arr[i] < n*2
        # to their places(all elements are assumed to be < n*2)
        # they are at most n, so we can use 
        # the array itself with a shift  
        while lst[i] >= n and lst[i] != n + i:
            j = lst[i]
            lst[i] = lst[j-n]
            lst[j-n] = j
    # print those in the upper half missing

    for i in range(0, n_range - n):
        if lst[i] != i + n:
            res.append(i + n)
            #print(f"missing {i + n}")

    return res    


def bogo_check(lst: list[int], n_range: int) -> list[int]: 
    missing: list[int] = []
    for i in range(0, n_range):
        if i not in lst:
            missing.append(i)
    return missing

def test_solution(): 
    n = 10000
    m = 9900
    num_list = random.sample(range(0, n), m)
    
    assert sorted(print_missing(num_list, n)) == sorted(bogo_check(num_list, n))

if __name__ == "__main__": 
    n = 100
    m = 90 # it holds true that n <= 2 * m
    test_solution()