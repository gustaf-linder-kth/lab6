import math
import timeit

# Logik från pseudocode en.wikipedia.org/wiki/Quicksort
def quicksort(data, low, high):
    
    # Kontroll att index är i rätt ordning
    if low >= high or low < 0:
        return
    
    # Partitionera datan och få pivot index
    p = partition(data, low, high)

    # Sortera de två partitionerna
    quicksort(data, low, p)
    quicksort(data, p+1, high)

def partition(data, low, high):
    # Välj mittersta element som pivot
    pivot = data[math.floor((high+ low)/2)]

    i = low-1
    j= high+1

    while True:
        i= i+1
        while data[i] < pivot:
            i = i+1
        
        j = j-1
        while data[j] > pivot:
            j=j-1
        
        if i>= j:
            return j

        data[i], data[j] = data[j], data[i]

def bubble_sort(data):
    while True:
        swaps = 0
        for i in range(0,len(data)- 1):
            if data[i] > data[i+1]:
                data[i+1], data[i] = data[i], data[i+1]
                swaps +=1
        if swaps == 0:
            return data
        
# This function test the runtime of qsort and bubble sort
# of a list of data until the n:th element.
def sorting_test(data, n):
    spliced_data = data[0:n]
    
    qsort_time = timeit.timeit(stmt = lambda: quicksort(spliced_data, 0, len(spliced_data)- 1), number=1)

    #restore spliced_data
    spliced_data = data[0:n]

    bubble_time = timeit.timeit(stmt=lambda: bubble_sort(spliced_data), number=1)

    print("Qsort:", qsort_time, "seconds")
    print("Bubble sort:", bubble_time, "seconds")
