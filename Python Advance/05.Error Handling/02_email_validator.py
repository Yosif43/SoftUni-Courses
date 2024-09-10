class NameTooShortError(Exception):
    """"Checking the length of the email name"""
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    """Check if the domains are by specifications given"""
    pass


valid_domains = [".com", ".bg", ".net", ".org"]

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    domain = email.split(".")[-1]  # Another solution could be writen ``> domain = "." + email.split(".")[-1] <`` which means line 27 will go without ``> "." + <``
    if len(email.split("@")[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." + domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
