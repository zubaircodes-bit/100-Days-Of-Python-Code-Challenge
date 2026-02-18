import random
letters = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m',
  'n','o','p','q','r','s','t','u','v','w','x','y','z',
  'A','B','C','D','E','F','G','H','I','J','K','L','M',
  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
];

numbers = ['1','2','3','4','5','6','7','8','9'];

symbols = [
  '!','@','#','$','%','^','&','*',
  '(',')','-','_','=','+',
  '[',']','{','}','|','\\',
  ';',':','"',"'",
  '<','>',',','.','?','/'
];

numbersCount = int(input("How many numbers would you like in your Password ? \n "))
lettersCount = int(input("How many letters would you like in your Password ? \n "))
symbolsCount = int(input("How many symbols would you like in your Password ? \n "))
password = []
for i in range(0, numbersCount):
  password.append(random.choice(numbers))
for i in range(0, lettersCount):
  password.append(random.choice(letters))
for i in range(0, symbolsCount):
  password.append(random.choice(symbols))
random.shuffle(password)
passwordstring = ""
for char in password:
  passwordstring += char
print(f"Your Password is {passwordstring}.")