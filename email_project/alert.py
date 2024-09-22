from argparse import ArgumentParser
from mailer import send_email


def setup_args(parser):
    """
    Setup the command line arguments for the email that will be sent.

    Arguments:
        parser - ArgumentParser object.

    Returns:
        ArgumentParser object with the required arguments added.
    """

    parser.add_argument("-s", "--sender", type=str, required=True)
    parser.add_argument("-r", "--recipient", type=str, required=True)
    parser.add_argument("-j", "--subject", type=str, default="Subject")
    parser.add_argument("-b", "--body", type=str, default="Body")

    return parser

def main():
    """
    Main function to send an email using the function  setup_args and send_email created in mailer.py.
    """

    parser = ArgumentParser()
    args = setup_args(parser).parse_args()

    send_email(
        sender=args.sender,
        recipient=args.recipient,
        subject=args.subject,
        body=args.body
    )

if __name__ == "__main__":
    main()