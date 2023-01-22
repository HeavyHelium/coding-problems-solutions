def hoare_partition(arr: list[int], pivot: int) -> int: 
    i: int = -1
    j: int = len(arr)

    while True: 
        i += 1
        j -= 1

        while arr[i] < pivot: 
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j: 
            return i
        
        arr[i], arr[j] = arr[j], arr[i]


def kth_smallest(arr: list[int], k: int): 
    if k < 0 or k >= len(arr): 
        raise IndexError("Index put of bound")
   
    # for simplicity, the last element is chosen as pivot
    idx = hoare_partition(arr, arr[-1])
    
    if idx == k: 
        return arr[idx]

    if idx < k: 
        return kth_smallest(arr[idx + 1: ], k - idx - 1)

    return kth_smallest(arr[0:idx], k)

if __name__ == "__main__": 
#    arr: list[int] = [1, 8, 4, 6, 4]
#    id: int = hoare_partition(arr, 5)
#    print(f"arr is: { arr }, first >='s id is: { id }")
    
    arr = [ 10, 4, 5, 8, 6, 11, 26 ]
    k = 2

    sored_unique = [kth_smallest(arr, i) for i in range(len(arr))]
    print("sorted array is: ", sorted(arr))
    print("sorted with quickselect is: ", sored_unique)
    assert(sored_unique == sorted(arr))
