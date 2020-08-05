import random

print('Number guessing Game')
Number= random.randint(1,9)

chances = 0

print('Guess any Number (Between 1 to 9):')

while chances <5:
    guess = int(input())

    if guess == Number:
        print("Congratulation YOU WON!!")
        break
#elif guess < number:
  #  print("Your Guess was too low. Guess higher Number than " )

    else:
        print(' Your guess was too high. guess a lower number than ', guess)
    chances +=1

if not chances < 5:
    print("YOU LOSE!!! the Number is ", number)        