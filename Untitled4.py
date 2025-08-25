#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HR Analytics - Predict Attrition using Pandas, Sklearn, Seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


df = pd.read_csv(r'C:\Users\vijay sharma\Downloads\WA_Fn-UseC_-HR-Employee-Attrition.csv')  # Replace with your file path

print(df.head())
print(df.info())




# In[23]:


df['Attrition'] = df['Attrition'].apply(lambda x: 1 if str(x).strip().lower() in ['yes', '1'] else 0)


print("\nOverall Attrition Rate:", df['Attrition'].mean())


if 'Department' in df.columns:
    dept_attrition = df.groupby('Department')['Attrition'].mean().sort_values(ascending=False)
    print("\nDepartment-wise Attrition:\n", dept_attrition)

    plt.figure(figsize=(8,5))
    sns.barplot(x=dept_attrition.index, y=dept_attrition.values, palette="viridis")
    plt.title('Attrition Rate by Department')
    plt.ylabel('Attrition Rate')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


if 'MonthlyIncome' in df.columns:
    df['SalaryBand'] = pd.qcut(df['MonthlyIncome'], 5, labels=['Very Low','Low','Medium','High','Very High'])
    salary_attrition = df.groupby('SalaryBand')['Attrition'].mean()
    print("\nAttrition by Salary Band:\n", salary_attrition)

    plt.figure(figsize=(8,5))
    sns.barplot(x=salary_attrition.index, y=salary_attrition.values, palette="coolwarm")
    plt.title('Attrition by Salary Band')
    plt.ylabel('Attrition Rate')
    plt.tight_layout()
    plt.show()


if 'YearsSinceLastPromotion' in df.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x='Attrition', y='YearsSinceLastPromotion', data=df, palette="pastel")
    plt.title('Promotion Gap vs Attrition')
    plt.show()



# In[2]:


df_clean = df.copy()

categorical_cols = df_clean.select_dtypes(include='object').columns

from sklearn.preprocessing import OrdinalEncoder


if len(categorical_cols) > 0:
    encoder = OrdinalEncoder()
    df_clean[categorical_cols] = encoder.fit_transform(df_clean[categorical_cols])


X = df_clean.drop('Attrition', axis=1)
y = df_clean['Attrition']


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)


from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression(max_iter=1000, random_state=42)
log_model.fit(X_train, y_train)

y_pred_log = log_model.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
print("\n--- Logistic Regression Results ---")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))
print("Classification Report:\n", classification_report(y_test, y_pred_log))


from sklearn.tree import DecisionTreeClassifier
tree_model = DecisionTreeClassifier(max_depth=5, random_state=42)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

print("\n--- Decision Tree Results ---")
print("Accuracy:", accuracy_score(y_test, y_pred_tree))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_tree))
print("Classification Report:\n", classification_report(y_test, y_pred_tree))


# In[ ]:




