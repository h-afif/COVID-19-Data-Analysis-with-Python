# 📌 COVID-19 Data Analysis Project

## 📊 Overview

This project performs exploratory data analysis (EDA) on global COVID-19 data using Python.
It analyzes trends, compares countries, and generates insights using real-world data.

---

## 🎯 Objectives

* Analyze total COVID-19 cases by country
* Identify the most affected countries
* Study global daily case trends
* Apply 7-day rolling average to smooth data
* Generate automatic insights report

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas 📊
* Matplotlib 📈
* UV (package & script runner) ⚡

---

## 📁 Project Structure

```
data/                  # Dataset (COVID-19 data)
outputs_covid_19/     # Charts and reports generated
src/                   # Main Python script
```

---

## 🚀 How to Run

This project uses **uv** as the runtime.

```bash
uv run -m src
```

📌 Make sure:

* dataset exists in `data/covid_19.csv`
* you run the command from project root

---

## 📈 Analysis Performed

### 🟢 Top Countries

Identifies the top 10 countries with the highest total COVID-19 cases.

### 🌍 Global Trend

Aggregates daily new cases worldwide to analyze overall spread over time.

### 📉 Rolling Average (7-day)

Smooths fluctuations to highlight real trends in infection waves.

---

## 📊 Outputs Generated

After running the project, the following files are created:

* 📊 `top_10_countries_by_total_covid_cases.png`
* 📈 `daily_covid_cases_worldwide.png`
* 📉 `covid_trend_over_time.png`
* 📄 `covid_19_analysis_report.txt`

---

## ▶️ Example Insight

* Highest affected country: United States
* Total global cases: ~775M
* Average daily cases: ~463K
* Peak date identified from dataset
* Clear wave patterns visible in rolling average

---

## 👨‍💻 Author

Built for learning purposes as a Data Analysis project using Python.

---

## 📌 Note

This project is part of a portfolio demonstrating basic data analysis, visualization, and reporting skills.

---
