# Student Performance Analysis & Prediction

## Overview

This project analyzes student academic performance using behavioral, academic, and socio-economic factors. It identifies key drivers of exam scores and builds a foundation for predictive modeling.

The dataset contains **6,607 student records** with features such as attendance, study hours, tutoring sessions, motivation level, previous scores, family income, and more.

## Objectives

* Analyze factors affecting student exam performance
* Discover meaningful patterns through EDA
* Validate findings using statistics
* Build machine learning models to predict exam scores
* Develop an interactive prediction app (upcoming)

## Dataset Features

### Academic

* Hours_Studied
* Attendance
* Previous_Scores
* Tutoring_Sessions
* Exam_Score

### Behavioral

* Motivation_Level
* Sleep_Hours
* Physical_Activity

### Environmental

* Family_Income
* Teacher_Quality
* Internet_Access
* Access_to_Resources

## Key Insights

* Higher attendance strongly correlates with better scores
* Students studying 30+ hours frequently scored above 70
* Tutoring support improved average performance
* Motivation level impacts academic outcomes
* Previous scores are strong predictors of future results

Detailed findings available in `INSIGHTS.md`

## Files in Repository

* `Student-Performance-Analysis.ipynb` → Full notebook analysis
* `INSIGHTS.md` → Case study & findings
* `SPF.csv` → Dataset
* `app.py` → Prediction web app (in progress)

## Tools Used

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib
* SciPy
* Scikit-learn
* Jupyter Notebook
* Streamlit (planned)

## Future Improvements

* Deploy prediction dashboard
* Compare ML models
* Feature importance analysis
* Student risk detection system

## Author

Debasmita Sarkar
