class NameTooShort(ValueError):
    pass


def validate(name):
    if len(name)<8:
        raise NameTooShort("name too short")
    return f"Hello {name}"

username = input("Username: ")
print(validate(username))
