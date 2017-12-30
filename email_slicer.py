# get user email address
email = input("Enter your email address").strip()

# slice out user name
user_name = email[:email.index("@")]
#slice domain name
domain_name = email[email.index("@")+1:]
# format message
message = "Your Username is {} and Domain name is {}".format(user_name, domain_name)
# display out message
print(message)