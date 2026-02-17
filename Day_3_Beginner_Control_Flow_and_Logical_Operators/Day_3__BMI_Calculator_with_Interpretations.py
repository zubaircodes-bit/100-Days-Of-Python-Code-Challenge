height = float(input("Please Enter Your Height in meters : "))
weight = float(input("Please Enter Your Weight in kgs : "))
bmi = (weight / height ** 2)
if bmi < 18.5:
  print("underweight.")
elif bmi >= 18.5 and bmi < 25:
  print("normal weight.")
else :
  print("overweight.")
print(int(bmi))
