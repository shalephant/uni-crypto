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
    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)
        print(f"Shift #{shift}: {decrypted}")

def main():
    ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
    print("Ciphertext:", ciphertext)
    brute_force_decrypt(ciphertext)

if __name__ == "__main__":
    main() 
