#  Print The Multiples of 8 and 12 Between Numbers Range  to 100
for num in range(1,101):
    if(num % 8 == 0 and num % 12 == 0):
        print(num, end=" ")
    else:
        continue
    
    #  Break Statement 
    
start = 1
while(start<=11):
    if(start == 5):
        print(start)
        print("Add This song to My favourit playlist ")
    start  = start + 1
    
    #   Problems Based on Loops 
strt = 1
sum = 0
for i in range(strt , 51):
    if(i%2==0):
        sum = sum + i
    
        
print(f"The Sum of Value is : {sum}")
        
string = "Why fit in , When you are Born to Stand Out "
#  Length of the String 
print(f" Length of the String is : {len(string)}")

#  Check how many Times 'o' is Occuring 
count = 0
for i in range(0 , len(string)):
    if('o' or 'O' == string[i]):
        count = count + 1
        
print(count)

        
    
   
        
    
        
            