# Quote of the Day Email Sender

This Python script sends a daily inspirational quote email using a Gmail account.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system.
- A Gmail account to send emails from.

## Setup

1. Clone or download the repository.

2. Update the script with your Gmail email address and password.

## Usage

1. Run the script.
    ```
    python quote_of_the_day.py
    ```
2. The script will log in to your Gmail account, choose a random inspirational quote, and send it as an email to the recipient.

## Customization

You can customize the following aspects of the script:

- **Email Recipient**: Change the `to_addrs` variable to specify the recipient's email address.
- **SMTP Server and Port**: Modify `gmail_server` and `port` variables if you're using a different SMTP server.
- **Quotes**: Add, remove, or modify quotes in the `messages` list to suit your preferences.

## Note

- Ensure that you allow less secure apps to access your Gmail account or use App Passwords if you have two-factor authentication enabled.

