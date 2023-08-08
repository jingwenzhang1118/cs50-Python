from validator_collection import validators

try:
    email_address = validators.email(input("What's your email address? "))
    print("Valid")
except (ValueError, TypeError):
    print("Invalid")