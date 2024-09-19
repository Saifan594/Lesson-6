print("\033c")

height = float ( input ( "enter your height (m) : " ) )
weight = float ( input ( "enter your weight (kg) : " ) )

bmi = weight / (height ** 2)
print(f"your bmi is {bmi}")

if bmi <= 18.4 :
    print("you are underweight")

elif bmi <= 24.9 :
    print("you are healthy")

elif bmi <= 29.9 :
    print("you are over weight")

elif bmi <= 34.9 :
    print("you are severely over weight")

elif bmi <= 39.9 :
    print("you are obese")

else :
    print("you are severely obese")