import sys
import random as r

size = 50


def binarySearch(a, val, min, max):
    mid = int((min + max) / 2)
    if min > max:
        return -1
    if val == a[mid]:
        return mid
    else:
        if val > a[mid]:
            return binarySearch(a, val, mid + 1, max)
        return binarySearch(a, val, min, mid - 1)


def main():
    l = [size]
    for i in range(size):
        l.append(i)
    ran = r.randint(0, size)
    foundindex = binarySearch(l, ran, 0, len(l) - 1)
    print("found index " + str(foundindex) + " ran:" + str(ran))


if __name__ == "__main__":
    main()
