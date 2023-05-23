import random
import wordlist


cword=random.choice(wordlist.words)

display=[]
lives=6
for letter in cword:
	display+="_"
print(display)

game_over=False
while  game_over==False:
	gletter=input("guess a letter").lower()
	for position in range(len(cword)):
		letter=cword[position]
		if letter==gletter:
			display[position]=gletter
			print(display)
			
	if gletter not in cword:
		lives-=1
		if lives==0:
			game_over=True
			print("you lose!")
			print(cword)
	if "_" not in display:
		game_over=True
		print("You Won!")