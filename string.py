username = input("enter a username: ")

username.isalpha

if len(username) > 12:
    print("tooo long")
elif not username.find("  ") == -1:
    print("no spaces")
elif not username.isalpha():
    print("no digits")
else:
    print(f"welcome {username}")
