from faker import Faker
from pathlib import Path

CREDS_DIR = Path("credentials")
CREDS_DIR.mkdir(exist_ok=True)


def random_email_generator(save_to_file: bool = True) -> str:
    """Create a dummy gmail email using faker and optionally save to credentials/username.txt

    Returns the generated email string.
    """
    dummy = Faker()
    dummy_email = dummy.email(domain='gmail.com')
    if save_to_file:
        with open(CREDS_DIR / "username.txt", "w") as file:
            file.write(dummy_email)
    print(f"generated email: {dummy_email}")
    return dummy_email


def random_password_generator(save_to_file: bool = True) -> str:
    """Create a dummy password using faker and optionally save to credentials/password.txt

    Returns the generated password string.
    """
    dummy = Faker()
    dummy_password = dummy.password(length=12, special_chars=True, upper_case=True)
    if save_to_file:
        with open(CREDS_DIR / "password.txt", "w") as file:
            file.write(dummy_password)
    print(f"generated password: {dummy_password}")
    return dummy_password
