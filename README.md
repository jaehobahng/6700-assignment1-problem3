
---

# 🌸Python Email Sender🌸

This is a simple Python script that sends emails using the SMTP protocol. It can be used to send plain text emails by providing command-line arguments for the sender, recipient, subject, and body of the email. 😄

## 📪Features📪

- Sends plain text emails using the SMTP protocol.
- Allows easy configuration through command-line arguments.
- Built with Python's standard libraries for email handling (`smtplib`, `email`).
- Designed for local testing with an SMTP server running on `localhost` at port `1025`.

## Requirements

📬 Python 3.x <br>
📬 An SMTP server for email sending (such as Python’s built-in `smtpd` for local testing or a tool like `MailHog`).

## 📬Installation📬

1. **Clone the repository**:
   ```bash
   git clone git@github.com:DSAN6700-24Fall/assignment-1-jaehobahng.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd assignment-1-jaehobahng
   ```

3. **Ensure Python is installed**:
   Make sure you have Python 3.x installed. You can check by running:
   ```bash
   python --version
   ```

## Usage

1. **Start a local SMTP server for testing** (if you don't have a real one):
   ```bash
   python -m smtpd -c DebuggingServer -n localhost:1025
   ```
   This starts an SMTP server that prints email details to the console (for testing).

2. **Send an email by running the script**:
   You can use the following command to send an email:

   ```bash
   python script_name.py -s "sender@example.com" -r "recipient@example.com" -j "Test Subject" -b "This is the email body."
   ```

### Command-Line Arguments:

- `-s` or `--sender`: The email address of the sender (required).
- `-r` or `--recipient`: The email address of the recipient (required).
- `-j` or `--subject`: The subject of the email (default is `"Subject"`).
- `-b` or `--body`: The body of the email (default is `"Body"`).

### Example:

```bash
python script_name.py -s "your_email@example.com" -r "friend@example.com" -j "Hello" -b "This is a test email."
```

## Code Overview

### `send_email` function

This function handles the construction and sending of the email using the `smtplib` and `email` libraries.

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

### Argument Parser

The `setup_args` function handles the configuration of command-line arguments for the script.

```python
def setup_args(parser):
    parser.add_argument("-s", "--sender", type=str, required=True)
    parser.add_argument("-r", "--recipient", type=str, required=True)
    parser.add_argument("-j", "--subject", type=str, default="Subject")
    parser.add_argument("-b", "--body", type=str, default="Body")
    return parser
```

The `main()` function parses the arguments and calls the `send_email()` function with the provided values.

## Running the Script

1. Open a terminal or command prompt.
2. Ensure you have the necessary SMTP server running on `localhost:1025`.
3. Run the script using the `python` command, providing the necessary command-line arguments for sender, recipient, subject, and body.

## Error Handling

Currently, the script assumes a local SMTP server is running on `localhost:1025`. If the SMTP server is not running, or the connection fails, the script will terminate with an error. To improve the script, you can add error handling for SMTP connection errors and other exceptions.

## Future Improvements

- **Error Handling**: Add try-except blocks to handle failures during the email sending process.
- **Authentication**: Extend the functionality to work with authenticated SMTP servers.
- **HTML Content & Attachments**: Add support for sending HTML emails and attachments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the `README.md` file to include additional sections or modify it to suit your project structure!