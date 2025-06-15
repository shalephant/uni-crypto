import base64
from itertools import cycle

def base64_xor(ciphertext, passphrase):
    decoded_ciphertext = base64.b64decode(ciphertext)
    print("Base64 decoded ciphertext: ", decoded_ciphertext)
    decoded_passphrase = passphrase.encode()
    xor_result = bytes([a ^ b for a, b in zip(decoded_ciphertext, cycle(decoded_passphrase))])
    print("XOR result: ", xor_result.decode())

    


def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def brute_force_decrypt(ciphertext):

    print("\nBrute Force Results:")
    print("-" * 50)
    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)
        print(f"Shift {shift}: {decrypted}")

def main():
    encoded_passphrase = "mznxpz"    
    brute_force_decrypt(encoded_passphrase)


    # Got rescue for the shift #21 which should be anagram for "secure"

    passphrase = "secure"

    ciphertext = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="

    base64_xor(ciphertext, passphrase)



if __name__ == "__main__":
    main() 