#!usr/bin/python

if __name__ == '__main__':

        I = 5
        SOLUCE = [57,73,79,16,18,26,74,50,13,38,13,79,86,86,87]
        KEY = 'I know, you love decrypting Byte Code !'
        ANSWER = ""
        for X in SOLUCE:
        	TMP = X ^ ord(KEY[I])
        	TMP = TMP - I
        	ANSWER += chr(TMP)
        	I = (I + 1) % len(KEY)

        print(ANSWER)
