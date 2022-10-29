# a = 4
# b = 3
# c = 2
# d = 10
# # if a > b:
# #     print(a)
    
# # if False:
# #     print("Was true")



# var = 100
# if var == 200:
#   print("1 - Got a true expression value")
#   print(var)
# elif var == 150:
#   print("2 - Got a true expression value")
#   print(var)
# elif var == 100:
#   print("3 - Got a true expression value")
#   print(var)
# else:
#   print("4 - Got a false expression value")
#   print(var)

# print("Good bye!")
# name = input("What is your name? ")

# if len(name) >= 6:
#     print("You name is long")
# elif len(name) == 5:
#     print("Your name is 5 characters")
# elif len(name) >= 4:
#     print("Your name is 4 or more characters")
# else:
#     print("Your name is short")

#Take a single number, and process what happens in the fizzbuzz problem

value = int(input("Enter an interger value: "))

if value % 5 == 0 and value % 3 == 0:
    print("Fizzbuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)