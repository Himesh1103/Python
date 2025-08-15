'''
x = int(input('enter the number'))  #q1
for i in range(1,11):
    print(x,'*',i ,'=', x*i)

x = int(input('enter the number:'))    #q1 while loop
i = 1
while (i<11):
    print(x*i)
    i+=1

b = ['harry','sam','saibi','vansh']       #q2
for x in range(0,4):
    while b[x][0] == 's':
        print (b[x])
        break

a = int(input('enter the number'))     #q4
if all(a%i != 0 for i in range(2,a)):
    print('no. is prime')
else:
    print('not')

a = int(input('enter the number:'))

sum = 0            #q5
i = 1
while (i<=a):
    i+=1
    sum+=i
print(sum)

a = int(input('enter the number:'))       #q6
i = 0
f = 1
while(i<a):
    i+=1
    f*=i
print(f)

x = int(input('enter the number'))  #q10
for i in range(1,11):
    print(x,'*',11-i ,'=', x*(11-i))

for x in range (1,4):      #q8
    print('*' * x)

a = 1
for i in range (1,4):      
    print('*' * (a))
    a+=2

a = 1         #q7
b = 2
for i in range (1,4):
    print(' '*b, '*'*(a))
    a+=2
    b-=1

print('***')
print('* *')
print('***')
'''