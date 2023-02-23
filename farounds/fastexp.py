

def exp(a: int, x: int):
    if x == 0:
        return 1

    if x == 1:
        return a

    if x % 2 == 0:
        temp: int = exp(a, x / 2)
        return temp * temp
    
    temp = exp(a, x // 2)
    return temp * temp * a



if __name__ == "__main__":
    print(f"2 to the power of 10 is {exp(2, 10)}")

