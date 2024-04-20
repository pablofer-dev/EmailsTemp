# OneSecMail

OneSecMail is a Python class for generating temporary email addresses using the 1secmail API and retrieving emails sent to those addresses.

[1secmail API](https://www.1secmail.com/)

## Features

- Generate a temporary email address.
- Check for incoming emails.
- Retrieve the content of incoming emails.

## Installation

1. Clone this repository: git clone ```https://github.com/your-username/OneSecMail.git```

2. Install the required dependencies: ```pip install -r requirements.txt```

## Example

```python


from OneSecMail import OneSecMail

# Create an instance of OneSecMail custom domain
email = OneSecMail(customDomain = True, domain = 'laafd.com')
# Create an instance of OneSecMail
email = OneSecMail()

# Generate a temporary email address
email.generate_email()

# Check for incoming emails and print subject and body if any
if email.check_email():
    email_data = email.get_email()
    print("Subject:", email.subject)
    print("Body:", email_data["textBody"])
else:
    print("No new emails.")