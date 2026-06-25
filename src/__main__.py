import pandas as pd
import matplotlib.pyplot as plt


df: pd.DataFrame = pd.read_csv("data/covid_19.csv", on_bad_lines='skip')


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

df = df.dropna(subset=['continent', 'total_cases', 'new_cases', 'new_deaths'])

df['date'] = pd.to_datetime(df['date'])

country_cases = df.groupby('location')['total_cases'].max()

top_10 = country_cases.sort_values(ascending=False).head(10)
bottom_10 = country_cases.sort_values(ascending=True).head(10)


daily_cases = df.groupby('date')['new_cases'].sum().sort_index()

rolling_avg = daily_cases.rolling(7).mean()


plt.figure(figsize=(14, 10))
top_10.sort_values().plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries by Total COVID Cases", fontsize=18, fontweight='bold', color='green')
plt.xlabel("Country", fontsize=12, fontweight='bold', color='green')
plt.ylabel("Total Cases", fontsize=12, fontweight='bold', color='green')
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig("outputs_covid_19/top_10_countries_by_total_covid_cases.png")
plt.close()


plt.figure(figsize=(18, 8))
daily_cases.plot(color='blue', kind='line')
plt.title("Daily COVID Cases Worldwide", fontsize=18, fontweight='bold', color='green')
plt.xlabel("Date", fontsize=12, fontweight='bold', color='green')
plt.ylabel("New Cases", fontsize=12, fontweight='bold', color='green')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs_covid_19/dialy_covid_cases_worldwide.png")
plt.close()


plt.figure(figsize=(14, 6))
daily_cases.plot(alpha=0.3, label="Daily Cases")
rolling_avg.plot(color='red', label="7-Day Average")
plt.title("Covid Trend Over Time", fontweight='bold')
plt.xlabel("Date", fontweight='bold')
plt.ylabel("Cases", fontweight='bold')
plt.legend()
plt.tight_layout()
plt.savefig("outputs_covid_19/covid_trend_over_time.png")



report = f"""
{"=" * 20} Data Analyst Report {"=" * 20}

🟢 Top 10 Countries:

{top_10}


🌍 Global Cases:

{daily_cases.sum()}


📊 Average Daily Cases:

{daily_cases.mean():.0f}


📅 Peak Day:

{daily_cases.idxmax()}


🔥 Max Daily Cases:

{rolling_avg.iloc[-1]:.0f}

"""

print(top_10)
print()
print(daily_cases.sum())
print()

print(daily_cases.mean())
print()

print(daily_cases.idxmax())
print()

print(rolling_avg.iloc[-1])
print(report)