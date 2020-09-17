def main():
    """Create a dictionary of emails and check if name generated is equal to your name"""
    email = input("Email: ")
    check_email_for_name = {}
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation != "" and confirmation.upper() != "Y":
            name = input("Name: ")
        check_email_for_name[email] = name
        email = input("Email: ")

    for email, name in check_email_for_name.items():
        print("{} {}".format(name, email))


def get_name_from_email(email):
    """Get name from email address."""
    individual_name = email.split('@')[0]
    parts = individual_name.split('.')
    name = " ".join(parts).title()
    return name


main()