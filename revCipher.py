# Reverse Cipher

message = input('Enter message: ')
translated = '' # Storing reverse string.

i = len(message)-1

while i>=0:
	translated = translated + message[i]
	i = i-1
	
print(translated)
