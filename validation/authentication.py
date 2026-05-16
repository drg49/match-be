import re
from models.user import Users


# -----------------------------
# EMAIL
# -----------------------------
EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'


def validate_email(email):
    email = email.strip().lower()

    if len(email) < 3 or len(email) > 150:
        return False, 'Email must be between 3 and 150 characters.'

    if not re.match(EMAIL_REGEX, email):
        return False, 'Invalid email address.'

    if Users.query.filter_by(email=email).first():
        return False, 'Email already registered.'

    return True, ''


# -----------------------------
# PASSWORD (STRONGER)
# -----------------------------
def validate_password(password):
    if len(password) < 8 or len(password) > 128:
        return False, 'Password must be between 8 and 128 characters.'

    if ' ' in password:
        return False, 'Password cannot contain spaces.'

    if not re.search(r'[A-Z]', password):
        return False, 'Password must contain at least one uppercase letter.'

    if not re.search(r'[a-z]', password):
        return False, 'Password must contain at least one lowercase letter.'

    if not re.search(r'\d', password):
        return False, 'Password must contain at least one number.'

    return True, ''


# -----------------------------
# FIRST NAME
# -----------------------------
NAME_REGEX = r"^[a-zA-Z'-]{1,25}(?: [a-zA-Z'-]{1,25})*$"


def validate_first_name(first_name):
    if not first_name:
        return False, 'First name cannot be empty.'

    first_name = first_name.strip()

    if len(first_name) > 25:
        return False, 'First name cannot exceed 25 characters.'

    if not re.match(NAME_REGEX, first_name):
        return False, 'Invalid first name format.'

    return True, ''


# -----------------------------
# LAST NAME
# -----------------------------
def validate_last_name(last_name):
    if last_name is None or last_name == '':
        return True, ''  # last name optional

    last_name = last_name.strip()

    if len(last_name) > 25:
        return False, 'Last name cannot exceed 25 characters.'

    if not re.match(NAME_REGEX, last_name):
        return False, 'Invalid last name format.'

    return True, ''