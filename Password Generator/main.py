import random
import string 

pass1 = string.ascii_letters + string.digits + string.hexdigits + string.punctuation


password = "".join(random.sample(pass1,15))

print("Your Generated Password is: " +password)