import pandas as pd

pd.set_option('display.max_rows', None)
# stack overflow app development
so_app = pd.read_csv('/Users/aggarwalc/Desktop/le-data-2.0-DATA/Stack-Overflow/app-dev/app_development_results.csv', usecols=['date', 'percent', 'tag'])
so_app.rename(columns={'tag':'language'}, inplace=True)
so_app['date'] = pd.to_datetime(so_app['date'])

# stack overflow general languages
so_gen = pd.read_csv('/Users/aggarwalc/Desktop/le-data-2.0-DATA/Stack-Overflow/general-languages/general_languages_results.csv', usecols=['date', 'percent', 'tag'])
so_gen.rename(columns={'tag':'language'}, inplace=True)
so_gen['date'] = pd.to_datetime(so_gen['date'])
so_gen = so_gen.loc[1:]

# stack overflow machine learning languages
so_mac = pd.read_csv('/Users/aggarwalc/Desktop/le-data-2.0-DATA/Stack-Overflow/machine-learning-languages/machine_learning_languages_results.csv', usecols=['date', 'percent', 'tag'])
so_mac.rename(columns={'tag':'language'}, inplace=True)
so_mac['date'] = pd.to_datetime(so_mac['date'])
so_mac = so_mac[so_mac['language'] != 'python']

# github app development
gh_app = pd.read_csv('/Users/aggarwalc/Desktop/le-data-2.0-DATA/GitHub/gh-app-dev/gh_app_dev_results.csv')
gh_app = gh_app.loc[28:]
gh_app = gh_app[gh_app['percent']>0]
gh_app['date'] = pd.to_datetime(gh_app['date'])

# github general languages
gh_gen = pd.read_csv('/Users/aggarwalc/Desktop/le-data-2.0-DATA/GitHub/gh-general-languages/gh_general_languages_results.csv')
gh_gen = gh_gen.loc[49:]
gh_gen = gh_gen[gh_gen['percent']>0]
gh_gen['date'] = pd.to_datetime(gh_gen['date'])

# github machine learning languages
gh_mac = pd.read_csv('/Users/aggarwalc/Desktop/le-data-2.0-DATA/GitHub/gh-machine-learning-languages/gh_machine_learning_languages_results.csv')
gh_mac = gh_mac.loc[42:]
gh_mac = gh_mac[gh_mac['percent']>0]
gh_mac['date'] = pd.to_datetime(gh_mac['date'])
gh_mac = gh_mac[gh_mac['language'] != 'Python']

combined = pd.concat([so_app, so_gen, so_mac, gh_app, gh_gen, gh_mac], ignore_index=True)
combined = combined.sort_values(by=['date', 'language'], ignore_index=True)
combined.to_csv('combined_results.csv', index=False)
