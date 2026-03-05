import re
text = "python is powerful"
result = re.search("powerful",text)
if result :
    print("Match found")
else:
    print("Match not found")

#Finding digits in a string
import re
text = "My Rollno is 2541"
results=re.findall("\d+",text)
print(results)

#Finding all words
import re
text="My Name is Nick"
result=re.findall("\w+",text)
print(result)

#checking email pattern
import re
email="student@gmail.com"
pattern="\w+@\w+\.\w+"

if re.match(pattern,email):
    print("valid email")
else:
    print("Invalid email")

#Replace words
import re
text = "I like Java"
new_text =re.sub("Java","Python",text)
print(new_text)

#Split using regex
import re
text ="apple,banana;Mango Orange"
result = re.split("[,; ]",text)
print(result)

import re
text = "hello python"
print(re.match("python",text))
print(re.search("python",text))

#Validate phone number
import re
number = "9562384125"
if re.match(r"[6-9]\d{9}",number):
    print("valid phone number")
else:
    print("invalid phone number")

#extracting digits from text
import re
text = " my roll no is 21 before it was 49"
numbers = re.findall(r"\d+",text)
print(numbers)
#Find all lower cases
import re
text = "python programming"
result = re.findall(r"[a-z]",text)
print(result)
#Count vowels
import re
text ="Authentication"
result = re.findall(r"[aeiouAEIOU]",text)
print("Vowels:",result)
print("count",len(result))

#Findineg words starting with capital letters
import re
text = "Python Is Easy To Learn"
result = re.findall(r"[A-Z][a-z]*", text)
print(result)
#Removes Special letters
import re
text = "Hello@#$ Python !! 1234"
result = re.sub(r"[^a-zA-Z0-9]"," ",text)
print(result)
#Find repeated words
import re
text="aabbbhsujddffs"
result = re.findall(r"(.)\1+",text)
print(result)