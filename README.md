# News Scraper and Email Notifier

This project is a simple news scraper that fetches the latest headlines from BBC News' RSS feed, formats the headlines, and sends them to a specified email address. It uses Python with libraries like `requests`, `BeautifulSoup`, `smtplib`, and `.env` to handle environment variables securely.

## Features

- Scrapes the latest 5 news headlines from [BBC News RSS Feed](https://feeds.bbci.co.uk/news/rss.xml).
- Formats the news titles and their links into a structured format.
- Sends the news headlines as a daily digest email to the configured email address.
- Securely stores and uses credentials (email username, password) through environment variables loaded from a `.env` file.

## Requirements

Make sure you have Python 3.x installed. You can install the necessary dependencies using `pip` by running:

```bash
pip install -r requirements.txt
