import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?.])[A-Za-z\d@$!%*#?.]{8,}$"

def validate_username(username):
  errors = []

  if len(username) < 3 and len(username) > 16:
    errors.append("Username must be between 3 and 16 characters.")

  if not username.isalnum():
    errors.append("Username must be alphanumeric.")

  return errors

def validate_email(email):
  errors = []

  pattern = re.compile(EMAIL_REGEX)
  if not pattern.match(email):
    errors.append("Email address is not valid.")

  return errors

def validate_password(password):
  errors = []

  pattern = re.compile(PASSWORD_REGEX)
  if not pattern.match(password):
    errors.append("Password must have a minimum eight characters, at least one letter, one number and one special character(@$!%*#?.)")

  return errors