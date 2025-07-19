#امیرحسین مطیع
from random import randint
from time import time
import matplotlib.pyplot as plt
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        i,j,k = 0,0,0
        mergeSort(left)
        mergeSort(right)

        while len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1

            k += 1

        while len(left) > i:
            array[k] = left[i]
            i += 1
            k += 1

        while len(right) > j:
            array[k] = right[j]
            j += 1
            k += 1
    return array

def fancyPivot(array, k):
    if len(array) <= 50:
        array = mergeSort(array)
        return array[k-1]
    sublists = []
    medians = []
    for i in range(0, len(array), 5):
        if i + 5 < len(array):
            sublists.append(array[i: i + 5])
            i += 5
        else:
            sublists.append(array[i:])
    for sub in sublists:
        sub = sorted(sub)[len(sub)// 2]
        medians.append(sub)
    if len(medians) <= 5:
        pivot = [len(medians)//2]
    else:
        pivot = fancyPivot(medians, len(medians)//2)
    left = []
    right = []
    for n in range(len(array)):
        if n < pivot:
            left.append(n)
        elif pivot < n:
            right.append(n)
        if n == pivot:
            continue
    if len(left) == k - 1:
            return pivot
    elif len(left) > k - 1:
        return fancyPivot(left, k)
    elif len(left) < k - 1:
        return fancyPivot(right, k - len(left) - 1)

def randomPivot(array, k):
    if len(array) <= 50:
        array = mergeSort(array)
        return array[k-1]
    index = randint(0, len(array) - 1)
    pivot = array[index]
    left = []
    right = []
    for n in range(len(array)):
        if n == pivot:
            continue
        if n <= pivot:
            left.append(n)
        elif pivot < n:
            right.append(n)
    if len(left) == k - 1:
            return pivot
    elif len(left) > k - 1:
        return randomPivot(left, k)
    elif len(left) < k - 1:
        return randomPivot(right, k - len(left) - 1)


fancyTimes = []
randomTimes = []
mergeTimes = []
for size in range(2000,5000,100):
    array = [randint(1,5000) for n in range(size)]
    print(array)

plt.plot(range(2000,5000,100), fancyTimes,":", color="red", label="Fancy select")
plt.plot(range(2000,5000,100), randomTimes,"-.", color="green", label="Random select")
plt.plot(range(2000,5000,100), mergeTimes,"-", color="blue", label="MergeSort select")
plt.xlabel('Array Size')
plt.ylabel('Time(ms)')
plt.legend()
plt.title("Selection")
plt.show()









