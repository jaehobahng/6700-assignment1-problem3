
---

# 🚨📨 Emails Alerts 🚨📨

This Python program allows the user to send emails to a recipient via SMTP protocals. Plain-text emails can be sent when the user provides the sender, recipient, subject, and body of the email. 

## Features

📪 Sends plain text emails using the SMTP protocol.

📪 Allows for easy use through command-line arguments.

## Requirements

📬 Python 3.11

📬 An SMTP server for email sending (such as Python’s built-in `smtpd`).

## Installation 

1. **Clone the repository**:
   ```bash
   git clone git@github.com:DSAN6700-24Fall/assignment-1-jaehobahng.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd assignment-1-jaehobahng-problem3
   ```

3. **Ensure Python is installed**:
   Make sure you have Python 3.11 installed. You can check by running:
   ```bash
   python --version
   ```

## Usage

1️⃣ **Start a local SMTP server for testing** (if you don't have a real one):
   ```bash
   python -m smtpd -c DebuggingServer -n localhost:1025
   ```
   This starts an SMTP server that prints email details to the console (for testing). The email alerts will be printing here for testing rather than gettign sent to the sender/reciepient. 

2️⃣ **Send an email by running the script**:
   You can use the following command to send an email:

   ```bash
   python alert.py -s "sender@example.com" -r "recipient@example.com" -j "Test Subject" -b "This is the email body."
   ```

**The following is a description of the flags used in the example above:**
### Command-Line Arguments:

- `-s` or `--sender`: The email address of the sender (required).
- `-r` or `--recipient`: The email address of the recipient (required).
- `-j` or `--subject`: The subject of the email (default is `"Subject"`).
- `-b` or `--body`: The body of the email (default is `"Body"`).


## Code Overview

Below, we will be breaking down the scripts used to execute this project. For more details, please open our [sphinx documentation](https://github.com/jaehobahng/6700-assignment1-problem3/blob/main/docs/_build/html/index.html). 

### `alert.py` 

This function handles the construction and sending of the email using the `smtplib` and `email` libraries. 

The program takes in sender, recipient, subject, and body text information from the command line. 

```python
def setup_args(parser):
    parser.add_argument("-s", "--sender", type=str, required=True)
    parser.add_argument("-r", "--recipient", type=str, required=True)
    parser.add_argument("-j", "--subject", type=str, default="Subject")
    parser.add_argument("-b", "--body", type=str, default="Body")
    return parser
```

The `main()` function parses the arguments and calls the `send_email()` function with the provided values.

```python
def main():
    parser = ArgumentParser()
    args = setup_args(parser).parse_args()

    send_email(
        sender=args.sender,
        recipient=args.recipient,
        subject=args.subject,
        body=args.body
    )
```

### `mailer.py` 

This script contains the function `send_email()`, which constructs and sends the email using Python's smtplib and email modules. This method is used in the `alert.py` to send out the email in `main()`. 

```python
def send_email(sender, recipient, subject, body):
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = recipient
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    if body is not None:
        msg.attach(MIMEText(body, "plain"))

    s = SMTP("localhost", 1025)
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()
```

## Running the Script

1️⃣ Open a terminal or command prompt.

2️⃣ Ensure you have the necessary SMTP server running on `localhost:1025`.

3️⃣ Run the script using the `python` command, providing the necessary command-line arguments for sender, recipient, subject, and body.

## Error Handling

Currently, the script assumes a local SMTP server is running on `localhost:1025`. If the SMTP server is not running, or the connection fails, the script will terminate with an error. For future further improvements, you can add error handling for SMTP connection errors and other exceptions.

---
