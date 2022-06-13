import random 

def password_gen(length):
    password = []
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_10 = "0123456789"
    symbols = "!@#$%&"
    characters = list(lowercase_letters + uppercase_letters + numbers_10 + symbols)
    random.shuffle(characters)
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
    