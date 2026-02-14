'''name = input("whats your name? ")
print("hello," + name)
# writing it with the plus sign gives no space, and u will have to add spaces manually

name = input("whats your name? ")
print("hello,",name)'''
#automatically gives spaces when writing it using comma sign
#it dint happen automatically, it happened because of the built in parameters of the print function

'''print(*objects, sep=' ', end='\n',file=None, flush=False)
this is the print fucntion's parameters'''

'''name = input('whats your name? ')
print("hello,", name, sep='', end='')
print(name)'''
# u can override the parameters of a function this way, i did sep with no space so there was no space and same with the end one of \n.
# u can also add anything in the quotes of sep and end n it will influence the function for you.

name = input('whats your name? ').strip().title()
print(f'Hello,{name}')
print("Hello,\'name\'")
first, middle, last= name.split(' ')
print('hello,',first)
print('hello,',last)
print('hello,',middle)
#can link multiple string methods in the input line but not too many the code will look bad.
#print f is for format string when name variable is within the string quotes.
#can use without f string by typing \' \' at the start and end of the variable name.