# Case Study: Student Performance Prediction & Factor Analysis

## Executive Summary

This project analyzes 6,607 student records to identify the academic, behavioral, and environmental factors that influence exam performance. Through data cleaning, exploratory data analysis, statistical testing, and predictive modeling, several measurable relationships were identified. Attendance, study hours, tutoring frequency, motivation level, previous academic scores, and healthy lifestyle habits were all associated with stronger student outcomes.

The objective of this project was to transform raw student data into actionable insights that could support educators, institutions, and policy makers in improving academic performance.

## Objective

To identify the key drivers of student exam performance and build a predictive analytics workflow capable of estimating student scores using historical and behavioral data.

## Dataset Overview

The dataset contains **6,607 student records** with **20 variables**, covering:

### Academic Variables

* Hours_Studied
* Attendance
* Previous_Scores
* Tutoring_Sessions
* Exam_Score

### Behavioral Variables

* Motivation_Level
* Sleep_Hours
* Physical_Activity
* Extracurricular_Activities

### Environmental & Socio-Economic Variables

* Family_Income
* Teacher_Quality
* School_Type
* Internet_Access
* Access_to_Resources
* Parental_Involvement
* Parental_Education_Level
* Distance_from_Home

### Demographic Variables

* Gender

## Data Quality & Preprocessing

The following preprocessing steps were performed:

* Inspected dataset structure, data types, and completeness
* Checked missing values in categorical columns
* Imputed missing categorical values using mode replacement
* Verified duplicates and cleaned records where necessary
* Standardized column understanding for analysis
* Created derived metrics for deeper insight generation

Final cleaned dataset retained all usable observations for analysis.

## Methodology

The project followed a structured analytics workflow:

1. Data Cleaning & Preparation
2. Exploratory Data Analysis (EDA)
3. Correlation Analysis
4. Hypothesis Testing
5. Predictive Modeling Preparation
6. Insight Generation & Recommendations

Libraries used included Python, Pandas, NumPy, Seaborn, Matplotlib, SciPy, and Scikit-learn.

## Exploratory Data Analysis

The following relationships were studied:

* Attendance vs Exam Score
* Hours Studied vs Exam Score
* Tutoring Sessions vs Exam Score
* Motivation Level vs Performance
* Sleep Hours vs Performance
* Teacher Quality vs Performance
* Family Income vs Performance
* Access to Resources vs Outcomes

Visual tools included:

* Histograms
* Boxplots
* Scatterplots
* Correlation Heatmaps
* Grouped Mean Comparisons

## Key Findings

### 1. Attendance Is One of the Strongest Drivers

Attendance showed one of the strongest positive relationships with performance. Students with near-perfect attendance averaged over **8 marks higher** than students with 60% attendance.

### 2. Study Hours Positively Impact Scores

Students who studied more hours generally achieved higher exam scores. Students studying **30+ hours frequently averaged above 70**, while lower study-hour groups scored notably lower on average.

### 3. Tutoring Support Improves Outcomes

Average exam scores increased steadily with tutoring frequency:

* 0 sessions → 66.51
* 3 sessions → 67.95
* 5 sessions → 69.09
* 6 sessions → 71.67

This indicates academic support programs can positively impact student results.

### 4. Motivation Level Matters

Students categorized with higher motivation levels generally outperformed lower-motivation peers, highlighting the importance of engagement and mindset.

### 5. Healthy Lifestyle Shows Positive Effect

Balanced sleep duration and regular physical activity were moderately associated with better exam performance.

### 6. Previous Academic Scores Are Strong Predictors

Students with stronger previous scores typically continued to perform well in final exams.

### 7. Resource Access Plays a Role

Students with better access to educational resources and internet connectivity showed improved outcomes relative to lower-access groups.

## Statistical Validation

A two-sample t-test was conducted comparing:

* Students with **0 tutoring sessions**
* Students with **3 or more tutoring sessions**

### Result:

* t-statistic = -11.19
* p-value < 0.001

### Interpretation:

The score difference between these groups was statistically significant, indicating that tutoring participation is strongly associated with improved academic performance.

## Predictive Modeling

A predictive modeling workflow was prepared using student behavioral and academic variables to estimate exam scores.

### Candidate Models:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

### Target Variable:

* Exam_Score

### Input Features Included:

* Hours_Studied
* Attendance
* Previous_Scores
* Tutoring_Sessions
* Sleep_Hours
* Motivation_Level
* Family_Income
* Teacher_Quality
* Internet_Access

This framework can be extended into a production-ready student performance prediction tool.

## Recommendations

Based on analysis findings:

### For Schools

* Improve attendance tracking systems
* Expand tutoring support programs
* Encourage effective study habits through mentoring
* Strengthen teacher quality initiatives
* Improve access to learning resources

### For Students

* Maintain consistent attendance
* Build disciplined study routines
* Seek tutoring support when needed
* Prioritize sleep and balanced routines

### For Parents

* Increase academic involvement
* Encourage motivation and study structure
* Support access to digital learning tools

## Limitations

* Dataset findings are observational and do not prove causation
* Some emotional, psychological, and curriculum factors were not captured
* Real-world institutional differences may affect generalization

## Future Scope

This project can be expanded into:

* Early-risk student detection system
* Pass/Fail classification model
* Streamlit prediction dashboard
* Feature importance explainability dashboard
* Institution-level intervention recommendation system

## Tools & Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Scikit-learn
* Jupyter Notebook

## Conclusion

This case study demonstrates how student data can be transformed into meaningful educational intelligence. Academic performance is influenced not only by study hours, but also by attendance, support systems, motivation, prior results, and environmental conditions.

By combining analytics with predictive modeling, institutions can move from reactive decisions to proactive student success strategies.
