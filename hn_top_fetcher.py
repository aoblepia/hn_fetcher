import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
from dotenv import load_dotenv, find_dotenv


SEND_COUNT = 10     # how many articles to send

load_dotenv(find_dotenv())
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("PASSWORD")

#print(sender_email, receiver_email, password)

def get_articles():
    api_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # gets story ids for the number of stories that you want
        top_story_ids = response.json()[:SEND_COUNT]
        articles = []

        # standard api url with story id as documented
        for story_id in top_story_ids:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story_response = requests.get(story_url)

            if story_response.status_code == 200:
                story_data = story_response.json()
                title = story_data.get("title", "")
                url = story_data.get("url", "")
                articles.append(f"{title}: {url}")

        return articles
    else:
        return []

def send_articles():
    articles = get_articles()
    if articles:

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Top HN Articles"

        body = "\n".join(articles)
        msg.attach(MIMEText(body, 'plain'))

        # login with weird app password, send
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print("Top HN Articles sent to", sender_email)
    else:
        print("Failed to fetch top articles")

# send now
send_articles()

