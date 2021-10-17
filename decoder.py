import string

key = input("Enter key: ")
text = input("Enter text to decode: ")

alphabet = list(string.ascii_lowercase)

def decodeText(text):
    decodedText = []
    for i in list(text):
        if i == " ":
            decodedText.append(i)
        else:
            alphabetIndex = string.lowercase.index(i)
            newAlphabetIndex = alphabetIndex - key
            decodedText.append(alphabet[newAlphabetIndex])
    
    return "".join(decodedText)
    
print(f"Decoded text: {decodeText(text)}")
