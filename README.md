# SecurePass - Password Generator & Cipher Tool

A Python-based secure password generator with built-in encryption capabilities using Caesar and Vigenère ciphers.

## Features

- **Cryptographically Secure Password Generation**: Uses Python's `secrets` module for true randomness
- **Customizable Password Length**: Generate passwords of any desired length (default: 16 characters)
- **Character Set Options**: Include/exclude symbols based on requirements
- **Dual Cipher Support**: 
  - Caesar Cipher for simple encryption
  - Vigenère Cipher for enhanced security
- **Guaranteed Complexity**: Ensures passwords contain uppercase, lowercase, digits, and symbols

## Installation

No external dependencies required. Uses Python standard library only.

```bash
git clone <repository-url>
cd "Random Password generator and cipher"
```

## Usage

### Interactive Menu
```bash
python securepass.py
```

The program provides an interactive menu with options:
1. Generate Password - Create secure passwords with custom length
2. Caesar Encrypt - Encrypt text with shift cipher
3. Caesar Decrypt - Decrypt Caesar cipher text
4. Vigenere Encrypt - Encrypt with keyword cipher
5. Vigenere Decrypt - Decrypt Vigenere cipher text
6. Exit - Quit the program

### Programmatic Usage
```python
from securepass import SecurePass

sp = SecurePass()

# Generate a 20-character password
password = sp.generate_password(20)

# Encrypt with Caesar cipher
encrypted = sp.caesar_encrypt(password, shift=5)
decrypted = sp.caesar_decrypt(encrypted, shift=5)

# Encrypt with Vigenère cipher
key = "MYKEY"
encrypted = sp.vigenere_encrypt(password, key)
decrypted = sp.vigenere_decrypt(encrypted, key)
```

## Methods

- `generate_password(length, use_symbols)` - Generate secure random password
- `caesar_encrypt(text, shift)` - Encrypt text using Caesar cipher
- `caesar_decrypt(text, shift)` - Decrypt Caesar cipher text
- `vigenere_encrypt(text, key)` - Encrypt text using Vigenère cipher
- `vigenere_decrypt(text, key)` - Decrypt Vigenère cipher text

## Security Features

- Uses `secrets` module for cryptographically strong random generation
- Guarantees password complexity with mixed character types
- Supports multiple encryption algorithms for different security needs

## Requirements

- Python 3.6+
- No external dependencies

## License

Open source - feel free to modify and distribute.
