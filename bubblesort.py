def my_bubble_sort(someList):#funtion with list as a prameter
    swapped = True
    while swapped == True: #check if a swap has been made, if true repeat
        swapped = False #reset swapped value to false
        for i in range(len(someList)-1): #iterate over list until one from the end
            if someList[i] > someList[i+1]:#the greater sign will sort in ascending order
                temp = someList[i] #store the value to be replaced in a temporary variable
                someList[i] = someList[i+1] #swap the value to the right with the current value
                someList[i + 1] = temp #replace value on right with temp value
                print(someList)# print to watch the values moving - optional
                swapped = True #a swap has been made so set to true
    return someList

currentList =["zebra", "mouse", "cat", "dog"]
print (currentList)
sortedList = my_bubble_sort(currentList)
