class User:
    def __init__(self, user_id, username):
        self.id= user_id
        self.username=username
        self.follwer=0

u_id=input("ENter ID: ")
u_name=input("Enter Name: ")

user_1 = User(u_id, u_name)
print(user_1.id)
print(user_1.username)
print(user_1.follwer)