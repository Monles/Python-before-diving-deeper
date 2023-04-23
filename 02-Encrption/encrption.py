import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# Encryption
plain_text = input("Enter something to encrypt: ")
cipher_text = ""

for i in plain_text:
  index = chars.index(i)
  cipher_text += key[index]

print(f"Origin: {plain_text}")
print(f"Encrypted: {cipher_text}")

# Decrypt
encrypted_text = input("Enter the encrypted message: ")
decrypted_text = ""

for i in encrypted_text:
  index = key.index(i)
  decrypted_text += chars[index]

print(f"Encrypted: {encrypted_text}")
print(f"Origin: {decrypted_text}")