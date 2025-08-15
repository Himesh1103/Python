#dictionaries are mutable
a = {
    'marks':100,       #keys:values
    'himee':'snowww',
    'hulk':'green' ,
    50:53
 }
print(len(a))

print(a.keys())

print(a.values())

print(a.items())

a.update({'friends':'gawar', 'hulk':'red'})
print(a)

print(a.get('himeee')) #returns none
#print(a['himeee']) #returns an error

value = a.pop(50) #remove the key value pair entered by entering the key in pop bracket()
print(value)
print(a)

print(a.popitem())
print(a)
