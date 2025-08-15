a = int(input('enter your age:'))
if(a>=18):
    print('yes')

else:
    print('no')

b = int(input('Enter your age:'))

#if statement no 1

if(b*2>0):                    #if statements can be multiple so therefore v have to allign the if statement with the ladder
    print('wowwwwwwwwwwww')   #and similarly separate the independent if statement to be run separately n individually

#if statement no 2

if (b>=25):                                  #the if condition is checked first ,if its true then else condition is skipped
    print('You meet the age requirements')    #and it does not check for else condition n skips to the next code
    print('you may proceed to enter')        #and when if condition is not met it checks the else condition

elif(b<0):
    print('you have entered an invalid negative age')

elif(b==0):
    print('this is an invalid age as age cannot be zero')

else:
    print('you do not meet the age requirements so you cannot enter')

print('thanku for joining')