# Author: 0xSpiizN
## Challenge: crypto_multlock
## Description: Reverse from source.py file to get the flag

# Import modules
import string
import random
import base64

# Define the function generate_key
def generate_key(seed, length=16):
    random.seed(seed)
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return key

# Polyalphabetic

## Polyalphabetic encryption
def polyalphabetic_encrypt(plaintext, key):
    key_length = len(key)
    ciphertext = []
    for i, char in enumerate(plaintext):
        key_char = key[i % key_length]
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)
        ciphertext.append(encrypted_char)
    return base64.b64encode(''.join(ciphertext).encode()).decode()

## Polyalphabetic decryption
def polyalphabetic_decrypt(ciphertext, key):
    try:
        ciphertext = base64.b64decode(ciphertext).decode()
        key_length = len(key)
        plaintext = []
        for i, char in enumerate(ciphertext):
            key_char = key[i % key_length]
            decrypted_char = chr((ord(char) - ord(key_char)) % 256)
            plaintext.append(decrypted_char)
        return ''.join(plaintext)
    except Exception as e:
        return None

# Xor

## Xor cipher
def xor_cipher(text, key):
    return bytes([ord(c) ^ key for c in text])

## Xor decipher
def xor_decipher(text, key):
    return bytes([c ^ key for c in text])

# Filter function to ensure valid output
def is_valid_output(text):
    return all(c in string.printable for c in text)

def main():
    assert polyalphabetic_decrypt(ciphertext=polyalphabetic_encrypt(plaintext="test", key="OhbVrpoiVgRV5IfL"), key="OhbVrpoiVgRV5IfL") == "test" # Test de fonctionnement de la fonction polyalphabetic_decrypt
    assert xor_decipher(text=xor_cipher(text="test", key=42), key=42).decode() == "test" # Test de fonctionnement de la fonction xor_decipher

    # Initialize the flag list
    flag_hallf = []

    # Split the flag
    with open("../src/output.txt", "r") as f:
        encrypted_flags = f.read().splitlines()

    # Brute force the flag
    print("[+] Searching for the flag...")
    for encrypted_flag in encrypted_flags:
        for key_seed in range(1, 1001):
            for xor_key in range(1, 256):
                key = generate_key(key_seed)
                encrypted_half = bytes.fromhex(encrypted_flag)
                encrypted_half = xor_decipher(encrypted_half, xor_key)
                encrypted_half = polyalphabetic_decrypt(encrypted_half, key)

                if encrypted_half is not None:
                    if (encrypted_half.startswith("HTB{") or encrypted_half.endswith("}")) and (is_valid_output(encrypted_half)):
                        print(f"[+] One part found: {encrypted_half}")
                        flag_hallf.append(encrypted_half)
    
    print("[+] FLAG:", "".join(flag_hallf))
    

if __name__ == "__main__":
    main()