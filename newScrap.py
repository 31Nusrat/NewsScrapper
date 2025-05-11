import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()
EMAIL_USER=os.getenv('EMAIL_USER')
EMAIL_PASS=os.getenv('EMAIL_PASS')
EMAIL_TO=os.getenv('EMAIL_TO')

url = "https://feeds.bbci.co.uk/news/rss.xml"
response = requests.get(url)
soup = BeautifulSoup(response.content, features='xml')


def send_email(news_body):
    msg=MIMEText(news_body)
    msg['Subject']='Your Daily News Digest'
    msg['From']=EMAIL_USER
    msg['To']=EMAIL_TO
    with smtplib.SMTP("smtp.gmail.com",587)as server:
        server.starttls()
        server.login(EMAIL_USER,EMAIL_PASS)
        server.send_message(msg)
    print("Message Sent Successfully!")

news_list=[]
items = soup.find_all('item')[:5]
for i, item in enumerate(items, 1):
    title = item.title.text
    link=item.link.text
    news_list.append(f"{i}. {title}\n{link}")

news_body='\n\n'.join(news_list)
send_email(news_body)

# print(news_body)