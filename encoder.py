import string
    
alphabet = list(string.ascii_lowercase)

def encodeText(text, key):
    encodedText = []
    for i in list(text):
        if i == " ":
            encodedText.append(i)
        else:
            alphabetIndex = string.ascii_lowercase.index(i)
            newAlphabetIndex = alphabetIndex + key
            encodedText.append(alphabet[newAlphabetIndex])
    
    return "".join(encodedText)
    
if __name__ == "__main__":
    key = int(input("Enter key: "))
    text = input("Enter text to encode: ").lower()
    print(f"Encoded text: {encodeText(text, key)}")