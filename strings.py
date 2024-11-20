# Concatenation in Strings 
a = "Nikhil"
b = "Jain"
print(a + " " + b)

#  String Indexing 
string = "I am A good boy "
i = 0
while(i<len(string)):
    print(string[i], end=" ")
    i = i+1
    
print(""" """) # For Next Line Movement 

    # String Slicings 
string_new = "RoopChandJain"
print(f"String Slicing is {string_new[0:6]}")
print(f"String New Type Slicing is : {string_new[:8]}")

# Strigns Some More Functions 
str_new = "Nikhil Jain is a Good Boy Nikhil always used to go college and he is so gentle and polite he is eats fruits daily and go to college daily"
#  Length of String 
print(f" Length of String is : {len(str_new)}")
# Find Occurence in String 
print(str_new.count("college"))
print("""  """)
print(str_new.count("Nikhil"))
print("""  """)
print(str_new.count("is"))

print(" The Indexing of it is : " , str_new.find("is")) # return Indexing 

print(str_new.replace("Nikhil", "Kamal"))

print(str_new.upper())

