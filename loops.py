#  Sum of Numbers from 1 to 10 in python 

num = int(input(" enter the Number : "))
ans = 0
for i in range(1,num+1):
    ans += i

print(f"Sum is : {ans}")
    #  Print each letter of a String 
    
string = " nikhilJain"
for i in range(0, len(string)):
    
 print(string[i])
 
#  Write a Python Program to Reverse  a Number 

digit = int(input(" Enter Digit :  "))
ans = 0
while digit:
    ans = ans * 10 + (digit % 10)
    digit = digit // 10

print(f" The Reverse of digit is {ans}")


#  WHILE LOOP IN PYTHON
i=1
while i<=11:
    print(i)
    i = i+1
    
    #  Printing tables using While Loop
data = int(input(" Enter a Data :  "))
p = 1
while(p<=10):
        print(f"{data} X {p} = {data*p}")
        p = p+1

#  WHILE TRUE LOOP 

while True:
    a = int(input(" Enter a Number a : "))
    b = int(input(" Enter a Number b : "))
    print(f" Sum of {a} and {b} is : {a+b}")
    print("                                 ")
    print(" Do you want to stop the Execution ")
    choice = input("Enter Yes or no : ")
    if(choice == "yes"):
        break

#  NESTED LOOPS 

for i in range (1,6):
    for j in range (1,i+1):
     print(j , end=" ")
    print()
        


