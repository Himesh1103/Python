# prints the length of the string
name = "harry "
print(len(name))

#prints if string ends with the given string or not
print(name.endswith('rry'))
print(name.startswith('ha')) #similar with starts with or not

#for capitalizing the first letter of a string
print(name.capitalize())

#for printing the  number of occurrences of a character in a string
print(name.count('r'))

#finding a word and giving its index value
print(name.find('rry'))

#find and replace in a string
a = "parana banana"
print(a.replace('banana','nanana'))