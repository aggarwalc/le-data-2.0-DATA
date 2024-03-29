import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

def calc_lang_total(url):
    while (True):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # handles rate limit
        try:
            if 'find' in list(soup.select("h3")[1].stripped_strings)[0]:
                return(0)
            total_repos_html = list(soup.select("h3")[1].stripped_strings)[0].split(' ')
        except:
            total_repos_html = []

        # handles incomplete data retrieval
        if len(total_repos_html) == 3:
            return(int(total_repos_html[0].replace(',', '')))

def calc_month_total(url):
    while (True):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # handles rate limit
        try:
            total_repos_html = list(soup.select("h3")[1].stripped_strings)[0].split(' ')
        except:
            total_repos_html = []

        # handles incomplete data retrieval
        if len(total_repos_html) == 3:
            return(int(total_repos_html[0].replace(',', '')))

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

languages = ['Swift', 'Kotlin', 'Dart', 'Objective-C']

df = pd.DataFrame(columns=['date', 'language', 'percent'])
for year in range(2008,2023):
    for month in range(1,13):
        if month < 10:
            date = f"{year}-0{month}"
        else:
            date = f"{year}-{month}"

        if date == '2022-11': break
        print(date)

        url = f"https://github.com/search?q=created%3A{date}&type=Repositories"
        month_total = calc_month_total(url)

        for lang in languages:

          url = f"https://github.com/search?q=created%3A{date}+language%3A{lang}&type=Repositories"
          lang_total = calc_lang_total(url)
          print(lang, lang_total)

          df = df.append({'date':pd.to_datetime(date), 'language':lang, 'percent':lang_total/month_total*100}, ignore_index = True)
          time.sleep(7)


print(df)
df.to_csv('gh_app_dev_results.csv', index=False)
