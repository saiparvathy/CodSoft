import random
import string

def generate_password_with_length(target_length):

    uppercase_letters=string.ascii_uppercase
    all_characters=string.ascii_letters+string.digits+string.punctuation

    first_char=random.choice(uppercase_letters)
    remaining_length=target_length-1
    remaining_password=''.join(random.choice(all_characters) for _ in range(remaining_length))
    random_password=first_char+remaining_password

    return random_password
def main():
    target_length=input("Enter the length for password:")
    if target_length.isdigit():
        target_length=int(target_length)
        if target_length <1:
            print("password must be at leat 1")
            return 
    else:
        print("invalid input please enter a positive integer.")
        return 
    password=generate_password_with_length(target_length)

    print("Generated password",password)

main()