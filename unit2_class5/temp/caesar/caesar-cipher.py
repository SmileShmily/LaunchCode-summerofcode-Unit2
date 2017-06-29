mode = input('Encrypt or Decrypt? [E/D] \n')
if mode == "E":
    print("Encrypt-ing.\n")
elif mode == "D":
    print("Decrypt-ing.\n")

message = input('Enter message: \n')

key = input('Enter key: [1-25] \n')
print('Using key: '+key+'\n')
key = int(key)


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = message.upper()
result = ""

for char in message:
    if char in LETTERS:
        x = LETTERS.find(char)
        if(mode == 'E'):
            x = x+key
        elif(mode == 'D'):
            x = x-key

        if x >= 26:
            x = x-26
        elif x < 0:
            x = x+26

        result = result + LETTERS[x]

print('Result: '+result)