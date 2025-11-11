import random
import string
import secrets

class SecurePass:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate_password(self, length=16, use_symbols=True):
        chars = self.lowercase + self.uppercase + self.digits
        if use_symbols:
            chars += self.symbols
        
        password = [
            secrets.choice(self.lowercase),
            secrets.choice(self.uppercase),
            secrets.choice(self.digits)
        ]
        
        if use_symbols:
            password.append(secrets.choice(self.symbols))
        
        for _ in range(length - len(password)):
            password.append(secrets.choice(chars))
        
        random.shuffle(password)
        return ''.join(password)
    
    def caesar_encrypt(self, text, shift=7):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result
    
    def caesar_decrypt(self, text, shift=7):
        return self.caesar_encrypt(text, -shift)
    
    def vigenere_encrypt(self, text, key):
        result = ""
        key = key.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
                key_index += 1
            else:
                result += char
        return result
    
    def vigenere_decrypt(self, text, key):
        result = ""
        key = key.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
                key_index += 1
            else:
                result += char
        return result

def main():
    sp = SecurePass()
    
    while True:
        print("\n=== SecurePass Generator & Cipher ===")
        print("1. Generate Password")
        print("2. Caesar Encrypt")
        print("3. Caesar Decrypt")
        print("4. Vigenere Encrypt")
        print("5. Vigenere Decrypt")
        print("6. Exit")
        
        choice = input("Choose option (1-6): ").strip()
        
        if choice == "1":
            length = int(input("Password length (default 16): ") or 16)
            symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
            password = sp.generate_password(length, symbols)
            print(f"Generated Password: {password}")
            
        elif choice == "2":
            text = input("Text to encrypt: ")
            shift = int(input("Shift value (default 7): ") or 7)
            encrypted = sp.caesar_encrypt(text, shift)
            print(f"Encrypted: {encrypted}")
            
        elif choice == "3":
            text = input("Text to decrypt: ")
            shift = int(input("Shift value (default 7): ") or 7)
            decrypted = sp.caesar_decrypt(text, shift)
            print(f"Decrypted: {decrypted}")
            
        elif choice == "4":
            text = input("Text to encrypt: ")
            key = input("Encryption key: ")
            encrypted = sp.vigenere_encrypt(text, key)
            print(f"Encrypted: {encrypted}")
            
        elif choice == "5":
            text = input("Text to decrypt: ")
            key = input("Decryption key: ")
            decrypted = sp.vigenere_decrypt(text, key)
            print(f"Decrypted: {decrypted}")
            
        elif choice == "6":
            print("Goodbye!")
            break
            
        else:
            print("Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()
