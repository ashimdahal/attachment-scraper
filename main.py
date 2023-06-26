from imap_tools import MailBox, AND
import ssl
import argparse
import os
import imap_tools
import schedule
import time

parser = argparse.ArgumentParser(
    prog="Email Attachment Scraping",
    description="Goes through your emails and saves"
    "attachments from unseen/unread emails",
    epilog="Made with <3 by Ashim.",
)

parser.add_argument(
    "Hostname", help="provide the hostname of the mailserver. EG: mail.thetwl.org"
)
# HOSTNAME = "mail.thetwl.org"
args = parser.parse_args()
HOSTNAME = args.Hostname


def save_new_attachments(username, password, save_folder):
    with MailBox(HOSTNAME, ssl_context=ssl.create_default_context()).login(
        username, password, initial_folder="INBOX"
    ) as mailbox:
        print("Login Success")
        # Fetch emails with attachments
        emails = mailbox.fetch(AND(seen=False))

        # emails= mailbox.fetch(criteria=mailbox.has_attachment())
        # Iterate over emails with attachments
        for email in emails:
            print(email.subject)
            if not (email.attachments):
                mailbox.flag(
                    [email.uid], imap_tools.MailMessageFlags.SEEN, False
                )  # noqa
                continue
            for attachment in email.attachments:
                attachment_fname = email.date_str + " " + attachment.filename
                if attachment_fname not in os.listdir(save_folder):
                    # Save attachment to the specified folder
                    filepath = os.path.join(save_folder, attachment_fname)
                    with open(filepath, "wb") as file:
                        file.write(attachment.payload)

                    print(f"Attachment saved at {attachment_fname}.")
            mailbox.flag([email.uid], imap_tools.MailMessageFlags.SEEN, False)  # noqa
    print(f"Checked email for {username}")


def check_attachments():
    u_pwds = open("usernamepwd.txt", "r").readlines()
    for upwd in u_pwds:
        user, password = upwd.split(",")

        save_folder = f"attachments_for_{user.split('@')[0]}"
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        save_new_attachments(user.strip(), password.strip(), save_folder)


# Schedule the save_new_attachments function to run every minute
schedule.every(2).seconds.do(check_attachments)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
