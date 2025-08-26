num1=float(input("son-1:"))
num2=float(input("son-2:"))
operator=input("amal: ")

if operator== "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2) 
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    if num2 !=0:
        print(num1/num2)
    else:
        print("nolga bo'lib bo'lmaydi") 
else:
    print(f"xato amal: {operator}")                     