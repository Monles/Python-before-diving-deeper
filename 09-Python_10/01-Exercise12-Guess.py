from random import randint

answer = randint(1, 10)

while True:
  try:
    guess = int(input("Guess a # from 1 ~ 10: "))
    if 0 < guess <= 10:
      if guess == answer:
        print("Win!")
        break
      else:
        print("Keep trying! Wrong Answer!")
    else:
      print("That's not between 1 and 10!")

  except ValueError:
    print("Plz Enter A Number: ")
    continue
