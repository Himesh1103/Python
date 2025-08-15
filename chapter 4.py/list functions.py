list = [1,2,56,76,87,69,90] #add an element at the end of the list.
list.append(50)
print(list)

list.remove(76) #remove a certain element
print(list)

list.sort() #sort the list in ascending order.
print(list)

list.insert(5,92) #insert an element at a certain location in the list , (index value,the element)
print(list)

list.reverse() #reverse the order of the elements
print(list)

list.pop(6) #enter index number of the element you want to remove
print(list.pop(6))
print(list)

list1 = [56,72,False,True,68] #sort function does not support instances between str and int
list1.sort()
print(list1)

list2 = ['Harry', 'white', 'vanilla','Kannu','yacht','Himeeeeee'] #sorts the list in alphabetical order
list2.sort()
print(list2)

print(90 in list) #check if element is in the list or not
print(65 in list1) 

print(list[1:6:2]) #slicing same as strings and tuples