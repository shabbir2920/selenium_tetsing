from faker import Faker


def random_email_generator():
    """this method will create dummy email_id
    using faker library"""
    dummy = Faker()
    dummy_email = dummy.email(safe=True, domain='gmail.com')
    with open("credentials_username.txt", "w") as file:
        file.write(f"the username is - {dummy_email}")
        file.close()
    print(f"the email id of user is {dummy_email}")
    return dummy_email


def random_password_generator():
    """this method will create dummy password
    using faker library"""
    dummy = Faker()
    dummy_password = dummy.password(length=10, special_chars=True, upper_case=True)
    with open("credentials_password.txt", "w") as file:
        file.write(f"the password is - {dummy_password}")
        file.close()
    print(f"the password of user is {dummy_password}")
    return dummy_password
