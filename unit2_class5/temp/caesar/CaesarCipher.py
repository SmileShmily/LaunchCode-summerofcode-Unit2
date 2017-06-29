def main():
    'Start'
    while True:
        print """
		Type an option to continue:
		--------------------------
		(a) Encrypt
		(b) Decrypt
		--------------------------
		"""
        option = raw_input()

        if option in 'a b'.split():
            return option
        else:
            print "Please input a or b to continue"


def getKey():
    'Key for shifting.'
    print "Enter the shift number(1-26)"
    key = int(raw_input())
    return key


def getMessage():
    'Type a message to Encrypt or Decrypt'
    print "Please enter your message"
    message = raw_input()
    return message


def caesar(opt, mes, key):
    'Main function'
    if opt == 'b':
        key = -key
    ciphertext = ''
    for char in mes:
        if char.isalpha():
            num = ord(char) + key
            if char.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif char.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            ciphertext += chr(num)
        else:
            ciphertext += char
    return ciphertext


opt = main()
mes = getMessage()
key = getKey()

if __name__ == '__main__':
    print "Result message is:"
    print (caesar(opt, mes, key))