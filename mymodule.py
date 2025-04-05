# mymodule.py
def validate_email():
    special_char = ['#', '$', '/', '?', '<', '>', '*', '&', '%', ':', '!', '_', ')', '(']
    count = 5
    while count > 0:
        email = input('Please enter your email: ')
        try:

            if not email:
                raise ValueError("Email cannot be empty.")

            if not isinstance(email, str):
                raise TypeError("Email must be a string.")

            if email.isdigit():
                raise TypeError("Email must not be a digit.")

            for char in email:
                if char in special_char:
                    raise ValueError("Email cannot contain special characters.")

            if '@' not in email or '.' not in email:
                raise ValueError("Email must contain '@' and '.'.")

            username, domain = email.split('@')
            if not username or not domain:
                raise ValueError("Invalid email format.")

            print("Email is valid.")
            return email
        except (ValueError, TypeError) as x:
            count -= 1
            print(f"Invalid email: {x}")

    print("You have exceeded the maximum number of trying")
    return None
