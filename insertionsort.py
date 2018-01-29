def insertionSort(alist):
    for i in range(1,len(alist)): #look through the list, starting at 2nd item
        #item 0 is considered sorted
        currentvalue = alist[i] #pick the value to be compared
        position = i #make a note of the value's current position

        while position>0 and alist[position-1]>currentvalue: #run through items in list from 0 until an item greater than the current value is found
            alist[position]=alist[position-1]# copy the larger item one postion to the right
            print(alist)
            position = position-1 #back up one position
            #this section will move items in the list up to leve space for the item being compared to be slotted in

        alist[position]=currentvalue
        #drop the current value in to the correct position in the sorted part of the list
    return alist


currentList =["zebra", "mouse", "cat", "dog"]
print (currentList)
sortedList = insertionSort(currentList)
print(sortedList)
