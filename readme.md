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

Format for `usernamepwd.txt`
```
user1@gmail.com, password123
user2@gmail.com, P4$$w0rD
```

Demo Example:
```
python main.py mail.thetwl.org
```
## How to run with gmail?
In order to run the script with gmail do the following steps:
1. Activate 2FA in your google account. 
2. Under the newly activated 2FA, you'll have option to generate application spefcific password.
3. Generate an application spefcific password and keep that password in the usernamepwd.txt file.

### Todo
- [ ] Add a better way to share password than plain .txt file.
- [ ] Login to office 365 using OAuth2.
- [ ] Increase efficienty by not only tracking last date for the attachments saved but also last date for any emails checked.


