# Create a list of services using Python. IE: S3, Lambda, EC2, etc

# The list should be empty initially.
services = []

# Populate the list using append or insert.
services.append("EC2")
services.append("AWS Lambda")
services.append("AWS Gateway")
services.append("Code Pipeline")
services.append("Cloud9")
services.append("AWS Elastic Beanstalk")
print(services)

# Print the list and the length of the list.
print(len(services))

# Remove two specific services from the list by name or by index.
del services[0]
del services[3]


# Print the new list and the new length of the list.
print(services)
print(len(services))



