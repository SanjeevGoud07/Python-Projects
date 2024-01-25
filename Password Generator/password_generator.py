import random
# s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
samp="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@"
pass_len = int(input("Enter The Length Of Password: "))
print(" ")
password_new = "".join(random.sample(samp,pass_len))
print("Your Password is: ")
print(password_new)
