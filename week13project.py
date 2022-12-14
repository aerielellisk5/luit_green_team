# Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:
# 1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 2. Allow the user to input the name of their department that is used in the unique name.
# 3. Generate random characters and numbers that will be included in the unique name.

# ADVANCED
# The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. Be sure to account for incorrect upper or lowercase letters in the correct department. Example: a user inputs accounting vs Accounting.

# COMPLEX
# Turn the above into a Function and execute the Function to verify it works.




# Basic
# import random
# import string
# count = 0
# list = []

# number_of_ec2_instance = int(input("How many EC2 instance would you like names for? "))
# department_for_instances = input("Which department are these instances for? ")

# while count <= (number_of_ec2_instance):
#     special_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
#     count += 1
#     list.append({special_name, department_for_instances})
    
# print(list)

# Advanced
import random
import string
count = 0
list = []

number_of_ec2_instance = int(input("How many EC2 instance would you like names for? "))
chosen_department = input("Which department are these instances for? Marketing, Accounting, or Finops? ").capitalize()

departments = ["Marketing", "Accounting", "Finops"]
# match = departments.index(chosen_department)

# print(department)

if chosen_department in departments:
    while count < (number_of_ec2_instance):
        special_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        count += 1
        list.append({special_name, chosen_department})
    print('yess')
else:
    print("nope this is wrong")
    
print(list)


#Complex

# import random
# import string
# # count = 0
# # list = []

# def build_ec2_instance(number_of_ec2_instance, chosen_department):
#     count = 0
#     list = []
#     # number_of_ec2_instance = int(input("How many EC2 instance would you like names for? "))
#     # chosen_department = (input("Which department are these instances for? Marketing, Accounting, or Finops? ")).capitalize()
#     number_of_ec2_instance = number_of_ec2_instance
#     chosen_department = chosen_department.capitalize()
#     departments = ["Marketing", "Accounting", "Finops"]
#     # departments = ["Marketing", "Accounting", "Finops"]
#     match = departments.index(chosen_department)
    
#     if chosen_department in departments:
#         while count < (number_of_ec2_instance):
#             special_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
#             count += 1
#             list.append({special_name, chosen_department})
#     else:
#         print("nope this is wrong")
#     print(list)
    
    


# # build_ec2_instance(2, "finops")
# build_ec2_instance(5, "wejfoiwejfoajfj")
# build_ec2_instance(9, "Marketing")

# for department in departments:
#     print(department)
#     print(chosen_department)
    
#     if chosen_department == department:
#         print("We made it!")
#     else:
#         print("this is not the right department!")
        
        






# >>> import string
# >>> import random
# >>> def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
# ...    return ''.join(random.choice(chars) for _ in range(size))
# ...
# >>> id_generator()
# 'G5G74W'
# >>> id_generator(3, "6793YUIO")
# 'Y3U'