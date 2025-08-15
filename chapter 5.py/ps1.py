'''
d = {'who':'kaun','this':'ye','there':'vaha','when':'kab'}       #q1
y = input('type the key: ')
print('Value of the key is:', d.get(y))          #returns the value of the key but if key is not found it returns none

print(d[y])             #2nd way #returns the value of the key input but in case the key is not found, it reutrns an error

s = set()                             #q2 #using range function
for i in range(0,8):
    no = int(input('enter no:'))
    s.add(no)
print(s)

s1 = set()                             #other way of range
for _ in range(8):
    no = int(input('enter no:'))
    s1.add(no)
print(s1) 


a = {18,'18'}       #q3 #yess v can have 18 as both a str type and also as an int type
print(type(a))

b = set()       #4 #when using comparison operators ,if the mumbers are same like in this 20 and 20.0, python ignores the data type and 
b.add(20)        #says them to be true
b.add(20.0)   
b.add('20')
print(len(b))

c = {}          #q5 #prints an empty dictionary
print(type(c))


e = {}                       #q6 #used the range function for repeating the input function and updating the empty dictionary
for i in range(0,4):                     #it eliminates the same keys itself
    f = input('enter the key:')
    g = input('enter the value:')
    e.update({f:g})
print(e)


e = {}                       #q6 #used the range function for repeating the input function and updating the empty dictionary
for i in range(0,4):                     #also using set as h variable so that names (f) are unique
    f = input('enter the key:')
    g = input('enter the value:')
    e.update({f:g})
    h = {f}
print(e)

#7 if names of 2 friends are same in q6 as keys then the dictionary will remove them 
#automatically and record the last input of that key occurrence

#8 if languages of 2 friends are same in q6 as values then the program will simply run without any issue as values can be same

j = {8,7,12,'harry', [1,2] }
print(type(j))  
#cannot even have a list in set and moreover cannot change the value in a list 
#in a set because sets need all of their elements to be immutable and hashable.

'''