# Read and store Email attachments
As simple as the title goes, this small python script will go through your email, filter out the unseen emails and downloads the attachments in the following pattern:
`attachments_for_<username at the email address>`

## How to use?
create file named `usernamepwd.txt` and add the email and credentials for your users. And run the following command

```
pip install -r requirements.txt
python main.py <hostname> 
```
\<hostname> should be your hostname. Example: mail.thetwl.org, mail.ashimdahal.com, etc.

Demo Example:
```
python main.py mail.thetwl.org
```
