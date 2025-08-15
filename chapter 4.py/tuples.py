tuple = (2,87,True,'bhppppp')
tuple[2] = 90

a =(0,1,6,98,69,'halaluya','falana','dhingda',98,True,False) 
d = (2,4,6,45,34,23,'foooooooooooo','hoooooooo',False)
print(type(a))

b = a.index(98)
print(b)

c = a.count(1) #in case of counting the number of occurrences of 0 and 1 the true and false are also counted, true as 1 and false as 0.
print(c)

print(len(a)) #total length

print(a*3) #can be multiplied

print(a+d) #tuples can be added 

print(54 in a) #checking if that element is in the tuple or not 

print(a[3:6]) #slicing same as strings and lists

print(a[1:7:2]) #slicing