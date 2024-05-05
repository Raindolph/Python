
if __name__ == '__main__':
    num = 4
    nums = 3
    for a in range(1, num+1):
        for b in range(a):
            print("#", end="")
        print()
    for c in range(nums, 0, -1):
        for d in range(c):
            print("#", end="")
        print()
