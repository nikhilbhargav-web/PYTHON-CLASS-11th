# IGL AUSBILDUNG 2028 - DAY 5
# GOAL: SAP AUSBILDUNG IN GERMANY 2028
# PROJECT: NUMBER GUESSING GAME

import random

print("----- IGL NUMBER GUESSING GAME -----")
print("main 1 se 100 tak ek number soch rha hu...")

#computer secret no. choose karega
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nApna guess daal bhai: "))
    attempts = attempts + 1 
    
    if guess < secret_number:
        print("BHAI AUR BADA NUMBER SOCHO")
    elif guess > secret_number:
        print("BHAI THODA CHOTA NUMBER SOCHO")
    else:
        print(f"BOOM! SAHI PAKDA")
        print(f"SECRET NUMBER THA: {secret_number}")
        print(f"TUNE {attempts} ATTEMPTS MEIN JEET LIYA")
        break

    print("------ GAME OVER ------")