marks = []
f1 = int(input('enter marks here:'))
marks.append(f1)
f2 = int(input('enter marks here:'))
marks.append(f2)
f3 = int(input('enter marks here:'))
marks.append(f3)
f4 = int(input('enter marks here:'))
marks.append(f4)
f5 = int(input('enter marks here:'))
marks.append(f5)
f6 = int(input('enter marks here:'))
marks.append(f6)

marks.sort()

print(marks)



a = input('Enter marks:') 
b = input('Enter marks:')
c = input('Enter marks:')
d = input('Enter marks:')
e = input('Enter marks:')
f = input('Enter marks:')
marks=[a,b,c,d,e,f]
marks.sort()
print(marks)



marks = []                            #using range function to save code n time n all
for i in range(0,6):
    x = int(input('enter marks:'))
    marks.append(x)
    marks.sort()
print(marks) 


marks = []                            #a different type of range function 
for _ in range(6):
    x = int(input('enter marks:'))
    marks.append(x)
    marks.sort()
print(marks) 