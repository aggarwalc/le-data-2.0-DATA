import pandas as pd

df = pd.read_csv('gh_top_monthly_results.csv')
df['date'] = pd.to_datetime(df['date'])

df = df.groupby(df['date'].dt.year).agg('sum')

print(df)
df.to_csv('gh_top_yearly_results.csv')
