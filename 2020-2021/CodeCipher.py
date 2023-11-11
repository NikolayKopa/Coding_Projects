inputFile = open('CodeCipher.txt','r')
outputFile = open('CipherOutput.txt','w')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
inputFileRead = input_file.read()
splitInputFileRead = inputFileRead.split('\n')

def cipher(k, text):
    string = ''
    integerK = int(k)
alphabet_length = 26
for i in text:
    if i in alphabet:
        find = alphabet.find(i)
        scramble = int(find) + integerK
        if scramble > alphabet_length-1:
            difference = (alphabet_length - 1)- find
            scramble = integerK - difference - 1
            string = string + alphabet[scramble]
        else:
            string = string + alphabet[scramble]
        else:
            string = string + i
    return(string)

def textEncryption(text):
    listText = list(text)
    excess = []
    for i in range(len(text)):
        if text[i] not in alphabet:
            excess.append([i,text[i]])
            listText.remove(text[i])
    listText.reverse()
    for i in excess:
        listText.insert(i[0],i[1])
    return ''.join(listText)

def main():
    lengthChunk = len(splitInputFileRead)
    for i in range(0, lengthChunk, 2):
        text = splitInputFileRead[i + 1]
        k = splitInputFileRead[i]
        string = cipher(k, text)
        string = string.split()
        for i in string:
            outputFile.write(textEncryption(i) + ' ')
            print(textEncryption(i), e = ' ')
        outputFile.write('\n')
        print('\n')
    outputFile.close()

main()
