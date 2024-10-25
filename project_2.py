import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('StudentPerformanceFactors.csv')

# Check if there are any missing values in the dataset
data.columns[data.isnull().any()]

# drop missing values
data.dropna(inplace=True)

# Identify categorical columns by checking for object data type
categorical_columns=[col for col in data.columns if data[col].dtype=='object']
categorical_columns

# Calculate the range of 'Exam_Score' (max - min)
max_score = data['Exam_Score'].max()
min_score = data['Exam_Score'].min()
score_range = max_score - min_score
print(f"\nRange of Exam Scores: low: {min_score} to high: {max_score}")


# page title
st.title('Exam Score Analysis for DARA Project')

# Scatter plot 
st.subheader('Hours Studied vs Exam Score by Gender')
fig1 = plt.figure(figsize=(10, 8))
sns.scatterplot(x='Hours_Studied', y='Exam_Score', hue='Gender', data=data, palette='Set1')
plt.title('Hours Studied vs Exam Score by Gender')
st.pyplot(fig1)  

# Histogram 
st.subheader('Distribution of Exam Scores')
fig2 = plt.figure(figsize=(8, 6))
sns.histplot(data['Exam_Score'], kde=True, color='green')
plt.title('Distribution of Exam Scores')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')
st.pyplot(fig2)

# Categorical features versus Exam Score
st.subheader('Categorical Features vs Exam Score')
for col in categorical_columns:
    st.write(f"**{col}**")  
    fig3, axes = plt.subplots(1, 2, figsize=(14, 6))  

    sns.boxplot(x=data[col], y=data['Exam_Score'], palette='Set2', ax=axes[0])
    axes[0].set_title(f'Boxplot of Exam Score by {col}')
    axes[0].tick_params(axis='x', rotation=45)  

    sns.scatterplot(x=data[col], y=data['Exam_Score'], color='brown', ax=axes[1])
    axes[1].set_title(f'Scatterplot of Exam Score by {col}')
    axes[1].tick_params(axis='x', rotation=45)

    st.pyplot(fig3)  
    st.markdown("---")  
    


