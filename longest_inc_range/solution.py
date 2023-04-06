from dataclasses import dataclass


@dataclass 
class Range: 
    start_id: int
    end_id: int

    def __len__(self) -> int: 
        return self.end_id - self.start_id + 1
    
    def __str__(self) -> str: 
        return f"({self.start_id}, {self.end_id})"

def find_range(lst: list[int]) -> Range: 
    # sorting + window sliding
    if len(lst) == 0:
        raise ValueError("Empty list, no max range.")
    
    lst.sort()

    current_r: Range = Range(0, 0)
    max_r: Range = current_r


    for cid in range(1, len(lst)): 
        if lst[cid] == lst[cid - 1] + 1: 
            current_r.end_id += 1
        else: 
            if len(current_r) > len(max_r): 
                max_r = current_r
            current_r = Range(cid, cid)

    # check if the last range is the max
    if len(current_r) > len(max_r): 
        max_r = current_r

    return Range(lst[max_r.start_id], lst[max_r.end_id])             



if __name__ == "__main__": 
    lst = [9, 6, 1, 3, 8, 10, 12, 11]
    print(find_range(lst))