import pandas as pd


df: pd.DataFrame = pd.read_csv("data/owid-covid-data.csv")

important_columns = [
    'location',
    'continent',
    'date',
    'total_cases',
    'new_cases',
    'total_deaths',
    'new_deaths',
    'population'
]

df = df[important_columns]

df['location'] = df['location'].str.strip()
df['location'] = df['location'].str.lower()

df['date'] = pd.to_datetime(df['date'])

df['total_cases'] = df['total_cases'].fillna(0)
df['new_cases'] = df['new_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df['new_deaths'] = df['new_deaths'].fillna(0)

df = df.dropna(subset=['continent'])

df = df.sort_values(by=['location', 'date'])

print(df[['total_cases',
          'new_cases',
          'total_deaths',
          'new_deaths']].describe())