name= "hitanshi"

print("original=",name)
print("upper=",name.upper())
print("lower=",name.lower())
print("length=",len(name))
print("find=",name.find("shi"))
print("replace=",name.replace("hit","mit"))
print("slice=",name[0:3])

age = 21
print(f"my name is {name}.and i am {age} year old.")



# Problem 1 solution

print("---------clean and formar a name--------")
raw_name = "  hITAnsHI  AaSNani  "

# Clean name
clean_name = raw_name.strip().title()

# Total characters (without spaces)
total_chars = len(clean_name.replace(" ", ""))

# First name
first_name = clean_name.split()[0]

# Reversed name
reversed_name = clean_name[::-1]

print("Cleaned name=", clean_name)
print("Total chars =", total_chars)
print("First name  =", first_name)
print("Reversed    =", reversed_name)

# Problem 2 solution
print("------username generator-------")
fullname= "Hitanshi Aasnani"
parts = fullname.split()

username = parts[0].lower() + parts[1].lower() + str(len(fullname.replace(" "," ")))

print("username=",username)


# Problem 3 solution
print("--------Sentence Analyser-------")

sentence = "I Love Python Programming"

print("Sentence:", sentence)
print("Total Characters:", len(sentence))
print("Total Words:", len(sentence.split()))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("First Word:", sentence.split()[0])
print("Reversed:", sentence[::-1])
