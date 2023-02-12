from dataclasses import dataclass

@dataclass
class Interval:
    # values need not be integers, 
    # but it doesn't matter too much for the solution
    start: int
    end: int
    weight: int 

def p(j: int, intervals: list[Interval]):
    """
    :return: the largest index i < j request i and j are compatible 
    performs a binary search, i.e. looking for "upper bound"
    i.e. the largest index i < j such that intervals[i].end <= intervals[j].start
    """
    low: int = 0
    high: int = j - 1
    while low <= high: 
        mid: int = (low + high) // 2
        if intervals[mid].end <= intervals[j].start: # i.e. intervals[mid] and intervals[j] are compatible
            if intervals[mid + 1].end <= intervals[j].start: # i.e. intervals[mid + 1] and intervals[j] are compatible
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

def schedule(intervals: list[Interval]): 
    # sort intervals by end time
    intervals.sort(key=lambda x: x.end) # O(nlogn)
    dp = [0] * len(intervals) # dp[k] is the maximum weight if requests 0, ..., k are considered
    dp[0] = intervals[0].weight

    for j in range(1, len(intervals)): # O(n)
        
        i = p(j, intervals) # O(logn)
        new_value = intervals[j].weight
        
        if i != -1:
            new_value += dp[i]

        dp[j] = max(new_value, dp[j - 1])
    
    return dp[-1]

if __name__ == "__main__": 
    intervals = [Interval(1, 2, 50), Interval(3, 5, 20), 
                 Interval(6, 19, 100), Interval(2, 100, 200)]

    print(f"Optimal total weight: { schedule(intervals) }")

