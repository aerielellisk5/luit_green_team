import random

var_dict = {}

# print(var_dict)
print(type(var_dict))

var_dict['color']= 'red'
var_dict['color']= '386'


key_name = 'fruit'

var_dict[key_name] = 'cranberry'

print(var_dict)

var_dict[key_name] = ['apple', 'cranberr', 'vodka']

print(var_dict)

# for i in range(0,10):
#     var_dict[chr(i)] = [random.randint(0,10000) for j in range(0,10)]
    
print(var_dict.keys())

print(var_dict.values())

print(dir(var_dict))

for k, v in var_dict.items():
    print(k, v)