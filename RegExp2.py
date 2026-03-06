#Email Extractor
import re
text = "Contact us at abhi@gmail.com or admin@yahoo.com"
emails = re.findall(r"\w+@\w+\.\w+",text)
print("email found,",emails)

#Phone numbre validator 
import re
number = "9568423355"
pattern ="[6-9]\d{9}"
if re.match(pattern,number):
    print("valid number")
else: 
    print("invalid number")

#password validator
import re
password = "Nishi6"
pattern ="[A-Za-z0-9]{6,}"
if re.match(pattern,password):
    print("Correct password")
else:
    print("Incorrect password")

#Extract numbers from Text
import re
text = "the price is 500 , the discount is 50 rupees"
numbers = re.findall(r"\d+",text)
print("Numbers:",numbers)

#Start and end of string
import re
text = "python is easy"
result = re.findall(r"^python",text)
last=re.findall(r"python$",text)
print(result)
print(last)

#Validate extract word
import re
text = "Python"
result = re.findall(r"^Python$",text)
print(result)

