array = [10, 3, 123, 7, 3, 2, 5, 6, 7]

i = 1
while i < len(array):
    j = i
    while j > 0 and array[j - 1] > array[j]:
        temp = array[j - 1]
        array[j - 1] = array[j]
        array[j] = temp
    i += 1

print(array)
