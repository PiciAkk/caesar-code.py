# caesar-code.py
Caesar code (Caesar Cipher) encoder, and decoder, written in Python

## Usage

### Installation
- Clone this repository
```bash
git clone https://github.com/piciakk/caesar-code.py
```
- Go to the directory, you just cloned
```bash
cd caesar-code.py
```
### Decode
- Run the decoder script
```bash
python decoder.py
```
- Enter a key
- Enter a text
- Done
### Encode
- Run the encoder script
```bash
python encoder.py
```
- Enter a key
- Enter a text
- Done
### Using as library
```python
import decoder
import encoder

decode.decodeText(text.lower(), key) # text needs to be in lowercase
# returns decoded text
encode.encodeText(text.lower(), key) # text needs to be in lowercase
# returns encoded text
```
