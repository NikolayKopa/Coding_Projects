inputFile = open("PlainText.txt","r")
outputFile = open("cipher.txt","w")
outputFile2 = open("PlainOutput.txt","w")
normalalphabet = "abcdefghijklmnopqrstuvwxyz"
encryptedalphabet = "phqgiumeaylnofdxjkrcvstzwb"
def encryption(inp):
    result = ""
    for a in inp:
        if a == " ":
            result = result + a
        elif a == ",":
            result += a
        else:
            index_normal = normalalphabet.find(a.lower())
            result += encryptedalphabet[index_normal]
    return result
def decryption(inp2):
    result2 = ""
    for a in inp2:
        if a == " ":
            result2 = result2 + a
        elif a == ",":
            result2 += a
        else:
            index_encrypt = encryptedalphabet.find(a.lower())
            result2 += normalalphabet[index_encrypt]
    return result2
outputFile.write(encryption(inputFile.read()))
inputFile.close()
outputFile.close()
inputFile2 = open("cipher.txt", "r")
outputFile2.write(decryption(inputFile2.read()))
inputFile2.close()
outputFile2.close()
