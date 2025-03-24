

class InvalidPassword(Exception):
    pass

password = "abcde"

if len(password) < 5:
    raise InvalidPassword("Must be at least 5 characters.")

print('SUCCESS!')









