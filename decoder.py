import string

key = int(input("Enter key: "))
text = input("Enter text to decode: ").lower()

alphabet = list(string.ascii_lowercase)

def decodeText(text, key):
    decodedText = []
    for i in list(text):
        if i == " ":
            decodedText.append(i)
        else:
            alphabetIndex = string.ascii_lowercase.index(i)
            newAlphabetIndex = alphabetIndex - key
            decodedText.append(alphabet[newAlphabetIndex])
    
    return "".join(decodedText)
    
print(f"Decoded text: {decodeText(text, key)}")
