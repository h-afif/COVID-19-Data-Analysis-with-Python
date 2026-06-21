import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ======================
# CONFIG
# ======================

sns.set_theme(style="whitegrid")


# ======================
# LOAD DATA
# ======================

df = pd.read_csv("data/owid-covid-data.csv")


# ======================
# SELECT IMPORTANT COLUMNS
# ======================

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


# ======================
# CLEANING
# ======================

df['date'] = pd.to_datetime(df['date'])

# نحيد World / Continents / Income Groups
df = df.dropna(subset=['continent'])


# ======================
# CASES ANALYSIS
# ======================

country_cases = df.groupby(
    'location'
)['total_cases'].max()

top_10 = country_cases.sort_values(
    ascending=False
).head(10)


# ======================
# TIME SERIES ANALYSIS
# ======================

daily_cases = df.groupby(
    'date'
)['new_cases'].sum()

cumulative_cases = daily_cases.cumsum()


# ======================
# GROWTH ANALYSIS
# ======================

growth_rate = daily_cases.pct_change() * 100

growth_rate = growth_rate.replace(
    [float('inf'), float('-inf')],
    pd.NA
)

rolling_avg = daily_cases.rolling(
    window=7
).mean()


# ======================
# TOP 10 COUNTRIES CHART
# ======================

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_10.values,
    y=top_10.index
)

plt.title(
    "Top 10 Countries by Total Cases",
    fontsize=16
)

plt.xlabel(
    "Total Cases",
    fontsize=12
)

plt.ylabel(
    "Country",
    fontsize=12
)

plt.tight_layout()

plt.savefig(
    "outputs/top_10_countries.png"
)

plt.close()


# ======================
# DAILY CASES CHART
# ======================

plt.figure(figsize=(12, 6))

sns.lineplot(
    x=daily_cases.index,
    y=daily_cases.values
)

plt.title(
    "Daily COVID Cases Worldwide",
    fontsize=16
)

plt.xlabel(
    "Date",
    fontsize=12
)

plt.ylabel(
    "New Cases",
    fontsize=12
)

plt.tight_layout()

plt.savefig(
    "outputs/daily_cases.png"
)

plt.close()


# ======================
# ROLLING AVERAGE CHART
# ======================

plt.figure(figsize=(12, 6))

sns.lineplot(
    x=rolling_avg.index,
    y=rolling_avg.values
)

plt.title(
    "7-Day Rolling Average",
    fontsize=16
)

plt.xlabel(
    "Date",
    fontsize=12
)

plt.ylabel(
    "Cases",
    fontsize=12
)

plt.tight_layout()

plt.savefig(
    "outputs/rolling_average.png"
)

plt.close()


# ======================
# EXPORT RESULTS
# ======================

top_10.to_csv(
    "outputs/top_10_countries.csv"
)


# ======================
# INSIGHTS
# ======================

best_country = top_10.index[0]

highest_cases = int(
    top_10.iloc[0]
)

global_cases = int(
    cumulative_cases.iloc[-1]
)


report = f"""
COVID-19 ANALYSIS REPORT
========================

Top Country:
{best_country}

Total Cases:
{highest_cases:,}

Global Cases:
{global_cases:,}
"""


with open(
    "outputs/insights.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(report)


# ======================
# TERMINAL OUTPUT
# ======================

print("\nCOVID ANALYSIS COMPLETED")
print("-" * 40)

print(f"Top Country: {best_country}")
print(f"Total Cases: {highest_cases:,}")
print(f"Global Cases: {global_cases:,}")

print("\nFiles Generated:")
print("outputs/top_10_countries.png")
print("outputs/daily_cases.png")
print("outputs/rolling_average.png")
print("outputs/top_10_countries.csv")
print("outputs/insights.txt")