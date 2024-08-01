import random 
def create_password(pass_lenght):
    elements="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password=""
    for i in range(pass_lenght):
        password+=random.choice(elements)
    print(password)
create_password(17)
