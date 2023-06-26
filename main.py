from imap_tools import MailBox, AND
import os
import schedule
import time

# IMAP server details
HOSTNAME = "mail.thetwl.org"
# Folder to save attachments


def save_new_attachments(username, password, save_folder):
    with MailBox(HOSTNAME).login(username, password, initial_folder="INBOX") as mailbox:
        # Fetch emails with attachments
        emails = mailbox.fetch(AND(seen=False))

        # Iterate over emails with attachments
        for email in emails:
            for attachment in email.attachments:
                attachment_fname = email.date_str + " " + attachment.filename
                if attachment_fname not in os.listdir(save_folder):
                    # Save attachment to the specified folder
                    filepath = os.path.join(save_folder, attachment_fname)
                    with open(filepath, "wb") as file:
                        file.write(attachment.payload)

                    print(f"Attachment '{attachment.filename}' saved.")
    print("Surfed the mails Succesfully.")


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
