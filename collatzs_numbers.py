def collatz(number):
  
  if number % 2 == 0:
    number = number / 2
  else:
    number = number * 3 + 1
  
  return number

def userInput():
  print("Please enter an integer number")
  number_to_use = int(input())
  result = 0

  while collatz(number_to_use)>=1:
    result = collatz(number_to_use)
    print(int(result))
    number_to_use = result
    if number_to_use == 1:
      break

userInput()


