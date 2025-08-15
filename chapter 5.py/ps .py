translator = {

    "mad":"pagal",
    "proud":"garv",
    "donkey":"gadheda"
}

a = input("enter the key:")
print("the value is :" ,translator.get(a))

#q2
#a = set(input('number') for _ in range(8))
#print(a)

a = set(int(input('number'))for _ in range(8))
print(a)
