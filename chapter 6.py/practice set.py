'''
list = []                                       #q1 #alternative way of finding the greatest
for i in range(0,4):                   
    a = int(input('enter the number:'))  
    list.append(a)
    list.sort()
print(list[3])

b = int(input('enter the number:'))            #q1 #2nd way forfinding the greatest using if elif else
c = int(input('enter the number:'))
d = int(input('enter the number:'))
e = int(input('enter the number:'))

if(b>c and b>d and b>e):
    print('b is the greatest',b)

elif(c>b and c>d and c>e):
    print('c is the greatest',c)

elif(d>c and d>b and d>e):
    print('d is the greatest',d)

elif(e>c and e>d and e>b):
    print('e is the greatest',e)


number = [int(input('enter the numbers:')) for i in range(4)]       #q1 #shortest code for max number out of multiple input numbers
print('max number:',max(number))


f = int(input('enter marks of subject a:'))         #q2 #works in case of only when percentage of marks are already given
g = int(input('enter marks of subject b:'))
h = int(input('enter marks of subject c:'))

if(f>=33 and g>=33 and h>=33 and ((f+g+h)/3)>=40):
    print('pass')

else:
    print('fail')


q = [int(input('whts the number')) for i in range(0,3)]      #q2 #works when v have to calculate the percentage of marks as well
r = [int(input('total')) for i in range(0,3)]
if  (q[0]*100/r[0]>=33 and q[1]*100/r[1]>=33 and q[2]*100/r[2]>=33 and sum(q)*100/sum(r) >=40 ):
    print('yes,pass')
else:
    print('fail')


    
i = input('type the comment:')         #q3 #doesnt work as a phrase in a keyword, it works only in exactly equal condition
j = i.lower()
if(i=='make a lot of money' or i=='buy now' or i=='subscribe this' or i=='click this'):
    print('spam')

else:
    print('not spam')

i = input('type the comment:')         #q3 #works when the keyword is in a line also
j = i.lower()
if 'make a lot of money' in j:
    print('spam!')
else:
    print('safe')

username = input('enter the username:')     #q4
no = len(username)
if 0<no<10: #& no!=0:
    print('username contains less than 10 characters')
elif no==0:
    print('username cannot be empty')
elif no>10 :
    print('username contains more than 10 characters')

list = ['k','l','m','n']                    #q5
name = input('enter the name:')
if name in list:
    print('name is present in the list')
else:
    print('name is not present in the list')

marks = int(input('enter the marks:'))        #q6
if 90<=marks<=100:
    print('excellent')
elif 80<=marks<90:
    print('A')
elif 70<=marks<80:
    print('B')
elif 60<=marks<70:
    print('C')
elif 50<=marks<60:
    print('D')
elif marks<50:
    print('F')

post = input('enter the post content:')           #q7
if 'Harry'.lower() in post.lower():
    print('yes the post is talking about harry')
else:
    print('the post is not talking about harry')
'''