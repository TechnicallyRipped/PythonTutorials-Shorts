
def validate_pw(pw:str):
    has_upper = False
    has_lower = False
    has_number = False

    for i in pw:
        if i.islower():
            has_lower = True
        elif i.isupper():
            has_upper = True
        elif i.isdigit():
            has_number = True
    return has_upper and has_lower and has_number

password = 'abC2026'

if validate_pw(password):
    print("Valid password")
else:
    print("Invalid password")