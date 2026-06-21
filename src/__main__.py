import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

df['date'] = pd.to_datetime(df['date'])

df = df[important_columns]

df = df.dropna(subset=['continent'])

contry_cases = df.groupby('location')['total_cases'].max()


top_10 = contry_cases.sort_values(ascending=False).head(10)


daily_cases = df.groupby('date')['new_cases'].sum()

daily_cases = daily_cases[daily_cases > 100]

growth_rate = daily_cases.pct_change() * 100

growth_rate = growth_rate.replace(
    [float('inf'), float('-inf')],
    pd.NA
)

rolling_avg = daily_cases.rolling(window=7).mean()


plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
sns.barplot(x=top_10.values, y=top_10.index)
plt.title("Top 10 contries by total cases")
plt.xlabel("Total cases")
plt.ylabel("Country")

plt.show()

plt.figure(figsize=(14, 6))
sns.lineplot(x=daily_cases.index, y=daily_cases.values)

plt.title("Daily COVID cases")
plt.xlabel("Date")
plt.ylabel("New Cases")

plt.show()

plt.figure(figsize=(14, 6))
sns.lineplot(x=rolling_avg.index, y=rolling_avg.values)

plt.title("7-Day Rolling Average")
plt.xlabel("Date")
plt.ylabel("Cases")

plt.show()

