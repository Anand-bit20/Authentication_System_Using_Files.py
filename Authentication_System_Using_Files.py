def register(): # Function Created For Registration
    print("Registration Page".center(90))
    print("*"*100)
    # Validating Name
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            print("You've entered a valid name:", name)
            break
        else:
            print("Invalid input. Please enter a valid name containing only alphabets.")

    # Validating Email Address
    valid_domains = ['com', 'in', 'ac', 'org', 'edu']
    while True:
        email = input("Enter an email address: ")
        parts = email.split('@')
        if len(parts) == 2 and parts[1].split('.')[-1] in valid_domains:
            print("You've entered a valid email address:", email)
            break
        else:
            print("Invalid input. Please enter a valid email address with a valid domain name like .com, .in, .ac, .org, or .edu")

    # Validating Password
    while True:
        password = input("Enter a password: ")
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_special = any(c in '!@#$%^&*()-_+=' for c in password)
        has_digit = any(c.isdigit() for c in password)

        if has_upper and has_lower and has_special and has_digit:
            print("You've entered a valid password.")
            break
        else:
            print("Invalid password. Please enter a password containing at least one uppercase letter, one lowercase letter, one special character, and one digit.")

    # Validating Contact number
    while True:
        contact = input("Enter contact number: ")
        if contact.isdigit() and len(contact) == 10:
            print("You've entered a valid contact number:", contact)
            break
        else:
            print("Invalid input. Please enter a valid 10-digit contact number containing only digits.")

    # Validating Address    
    while True:
        address = input("Enter address: ")
        if any(c.isupper() for c in address) and any(c.islower() for c in address) and any(c in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '/'] for c in address) and any(c.isdigit() for c in address):
            print("You've entered a valid address:", address)
            break
        else:
            print("Invalid Address. Please enter an address containing at least one uppercase letter, one lowercase letter, one special character, and one digit.")

    with open('register1.txt', 'a') as f:
        f.write(name + '\n')
        f.write(email + '\n')
        f.write(password + '\n')
        f.write(contact + '\n')
        f.write(address + '\n')

    print("Registration Successful!!\n")
    main()


def login(): # Function created for Login
    # Opening the file containing registered users
    with open('register1.txt', 'r') as f:
        lines = f.readlines()

    attempts = 3
    print("Login Page".center(90))
    print("*"*100)
    print()
    print(f"You have {attempts} attempts to login.")
    for attempt in range(attempts):
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        # Check whether the email address matches a registered user
        user_found = False
        for i in range(0, len(lines), 5):
            user_email = lines[i + 1].strip()
            user_password = lines[i + 2].strip()
            if user_email == email:
                user_found = True
                if user_password == password:
                    print("Login successful!")
                    return
                else:
                    print("Incorrect password. Please try again.")

        if not user_found:
            print("No registered user with that email address. Please try again.")
        # Checking for attempts remaining
        if attempt < attempts - 1:
            print(f"You have {attempts - attempt - 1} attempts remaining.")
        else:
            print("Login failed.")

    reset_password = input("RESET PASSWORD? (YES/NO): ")
    if reset_password.upper() == "YES":
        new_password = input("Enter a new password: ").strip()
        # Update the user's password in the file
        with open('register1.txt', 'w') as f:
            for i in range(0, len(lines), 5):
                user_email = lines[i + 1].strip()
                if user_email == email:
                    # Check that the new password is different from the old password
                    if lines[i + 2].strip() == new_password:
                        print("Error: Your new password cannot be the same as your old password.")
                        return
                    else:
                        f.write(lines[i])
                        f.write(user_email + "\n")
                        f.write(new_password + "\n")
                        f.write(lines[i + 3])
                        f.write(lines[i + 4])
                else:
                    f.write(lines[i])
                    f.write(lines[i + 1])
                    f.write(lines[i + 2])
                    f.write(lines[i + 3])
                    f.write(lines[i + 4])
        print("Password changed successfully!")

    else:
        print("Login failed.")

    main()


def main(): # Main Function

    print("AUTHENTICATION SYSTEM".center(93))
    print("*"*100)
    print("1. Registration".center(90))
    print("2. Login".center(90))
    print("3. Exit".center(90))
    n = int(input('Enter your Choice: '))
    if n == 1:
        register()
    elif n == 2:
        login() 
    elif n == 3:
        print("Exit")
    else:
        print("Invalid choice. Please enter a valid option.")
        main()


main()
