# Ask user for name
name = input("what is your name?: ")

# Ask user for there age
age = input("How old are you?: ")


# Ask user for city
city = input("Where do you live?: ")

# Ask user what they enjoy
love = input("What do you enjoy doing?: ")

# Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output_string = string.format(name, age, city, love)
# Print output to screen
print("All about you:")
print(output_string)
