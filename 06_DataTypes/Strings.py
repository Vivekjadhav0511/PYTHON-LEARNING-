# In Python, strings are a sequence of characters enclosed in either single quotes (') or double quotes ("). 

# Strings in Python are immutable, meaning their content cannot be changed after creation. Operations like replace or slicing return a new string instead of modifying the original.

string = "vivekJadhav    " # Unicode string 
print(string)

# String Methods 

first_char = string[0]
print(first_char)

sliceString = string[5:]
sliceString = string[0:5]
print(sliceString)

print(string.lower() , "lenght Of String" , len(string))  # vivekjadhav     15
print(string.upper())  # VIVEKJADHAV
print(string.strip())  # VIVEKJADHAV 

lenghtOfStringAfterStrip = (string.strip()) 
print("lenght Of String After Strip :- " , len(lenghtOfStringAfterStrip)) # lenght Of String After Strip :-  11

strOne = "vivek"
strOne = "jadhav"
print(strOne)

num_string = "0123456789"
print(num_string[:])
print(num_string[2:])
print(num_string[0:7])
print(num_string[0:7:2]) # 3rd Parameter Hoping
print(num_string[-2]) 


subject = 'python Programming '
print(subject) # python Programming
print(subject.replace('python' , "Java")) # Java Programming
print(subject) # Java Programming String a immutable original value dosen't change 

courses = "DSA, python , ADBMS , SEPM , Business Statestic , DSA"
print(courses.split(" ")) # ['DSA', ',', 'Python', ',', 'ADBMS', ',', 'SEPM', ',', 'Business', 'Statestic']
print(courses.split(",")) # ['DSA ', ' Python ', ' ADBMS ', ' SEPM ', ' Business Statestic']

print(courses.find("python")) # 5
print(courses.count("DSA")) # 2

player = "Rohit sharma"
score = 100
finalCall = "indian player {} score {} in just 10 overs"
print(finalCall.format(player,score)) # indian player Rohit sharma score 100 in just 10 overs

print(f"indian Player {player} Score a {score}") # indian Player Rohit sharma Score a 100


# ******** LIST TO STRING *********

coursesList = ['DSA', 'python' , 'ADBMS' , 'SEPM' , 'Business Statestic']
print(" ".join(coursesList)) # DSA python ADBMS SEPM Business Statestic

# ******** LOOP *************
username = "  vivekjadhav@gmail.com   "
letterAfterStrip = username.strip()
for letter in letterAfterStrip:
    print(letter)


finalScore = "indian player \"Rohit sharma\" score 100 in just 10 overs"
print(finalScore) # indian player "Rohit sharma" score 100 in just 10 overs

studentName = "vivek\njadhav"
print(studentName) 

drive = r"c::\user\python\program"  #RawString
print(drive) # c::\user\python\program

# ****** String Contating Questions ****** 

questions = "question is avalible"
print('question' in questions)  # True 





