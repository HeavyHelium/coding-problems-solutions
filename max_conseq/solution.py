
def max_conseq(arr: list[int]):
    num_set = set(arr)

    max_len = 0

    for elem in arr:
        if elem - 1 not in num_set:
            curr_len = 1
            while elem + 1 in num_set:
                curr_len += 1
                elem += 1
            max_len = max(max_len, curr_len)
    
    return max_len

# what is worst case scenario?
# why is this O(n) time complexity?


if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    arr1 = [5, 2, 99, 3, 4, 1, 100]


    assert max_conseq(arr) == 4
    assert max_conseq(arr1) == 5