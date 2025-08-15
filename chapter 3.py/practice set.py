a = input("Enter the name:")
print("Good Afternoon", a.capitalize())

#using f thing
print(f"Good Afternoon {a}")

#replacing multiple or known as chaining
letter = '''Dear <|Name|> ,
You are selected!
<|Date|> '''
print(letter.replace('<|Name|>' , 'Harry').replace('<|Date|>' , '11 March 2006'))

#detect double spacing
b = 'are  saaleeee tu  jare'
print(b.find("  ")) 
print(b.replace('  ' , ' '))
print(b) 
'''string are immutable ,meaning that the string remains the same originally but when we use replacing function, 
new string is created '''

letter = "Dear Harry, \n\tThis python course is nice.\nThanks!"
print(letter)