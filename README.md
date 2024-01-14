# HN top article fetcher, sender

This script gets the top HN articles and emails them to you.

## API credit

https://github.com/HackerNews/API

# To use

Clone this repo, then

```bash
pip install -r requirements.txt
```
Then, create a .env file in the same directory and add these requirements:

```dotenv
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=recipient_email@gmail.com
PASSWORD=your_email_password
```
Then you can run the script.

```bash
python hn_top_fetcher.py
```

# Notes

Modify the `SEND_COUNT` parameter as you want.

For the email password, you may need to enable an 'app password' for Gmail. You can do this in the Gmail 2FA settings.

The email will send immediately. You can schedule the email to send when you want with Task Scheduler (windows) or crontab (linux).