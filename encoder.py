import string

key = int(input("Enter key: "))
text = input("Enter text to encode: ").lower()

alphabet = list(string.ascii_lowercase)

def encodeText(text):
    encodedText = []
    for i in list(text):
        if i == " ":
            encodedText.append(i)
        else:
            alphabetIndex = string.ascii_lowercase.index(i)
            newAlphabetIndex = alphabetIndex + key
            encodedText.append(alphabet[newAlphabetIndex])
    
    return "".join(encodedText)
    
print(f"Encoded text: {encodeText(text)}")
