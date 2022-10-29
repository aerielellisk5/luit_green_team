print("hello")
# Set emails as an empty dictionar
emails = {}

#add a bunch of people
emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'

print(emails)

#remove Craig

del emails['craig']

print(emails)

# add dalton

emails['dalton'] = 'dalton@example.com'

print(emails)
# Return a list of keys from the emails dictions as 'users'

users = list(emails.keys())
print(users)
# Return a list of values from the mails dictionary as 'email_list'

email_list = list(emails.values())
print(email_list)

# Return a list of tuples called 'pairs' representing the key/value pairs in 'emails'

pairs = list(emails.items())
print(pairs)
