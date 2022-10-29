# new = "This".lower()
# print(new)

# # .upper will capitalize everything possible
# # .capitalize will capitalize the first letter
# newer = "This is a multiword String".title()
# print(newer)

# my_str = "fun"
# # my_str.title().is(title)
# print(my_str)
# print(my_str.title().istitle())

# print("1.0".isdecimal())
# # isdecimal is asking if something is a whole number. so weird...

# print("1".isdigit())

# print("la".isalpha())
# print("awoiefjoiwejf".isalpha())
# print("1a".isalpha())
# # this is only using alphabet things

# print("owiefj".isalnum())
# # alphabet things and numbers

# print("1bear".isidentifier())
# # could be the name of a variable/function, etc

# print("This is printable".isprintable())

# # this one would be false if escape an escape character was used ie. "\n"
# # anything that would cause the string to do something difference

# phrase = "this is a simple phrase"

# words = phrase.split()
# print(words)

# url = "https://example.com/users/jimmy"
# print(url.split("/"))

# phrase = "this is a simple phrase"
# words = phrase.split()
# print(", ".join(words))


# lines = ['First line', 'Second line', 'Third Line']
# output = '\n'.join(lines)
# print(output)

# template = "Hello, my name is {}, and I really enjoy {}, have a nice day"

# print(template.format('Aeriel', 'Python'))

message = input("Enter a message: ")

print("Lowercase: ", message.lower())
print("Uppercase: " ,message.upper())

words = message.split()
print(words)

sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])