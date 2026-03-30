## Asiwome Agbleze
## CMSC 111
## Spring 2026
## Week 5 Assignment - Regex Practce

import re # Regular expressions module

# Task 1: Extract phone numbers in the format 123-456-7890
def extract_phone_numbers(text):

    "Takes a block of text and returns a list of phone numbers that match the pattern 123-456-7890."
    # Regex: \b = word boundary, \d = digit, {3} or {4} = how many digits pattern = r"\b\d{3}-\d{3}-\d{4}\b"
    phone_numbers = re.findall(pattern, text)

    return phone_numbers

# Task 2: Validate email addresses
def is_valid_email(email):
    ## Returns True if the email matches the basic pattern: at least one character, @, at least one character, dot, and 2-6 letters for the extension.

    # Regex explanation:
    # ^          start of string
    # [^@\s]+    one or more characters that are not @ or space (username)
    # @          literal @
    # [^@\s]+    one or more characters that are not @ or space (domain name)
    # \.         literal dot
    # [A-Za-z]{2,6}  2 to 6 letters (extension like com, edu, net)
    # $          end of string
    pattern = r"^[^@\s]+@[\s]+\. [A-Za-z]{2,6}$"
    match = re.fullmatch(pattern, email)


    return match is not None

# Main program wrapped in try/except for basic error handling
try:
    # ---- Task 1: Extract phone numbrs ----
    sample_text = (
        "Call me at 123-456-7890 or 987-654-3210. "
        "Office: 555-111-2222. Invalid: 1234567890."
    )

    phone_list = extract_phone_numbers(sample_text)

    # Check if any phone numbers were found
    if not phone_list:
        print("No phone numbers found in the text.")
else:
    print("Phone numbers found:", phone_;;ist)

# ---- Task 2: Validate an email address ----
email_input = input("Enter an email address: ").strip()

# Make sure the user typed something
if email_input == "":
    print("Error: Email address cannot be empty.")
else:
    if is_valid_email(email_input):
        print("Invalid email address.")

# If something unexpected happens, show a friendly error message
except Exception as e:
    print("An error occurred while running the program:", e)
               


    