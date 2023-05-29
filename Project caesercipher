alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encryption(plain_text,shift_key):
	new_text=""
	for char in plain_text:
		if char in alphabet:
		
			position=alphabet.index(char)
			new_pos=(position+shift_key)%26
			new_text+=alphabet[new_pos]
		else:
			new_text+=char
	print("encrypted text is:",new_text)
def decryption(cipher_text,shift_key):
	new_text=""
	for char in cipher_text:
		if char in alphabet:
		
			position=alphabet.index(char)
			new_pos=(position-shift_key)%26
			new_text+=alphabet[new_pos]
		else:
			new_text+=char
	print("decrypted text is:",new_text)



end=False
while end==False:
	wtd=input("enter 'encrypt' for encryption and 'decrypt' for decryption:")
	text=input("enter the message\n").lower()
	shift=int(input("enter the shift key\n"))
	if wtd=='encrypt':
		encryption(plain_text=text,shift_key=shift)
	
	elif wtd=="decrypt":
		decryption(cipher_text=text,shift_key=shift)
	play_again=input("Type Yes to Continue & no to stop:")
	if(play_again=="no"):
		end=True
		print("Ok Have A Nice Day Bye Bye...")
