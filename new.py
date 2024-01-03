import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n != guess:
    if guess < n :
        print('too low')
        guess = int(input("Enter any number: "))
    elif guess > n:
        print ('too high')
        guess = int(input("Enter any number: "))
    else:
        break
print('you guessed it Right')

print('Finish')