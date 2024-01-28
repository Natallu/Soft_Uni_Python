username = input()
user_password = input()

password = input()
while password != user_password:
    password = input()
if password == user_password:
    print(f"Welcome {username}!")
