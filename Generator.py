import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        print("Error: At least one character type must be selected.")
        return None

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the password length: "))
        
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for length.")

if _name_ == "_main_":
    main()