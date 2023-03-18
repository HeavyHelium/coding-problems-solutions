

def find_id(arr: list[int]): 
    lb: int  = 0
    up: int = len(arr) - 1
    ans: int = -1

    while lb <= up:
        mid: int = (lb + up) // 2
    
        if arr[mid] == mid:
            ans = mid
            # try left
            up = mid - 1
        elif arr[mid] > mid:
            # no right, try left
            up = mid - 1
        else: # arr[mid] < mid
            # no left, try right
            lb = mid + 1

    return ans;


        


if __name__ == "__main__": 

    # the array in the task is sorted, 
    # and its elements are distinct
    # this is essential for binary search
    # to give a correct solution

    arr1 = [-5, -3, 2, 3]
    assert find_id(arr1) == 2

    arr2 = [-10, -4, 2, 3, 4, 7, 9, 12, 13]
    assert(find_id(arr2) == 2)

