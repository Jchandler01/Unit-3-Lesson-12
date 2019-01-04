import time
import random

print('-'*65)
print('I am a Magic eight Ball! ')
print()
question = input('What is your question? ')
time.sleep(0.7)
print('shaking!')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)

choice = random.randint(1,6)

if choice == 1:
	print('idk? ')
elif choice == 2:
	print('maybe? ')
elif choice == 3:
	print('How am I supposed to know? ')
elif choice == 4:
	print('GO AWAY!!! ')
elif choice == 5:
	print('I dont know? ')
elif choice == 6:
	print('LEAVE ME ALONE!!! ')

print('-'*65)


