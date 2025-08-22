name =input ("Input your name: ")
try:
    age=int(input("Input your age"))
    print (f"Your age:{age}")
except ValueError:
    print("Enter a number!")    
    
age=int(age)
if age <= 18:
    print (f"Youre still too young {name}")
elif age>=18:
    print (f"Welcome {name}")
    
input()