import time
import pyttsx3
from requests_html import HTMLSession
from IPython.display import display
from plyer import notification
import pandas as pd
import matplotlib.pyplot as plt
from unicodedata import normalize
import seaborn as sns
import PyPDF2
import random
from time import sleep
t = int(input("Run the programs after time interval of: "))
def countdown(t):
    time.sleep(t)
def speak_func(*a):

    speaker = pyttsx3.init()

    # Rate
    rate = speaker.getProperty("rate")

    # change the default rate
    speaker.setProperty("rate", 200)
    # print(rate)

    # volume(volume level between 0 to 1, min=0 to max=1)
    volume = speaker.getProperty("volume")

    # change the default volume
    speaker.setProperty("volume", 1)
    # print("volume is {0}".format(volume))

     # voices(index 0 for men,index 1 for women)
    voices = speaker.getProperty("voices")

    # change the default voice
    speaker.setProperty("voice", voices[0].id)
    # print(" Male voice:{0}".format(voices[0].id))
    # print(" Women voice:{0}".format(voices[1].id))
    speaker.say(a)
    speaker.runAndWait()

def news():
    session = HTMLSession()
    r = session.get('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')
    r.html.render(sleep=1, scrolldown=2)
    articles = r.html.find('article')
    newslist = []
    for item in articles:
        try:
            newsitem = item.find('h3', first=True)
            title = newsitem.text
            newslist.append(str(title))
        except:
           pass
    noti_title = "Latest News"
    for i in range(3):
        noti_message = str(newslist[i])
        notification.notify(
            title= noti_title,
            message= noti_message,
            timeout=10,
            app_icon='icon.ico'
        )
        speak_func(noti_title, noti_message)
def covid():
    table_1 = pd.read_html('https://en.m.wikipedia.org/wiki/Template:COVID-19_testing_by_country')
    x = table_1[0]
    df_covid = pd.DataFrame(x)
    df_mod = df_covid[:172]
    final_df = df_mod[['Country or region', 'Tested /population,%', 'Confirmed /population,%']]
    df_lst_1 = final_df["Country or region"].values.tolist()
    df_lst_2 = final_df['Confirmed /population,%'].values.tolist()
    df_lst_3 = final_df['Tested /population,%'].values.tolist()
    rand_lst = [72, 165, 164, 30, 134, 23, 81, 33]
    lst_plt_1 = []
    lst_plt_2 = []
    for i in range(len(rand_lst)):
        lst_plt_1.append(df_lst_1[rand_lst[i]])
        lst_plt_2.append(df_lst_2[rand_lst[i]])
    lst_plt_1[1] = "US"
    lst_plt_1[2] = "UK"
    lst_conf = []
    lst_tst = []
    for i in range(len(df_lst_2)):
        ty_ch = float(df_lst_2[i])
        lst_conf.append(ty_ch)
    for i in range(len(df_lst_3)):
        ty_ch = float(df_lst_3[i])
        lst_tst.append(ty_ch)
    noti_title = "India's COVID Update"
    noti_msg = f'''Tested Population :{df_lst_3[72]}%                   Confirmed Population:{df_lst_2[72]}%'''
    notification.notify(
        title=noti_title,
        message=noti_msg,
        timeout=5,
        app_icon='icon.ico'
    )
    speak_func(noti_title, noti_msg)
    sns.set_style("darkgrid")
    plt.xlabel("Countries")
    plt.ylabel("Confirmed Cases %")
    plt.bar(lst_plt_1, lst_plt_2)
    plt.plot(lst_plt_1, lst_plt_2, 'o--r')
    plt.show()
def quotes():
    alist = []
    book = open('365DailyQuotes.txt', 'rb')
    a = book.read().splitlines()
    for i in range(len(a)):
        x = str(a[i])
        alist.append(x)
    b = random.randint(1, 147)
    d = alist[b]
    notification.notify(
        title="Here's A Refreshing Quote",
        message=d,
        timeout=10,
        app_icon='forrst_logo_icon_190959.ico'
    )
    speak_func(d)
news()
countdown(t)
covid()
countdown(t)
quotes()