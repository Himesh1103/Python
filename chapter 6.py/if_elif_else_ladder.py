a = int(input('Enter your age:'))
if (a>=25):                                  #the if condition is checked first ,if its true then else condition is skipped
    print('You meet the age requirements')    #and it does not check for else condition n skips to the next code
    print('you may proceed to enter')        #and when if condition is not met it checks the else condition

elif(a<0):
    print('you have entered an invalid negative age')

elif(a==0):
    print('this is an invalid age as age cannot be zero')

else:
    print('you do not meet the age requirements so you cannot enter')

print('thanku for joining')               #this is called if elif else ladder