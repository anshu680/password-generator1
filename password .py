import string
import secrets

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if not (use_upper or use_lower or use_digits or use_symbols):
        raise ValueError("At least one character set must be selected.")

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Secure Password Generator")
    print("-" * 35)

    try:
        length = int(input("Enter password length (min 4): "))
        if length < 4:
            print("Password length must be at least 4 characters.")
            return

        # Toggle options
        use_upper = input("Include UPPERCASE letters? (Y/n): ").strip().lower() != 'n'
        use_lower = input("Include lowercase letters? (Y/n): ").strip().lower() != 'n'
        use_digits = input("Include digits (0-9)? (Y/n): ").strip().lower() != 'n'
        use_symbols = input("Include symbols (!@#$%)? (Y/n): ").strip().lower() != 'n'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print("\n✅ Your Generated Password:")
        print(password)

    except ValueError:
        print("❌ Invalid input. Please enter a number for password length.")

if __name__ == "__main__":
    main()
