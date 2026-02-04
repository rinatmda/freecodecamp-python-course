# Demographic Data Analyzer

This project analyzes demographic data from the 1994 Census database to uncover insights about income, education, occupation, and work patterns. The work was completed as part of FreeCodeCamp's [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer) course. 

> Note: This project uses starter code provided by freeCodeCamp. The main task was to implement the function `calculate_demographic_data()` in `demographic_data_analyzer.py` to perform the required analysis.

---

## Project Overview

The goal of this project is to answer several demographic and income-related questions, including:

- How many people of each race are represented  
- The average age of men  
- Percentage of people with a Bachelor's degree  
- Salary statistics based on education level  
- Minimum working hours and high-earning percentages  
- Country with the highest percentage of people earning >50K  
- Most popular occupation for high earners in India  

The analysis is performed in `demographic_data_analyzer.py`, with results verified using unit tests in `test_module.py`.

---

## Skills & Tools

Python | Pandas | Data Cleaning | Exploratory Data Analysis (EDA) 

---
## Files in This Project

- `main.py` — Entry point for running the project and automated tests  
- `demographic_data_analyzer.py` — Contains the main function `calculate_demographic_data()`  
- `test_module.py` — Unit tests for the project  
- `requirements.txt` — Python dependencies  
- `adult.data.csv` — Dataset used for analysis  

---

## Key insights:

- **Higher education and income:** People with advanced education (Bachelors, Masters, or Doctorate) are more than 2.5 times as likely to earn over 50K compared to those without advanced education (46.5% vs 17.4%).  
- **Minimum working hours:** Individuals working the minimum number of hours per week are less likely to earn over 50K; only 10% of this group are high earners.  
- **Top countries for high earners:** The top three countries with the highest percentage of people earning over 50K are Iran (41.9%), France (41.4%), and India (40%).  
