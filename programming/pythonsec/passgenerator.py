
import secrets
import string

Min_length = 8
Max_length = 16

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbol = "!@#$&*?/:;\\|)(%^<>,.`~=+-_"

print("It should contain at least 1 uppercase, 1 lowercase, 1 number, and 1 special character(@ ! # () , . ? $ % ^ & * - _ + = ~ ` | : ; < > / \\)")


while True:

   try:
      length = int(input("Enter the length of the password: "))
      
   except ValueError:  
      print("Should only contain numbers (0 - 9)")
      
   else:  
      if Min_length <= length <=Max_length:
         break
      print("Should only contain characters between 8 to 16")
         
chars = [secrets.choice(group) for group in (lowercase , uppercase , digits, symbol)]
all_chars = lowercase + uppercase + digits + symbol
chars += [secrets.choice(all_chars) for _ in range(length - len(chars)) ]

secrets.SystemRandom().shuffle(chars)

password = "".join(chars)
print ("The generated password is :" , password)




                                                     