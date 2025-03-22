import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from gtts import gTTS
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import os

"""
Run the following command in your terminal to install the required packages:
    pip install -r requirements.txt
"""

"""Constant"""
load_dotenv()
recipient_email = os.getenv("recipient_email")
mail = os.getenv("mail")
pas = os.getenv("pas")
app_pass = os.getenv("app_pass")

ALL_LIST = []
date = datetime.datetime.now()
day_of_month = date.strftime('%d')
headers = {'User-Agent': 'Mozilla/5.0'}

#app URLs
url_ap = 'https://apnews.com/world-news'

#bbc URLs
url_bbc_news = 'https://www.bbc.com/news'

with open("all_text.txt","w") as txt:
    txt.write("")
    txt.close()
"""_______________________________________________Scrapping______________________________________________________"""
"""__________________________________________APNEWS - MORENEWS list______________________________________________"""
def AP_MORE_NEWS():
    with open("all_text.txt", "a", encoding="utf-8") as txt:
        txt.write(f"apnews.com Associated Press latest news:\n ")
        txt.close()

    response_ap = requests.get(url_ap, headers=headers)
    soup_ap = BeautifulSoup(response_ap.content, 'html.parser')

    list_ap_morenews = []

    new_ap = soup_ap.find_all("div",class_="PageList-items-item")
    for n in new_ap:

        try:
            link = n.find('h3',class_="PagePromo-title").find("a").get("href")
            title = n.find("h3", class_="PagePromo-title").find("span", class_="PagePromoContentIcons-text").text
            content = n.find("div",class_="PagePromo-description").find("span",class_="PagePromoContentIcons-text").text

            list_ap_morenews.append([title, content, link])

        except:
            pass

    for new in list_ap_morenews[:5]:

        with open("all_text.txt", "a", encoding="utf-8") as txt:
            txt.write(f"{new[0]} {new[1]}\n")
            txt.close()


    ALL_LIST.append(list_ap_morenews)

AP_MORE_NEWS()

"""_________________________________________________BBC  news_____________________________________________________"""
def BBC_NEWS():
    try:
        #HEAD
        with open("all_text.txt", "a", encoding="utf-8") as txt:
            txt.write(f"bbc.com top news:\n ")
            txt.close()
        response_bbc_news = requests.get(url_bbc_news,headers=headers)
        soup_bbc_news = BeautifulSoup(response_bbc_news.content, 'html.parser')
        new_bbc_news_5 = soup_bbc_news.find("div",class_="sc-b38350e4-1 dlepEy").find("div", class_="sc-93223220-0 sc-b38350e4-2 cmkdDu QUMNJ")
        list_bbc_news = []
        for n in new_bbc_news_5:
            link = f'https://www.bbc.com{n.find("a").get("href")}'
            title = n.find("h2",class_="sc-1207bea1-3 fxdkXN").text
            content = n.find("p").text
            list_bbc_news.append([title,content,link])


        #BBC TOP NEW
        new_bbc_news_top_title = soup_bbc_news.find("h2",class_="sc-1207bea1-3 cZBSCm").text
        new_bbc_news_top_content = soup_bbc_news.find("p",class_="sc-f98732b0-0 iQbkqW").text
        new_bbc_news_top_link = soup_bbc_news.find("div",class_="sc-f98732b0-3 ephYtw").find("div",{'data-testid': 'anchor-inner-wrapper'}).find("a").get("href")
        list_bbc_news.append([new_bbc_news_top_title,new_bbc_news_top_content,new_bbc_news_top_link])

        for new in list_bbc_news:
            with open("all_text.txt", "a", encoding="utf-8") as txt:
                txt.write(f"{new[0]} {new[1]}\n")
                txt.close()
        ALL_LIST.append(list_bbc_news)

        #BBC INNOVATION
        time.sleep(0.5)
        with open("all_text.txt", "a", encoding="utf-8") as txt:
            txt.write(f"bbc INNOVATION news:\n ")
            txt.close()

        list_bbc_innovation = []
        response_bbc_innovation = requests.get("https://www.bbc.com/innovation",headers=headers)
        soup_bbc_innovation = BeautifulSoup(response_bbc_innovation.content, 'html.parser')

        bbc_innovation = soup_bbc_innovation.find("div",class_="sc-93223220-0 sc-da05643e-1 fiJvSm djXsFQ")

        for n in bbc_innovation:
            # link = f'https://www.bbc.com{n.find("a",class_="sc-2e6baa30-0 gILusN").get("href")}'
            try:
                link = f'https://www.bbc.com{n.find("a",class_="sc-2e6baa30-0 gILusN").get("href")}'
                title = n.find("h2", class_="sc-1207bea1-3 bsYjcJ").text
                content = n.find("p", class_="sc-ae29827d-0 cNPpME").text
                list_bbc_innovation.append([title,content,link])
            except:
                pass

        for new in list_bbc_innovation[:5]:
            with open("all_text.txt", "a", encoding="utf-8") as txt:
                txt.write(f"{new[0]} {new[1]}\n")
                txt.close()

        ALL_LIST.append(list_bbc_innovation)

        #BBC ART
        time.sleep(0.3)
        with open("all_text.txt", "a") as txt:
            txt.write(f"bbc ART news:\n ")
            txt.close()

        list_bbc_ART = []
        response_bbc_ART = requests.get("https://www.bbc.com/arts",headers=headers)
        soup_bbc_ART = BeautifulSoup(response_bbc_ART.content, 'html.parser')

        bbc_ART = soup_bbc_ART.find("div",class_="sc-93223220-0 sc-da05643e-1 fiJvSm djXsFQ")

        for n in bbc_ART:
            try:
                link = f'https://www.bbc.com{n.find("a",class_="sc-2e6baa30-0 gILusN").get("href")}'
                title = n.find("h2", class_="sc-1207bea1-3 bsYjcJ").text
                content = n.find("p", class_="sc-ae29827d-0 cNPpME").text
                list_bbc_ART.append([title,content,link])

            except:
                pass
        for new in list_bbc_ART[:5]:
            with open("all_text.txt", "a", encoding="utf-8") as txt:
                txt.write(f"{new[0]} {new[1]}\n")
                txt.close()
        ALL_LIST.append(list_bbc_ART)

        #BBC culture
        time.sleep(0.4)
        with open("all_text.txt", "a") as txt:
            txt.write(f"bbc culture news:\n ")
            txt.close()
        list_bbc_culture = []
        response_bbc_culture = requests.get("https://www.bbc.com/culture",headers=headers)
        soup_bbc_culture = BeautifulSoup(response_bbc_culture.content, 'html.parser')

        bbc_culture = soup_bbc_culture.find("div",class_="sc-93223220-0 sc-da05643e-1 fiJvSm djXsFQ")

        for n in bbc_culture:
            try:
                link = f'https://www.bbc.com{n.find("a",class_="sc-2e6baa30-0 gILusN").get("href")}'
                title = n.find("h2", class_="sc-1207bea1-3 bsYjcJ").text
                content = n.find("p", class_="sc-ae29827d-0 cNPpME").text
                list_bbc_culture.append([title,content,link])

            except:
                pass
        for new in list_bbc_culture[:5]:
            with open("all_text.txt", "a", encoding="utf-8") as txt:
                txt.write(f"{new[0]} {new[1]}\n")
                txt.close()

        ALL_LIST.append(list_bbc_culture)
    except:
        pass
BBC_NEWS()

"""________________________________________________nytimes_____________________________________________"""

def NEWYORKTIMES_NEWS():

    # lifestyle

    with open("all_text.txt", "a", encoding="utf-8") as txt:
        txt.write(f"www.nytimes.com The New York Times lifestyle news:\n ")
        txt.close()

    list_nytimes_lifestyle = []
    response_nytimes_lifestyle = requests.get("https://www.nytimes.com/spotlight/lifestyle",headers=headers)
    soup_nytimes_lifestyle = BeautifulSoup(response_nytimes_lifestyle.content, 'html.parser')

    nytimes_lifestyle = soup_nytimes_lifestyle.find("ol",{"data-testid":"asset-stream"})


    for n in nytimes_lifestyle:
        try:
            link = f'https://www.nytimes.com{n.find("a",class_="css-8hzhxf").get("href")}'
            title = n.find("h3", class_="css-1j88qqx e15t083i0").text
            content = n.find("p", class_="css-1pga48a e15t083i1").text
            list_nytimes_lifestyle.append([title,content,link])

        except:
            pass
    for new in list_nytimes_lifestyle[:5]:
        with open("all_text.txt", "a", encoding="utf-8") as txt:
            txt.write(f"{new[0]} {new[1]}\n")
            txt.close()

    ALL_LIST.append(list_nytimes_lifestyle)

    #arts
    time.sleep(0.4)
    with open("all_text.txt", "a") as txt:
        txt.write(f"The New York Times ART news:\n ")
        txt.close()
    list_nytimes_arts = []
    response_nytimes_arts = requests.get("https://www.nytimes.com/section/arts",headers=headers)
    soup_nytimes_arts = BeautifulSoup(response_nytimes_arts.content, 'html.parser')

    nytimes_arts = soup_nytimes_arts.find("ol",{"data-testid":"asset-stream"})


    for n in nytimes_arts:
        try:
            link = f'https://www.nytimes.com{n.find("a",class_="css-8hzhxf").get("href")}'
            title = n.find("h3", class_="css-1j88qqx e15t083i0").text
            content = n.find("p", class_="css-1pga48a e15t083i1").text
            list_nytimes_arts.append([title,content,link])

        except:
            pass
    for new in list_nytimes_arts[:5]:
        with open("all_text.txt", "a", encoding="utf-8") as txt:
            txt.write(f"{new[0]} {new[1]}\n")
            txt.close()
    ALL_LIST.append(list_nytimes_arts)

NEWYORKTIMES_NEWS()

def Podcast_maker():

    with open("all_text.txt","r", encoding="utf-8") as all_text:
        complete_text = all_text.read()
        all_text.close()


    tts = gTTS(complete_text)
    filename = f"PODCAST{day_of_month}.mp3"
    tts.save(filename)

Podcast_maker()

def Csv_maker():
    columns = ['title', 'content', 'link']

    rows = []
    for first in ALL_LIST:

        for sec in first:

            row = dict(zip(columns, sec))
            rows.append(row)
    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(f'csv{day_of_month}.csv', index=False)



Csv_maker()

def Mail_sending():
    subject = f"Podcast of day: {day_of_month}"
    body = "Listen to top news of famous news agencies "
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465


    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = mail
    message['To'] = recipient_email
    body_part = MIMEText(body)
    message.attach(body_part)

    with open(f"PODCAST{day_of_month}.mp3", 'rb') as file:
        # Attach the file with filename to the email
        message.attach(MIMEApplication(file.read(), Name=f"PODCAST{day_of_month}.mp3"))

    with open(f'csv{day_of_month}.csv', 'rb') as file:
    # Attach the file with filename to the email
        message.attach(MIMEApplication(file.read(), Name=f'csv{day_of_month}.csv'))

    # secction 2 for sending email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:

        server.login(mail, app_pass)
        server.sendmail(from_addr=mail,to_addrs= recipient_email, msg=message.as_string())

Mail_sending()