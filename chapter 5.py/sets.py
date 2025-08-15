s = set() #empty set
print(s)
 
s1 = {12,76,98,34,23,55,34}        #set shows the unique values only and none element repeats #set uses curly brackets #set doesnt sort
print(s1)                                          #for sorting u will have to use list                                           

s2 = {1,87,4,45,3,2,1,'whotf','whyyyy','whotf'} #set can have mupltiple datatypes 
print(s2,type(s2))

s2.add(34)          #takes only one value at a time for addition into set
print(s2,type(s))

w = len(s2) #gives the length of the set
print(w) 

print(s2.remove(87),s2) # removes a certain element from the set

print(s2.pop(),s2) #removes a random element from the set

s1.clear() #clears the set
print(s1)

s3 = {2,43,23,1,2,5,6,5,76,54} #prints the new set with items from both sets
print(s2.union(s3))

print(s2.intersection(s3)) #prints a set with only the common elements from both sets

print({43,23,5}.issubset(s3)) #checks if its a subset of the set or not 

print((s3).issuperset({43,76,51})) #checks if its a superset of the set or not