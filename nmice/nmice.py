def find_mapping(holes: list[int], 
                 mice: list[int]): 
    assert(len(holes) == len(mice))
    holes.sort()
    mice.sort()
    return abs(holes[0] - mice[0]) 


if __name__ == "__main__":
    mice = [1, 4, 9, 15]
    holes = [10, -5, 0, 16]
    print(find_mapping(holes, mice))