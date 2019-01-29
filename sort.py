def quick(l):
    mid = l[0]
    count = len(l)
    left = []
    right = []
    for i in range(1, count):
        if l[i] < mid:
            left.append(l[i])
        else:
            right.append(l[i])
    if len(left) > 0:
        left = quick(left)
    if len(right) > 0:
        right = quick(right)
    return left + [mid] + right


if __name__ == "__main__":
    list = [2, 21, 31, 14, 6, 11, 5, 100]
    print(quick(list))
