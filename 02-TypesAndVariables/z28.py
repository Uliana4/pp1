h = int(input(" Enter your height in cm: "))
w = int(input(" Enter your weight in kg: "))
bmi = (w/h/h)*10000
print(f" Your BMI index: {bmi}")
if bmi<18.5:
    print(" Under weight")
elif bmi>=18.5 and bmi<=24.9:
    print(" Normal weight")
elif bmi>=25 and bmi<=29.9:
    print(" Over weight")
elif bmi>=30 and bmi<=34.9:
    print(" Obese 1")
elif bmi>=35 and bmi<=39.9:
    print(" Obese 2")
else:
    print(" Obese 3")