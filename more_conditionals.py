# #While Loops
# count = 1

# while count <= 4:
#     print("looping")
#     count += 1


# Forloops

# colors = ['blue', 'green', 'red', 'purple']

# for color in colors:
#     print(color)
    
# point = (1, 2, 3)

# for value in point:
#     print value
    
# ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
# # for key in ages:
# #     print(key)

# for key, value in ages.items():
#     print (key, value)

# for letter in 'my_string':
#     print(letter)


# counter = 1
# while counter <= 25:
#     if counter % 4 == 0:
#         print(counter)
#     counter += 1

# count = 1

# while count < 10:
#     if count % 2 == 0:
#         count+= 1
#         continue
#     print(f"We're counting odd numbers: {count}")
#     count += 1
    

# while count < 10:
#     if count % 2 == 0:
#         break
#     print(f"We're counting odd numbers: {count}")
#     count += 1

# colors = ['blue', 'green', 'red', 'purple']
 
# for color in colors:
#     if color == 'blue':
#         continue
#     elif color == 'red':
#         break
#     print(color)


# count = 1

# while count <= 4:
#     print (count)
#     count +=1
# else:
#     print("While loop is completed")
    
# for i in [1,2,3,4,5]:
#     print(i)
# else: 
#     print("Foor Loop Completed")
    
# colors = ['red', 'pink', 'blue', 'orange', 'green']

# for color in colors:
#     if color == 'orange':
#         print("Orange is in the list")
#         break
# else:
#         print("Orange is not in the list")
        
#  super helpful for search and using BREAK in the other clause


# my_range = range(10)
# # print(my_range)

# print(list(my_range))

# print(list(range(1, 14, 2)))

# count = 1

# # while count <= 4:
# #     print("looping")
# #     count += 1
    
    
# for _ in range(4):
#     print("looping")

# colors = ['red', 'blue', 'orange', 'green', 'yellow']
# uppercase_color = []

# for color in colors:
#     uppercase_color.append(color.upper())
    
# print(uppercase_color)
# uppercase_color = []
# colors = ['red', 'blue', 'orange', 'green', 'yellow']
# # uppercase_color = [color.upper() for color in colors]
# # print(uppercase_color)

# warm_colors=[]

# for color in colors:
#     if color in ['red', 'orange', 'yellow']:
#         warm_colors.append(color)
        
# print(warm_colors)

upper_number = int(input("How many values should we process? " ))

for number in range(1,upper_number + 1):
    pass
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
    

