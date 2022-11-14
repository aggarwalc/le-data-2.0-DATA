import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

df = pd.DataFrame(columns=['value', 'language'])
step = 0

languages = {'C#':'C%23', 'C++':'C%2B%2B', 'Java':'Java',
             'JavaScript':'JavaScript', 'PHP':'PHP', 'Python':'Python',
             'Ruby':'Ruby', 'Swift':'Swift', 'Kotlin':'Kotlin',
             'Dart':'Dart', 'Objective-C':'Objective-C', 'R':'R',
             'MATLAB':'MATLAB', 'Julia':'Julia', 'Fortran':'Fortran'}
             # 'SPSS':'SPSS%20statistical', 'SAS':'SAS%20statistical'}

for lang in languages:
    step += 1
    # LinkedIn Scrape
    url = f"https://www.linkedin.com/jobs/search/?keywords={languages[lang]}&location=United%20States"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    results = list(soup.find_all("label", attrs={"for":"f_TPR-3"})[0].stripped_strings)
    LinkedIn_count = int(''.join(char for char in results[0] if char.isdigit()))

    df = df.append({'value':LinkedIn_count, 'language':lang}, ignore_index=True)

df = df.sort_values(by='value', ascending=False, ignore_index=True)
df['step'] = list(range(1, 16))

df.to_csv('./job_listings_results_current.csv', index=False)
