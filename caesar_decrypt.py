def decrypt_caesar(ciphertext, shift):
    """
    Decrypt a Caesar cipher text with the given shift.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine the case of the character
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Apply the shift and wrap around if necessary
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def brute_force_decrypt(ciphertext):
    """
    Try all 26 shifts
    """

    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)
        print(f"Shift #{shift}: {decrypted}")

def main():
    # The given ciphertext
    ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
    
    print("Original ciphertext:", ciphertext)
    
    # Show all possible decryptions
    brute_force_decrypt(ciphertext)

if __name__ == "__main__":
    main() 