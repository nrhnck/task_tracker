name = input("enter your name")

while name == "":
    print("You did not enter your name")
    name = input("enter your name")
print(f"Hello {name}")


age = input("how old are you?")

while age == "":
    print("how old r u")
    age = input("enter your age")
print(f"hello you are {age} years old")


num = int(input("Enter a # between 1 and 10:"))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 and 10:"))

print(f"Your number is {num}")