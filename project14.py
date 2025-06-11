import random  
print("Starting password generator...")

characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password_length = int(input("Enter desired password length: "))

password = []
for i in range(password_length):
    
    password.append(random.choice(characters))
password = ''.join(password)
print("Your new password is:"+password)