array = [10, 3, 123, 7, 3, 2, 5, 6, 7]

swapped = True
while swapped:
    swapped = False
    i = 0
    for e in array:
        i += 1
        if i < len(array):
            if array[i] < e:
                array[i - 1] = array[i]
                array[i] = e
                swapped = True

print(array)
