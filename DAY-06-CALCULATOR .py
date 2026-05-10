# IGL AUSBILDUNG 2028 - DAY 6
# GOAL : SAP AUSBILDUNG IN GERMANY 2028
# OROJECT : SIMPLE CALCULATOR USING FUNCTION

print("----- MY CALCULATOR -----")

# Function 1: add liya
def add(num1, num2):
    return num1 + num2 # Answer wapis bhej dega

# Function 2: subtract ka liya
def subtract(num1, num2):
    return num1 - num2

# Function 3: multiply ka liya
def multiply(num1, num2):
    return num1 * num2

# Function 4: bhaag ke liya
def divide(num1, num2):
    return num1 / num2

# User se input lo
pehla = int(input("pehla number daalaa: "))
doosra = int(input("Doosra number daal: "))
operation = input("Operation daal + - * / : ")

# Ab check karo kaunsa operation hai
if operation == "+":
    result = add(pehla, doosra) # add function chalao
    print(f"answer: {result}")
elif operation == "-":
    result = subtract(pehla, doosra)
    print(f"answer: {result}")
elif operation == "*":
    result = multiply(pehla, doosra)
    print(f"answer: {result}")
elif operation == "/":
    result = divide(pehla, doosra)
    print(f"answer: {result}")
else:
    print("GALAT OPERATION BHAI")

    print("---------- DONE ----------")
