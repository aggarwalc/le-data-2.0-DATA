import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.DataFrame(columns=['date', 'language', 'count'])
for year in range(2008,2023):
    for month in range(1,13):
        if month < 10:
            date = f"{year}-0{month}"
        else:
            date = f"{year}-{month}"

        if date == '2022-06': break
        print(date)


        url = f"https://github.com/search?q=created%3A{date}&type=Repositories"
        
        while (True):
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            chicken = soup.select("a.filter-item")
            noodle = list(soup.select("h3")[1].stripped_strings)[0].split(' ')

            if len(noodle) == 3:
                print(noodle)
                break


        month_total = int(noodle[0].replace(',', ''))


        top_tags_total = 0
        for anchor_tag in chicken:
            [count, lang] = list(anchor_tag.stripped_strings)
            count = int(count.replace(',', ''))
            df = df.append({'date' : date, 'language' : lang, 'count' : count}, ignore_index = True)
            top_tags_total += count

        df = df.append({'date' : date, 'language' : 'Others', 'count' : month_total - top_tags_total}, ignore_index = True)
        time.sleep(8)


print(df)
df.to_csv('gh_top_languages_results.csv')

# print(df.pivot(index='date', columns='language', values='count'))
