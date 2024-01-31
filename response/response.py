from validator_collection import validators

try:
    email_address = validators.email(input("What's your Email Address ? "))

    print("Valid")
except:
    print("Invalid")
