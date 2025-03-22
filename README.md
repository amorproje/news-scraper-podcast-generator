# News Scraper & Podcast Generator 🎧
This project scrapes the latest news from AP News, BBC, and The New York Times, converts them into a podcast format using gTTS, and sends them via email. It also saves the news data as a CSV file.

## Features 

    Web Scraping: Extracts news articles using BeautifulSoup.

    Text-to-Speech: Converts news into an audio podcast (MP3).

    Email Delivery: Sends the podcast and CSV file via email.

    Automated Updates: Runs daily to collect fresh news.

Dependencies

    requests

    BeautifulSoup (bs4)

    pandas

    gTTS

    smtplib

    email (MIME handling)

    dotenv (for environment variables)

***IMPORTANT***

***WEBSITE STRUCTURES CHANGE FREQUENTLY, SO SELECTORS MIGHT NEED UPDATES***


Install dependencies:
    pip install -r requirements.txt