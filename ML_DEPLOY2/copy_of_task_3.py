# -*- coding: utf-8 -*-
"""Copy of TASK_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oZzU3erfijIr3PmZYDfecoWTJpO6Y3vm

##Richa Patel

##60009230202

##ML TASK 3

##Importing Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
# %matplotlib inline

df=pd.read_csv(r"C:\Users\patel\Desktop\ML_DEPLOY2\injury_data.csv")

df.head()

df['Player_Weight'] = df['Player_Weight'].round(2)
df['Player_Height'] = df['Player_Height'].round(2)
df['Training_Intensity'] = df['Training_Intensity'].round(2)

df.head()

"""##Checking Data"""

df_info = pd.DataFrame(df.dtypes, columns=['Dtype'])
df_info['Unique'] = df.nunique().values
df_info['Null'] = df.isnull().sum().values
df_info

df.describe()

"""##Creating New Columns:
 one containing the BMI and the other Age Categories.

BMI

The Body Mass Index (BMI) is a measure used to assess whether a person has a healthy weight in relation to their height. It is calculated by dividing weight (in kilograms) by height squared (in meters).
"""

# Calculate BMI
df['BMI'] = df['Player_Weight'] / ((df['Player_Height'] / 100) ** 2)  # Convert height to meters

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obesity'

# Apply classification
df['BMI_Category'] = df['BMI'].apply(classify_bmi)

# Display the first few rows with BMI and BMI_Category
df[['Player_Weight', 'Player_Height', 'BMI', 'BMI_Category']].head()

df.head()

df.shape

print('Player Age Min: {}'.format(df.Player_Age.min()))
print('Player Age Max: {}'.format(df.Player_Age.max()))

"""Age Groups

##Exploratory Data Analysis
"""

def plot_histogram_kde_and_boxplot(dataframe, column, color_column):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    for ax in axs:
        ax.grid(False)
        for spine in ax.spines.values():
            spine.set_visible(False)

    sns.histplot(data=dataframe, x=column, bins=20, color='skyblue', edgecolor='black', kde=True, ax=axs[0])

    axs[0].set_xlabel('')
    axs[0].set_ylabel('')
    axs[0].set_title(f'{column} Histogram', weight='bold', size=13)

    sns.kdeplot(data=dataframe, x=column, color='skyblue', fill=True, hue=color_column, palette={0: 'green', 1: 'red'}, ax=axs[1])
    axs[1].set_xlabel('')
    axs[1].set_ylabel('')
    axs[1].set_title(f'{column} Density', weight='bold', size=13)

    sns.boxplot(data=dataframe[column], orient='h', ax=axs[2])

    axs[2].set_xlabel('')
    axs[2].set_ylabel('')
    axs[2].set_title(f'{column} Boxplot', weight='bold', size=13)

    plt.tight_layout()

    plt.show()

def plot_dual_chart(dataframe, column1, column2, cat_order=None, y_limit1=None, y_limit2=None):
    fig, axs = plt.subplots(1, 2, figsize=(18, 6))

    for ax in axs:
        ax.grid(False)
        for spine in ax.spines.values():
            spine.set_visible(False)

    sns.histplot(data=dataframe, x=column1, bins=20, color='skyblue', edgecolor='black', kde=True, ax=axs[0])
    axs[0].set_title(f'{column1} Histogram', weight='bold', size=13)
    axs[0].set_xlabel('')
    axs[0].set_ylabel('')

    if y_limit1 is None:
        y_limit1 = dataframe[column1].max() * 1.1
    axs[0].set_ylim(top=y_limit1)

    ax = sns.countplot(data=dataframe, x=column2, hue='Likelihood_of_Injury', palette={0: 'lightsalmon', 1: 'mediumaquamarine'}, ax=axs[1], linewidth=2, order=cat_order)

    axs[1].set_xlabel('')
    axs[1].set_ylabel('')
    axs[1].set_title(f'{column2} x Likelihood_of_Injury', weight='bold', size=13)

    axs[1].tick_params(axis='x', rotation=0)

    axs[1].grid(False)

    axs[1].legend()

    if y_limit2 is None:
        y_limit2 = dataframe[column2].value_counts().max() * 1.1  # Max value multiplied by 1.1 to ensure a margin
    axs[1].set_ylim(top=y_limit2)

    for p in axs[1].patches:
        height = p.get_height()
        if not np.isnan(height):
            axs[1].annotate(str(int(height)), (p.get_x() + p.get_width() / 2., height),
                            ha='center', va='center', xytext=(0, 5), textcoords='offset points', color='black', weight='bold', size=13)
        else:
            axs[1].annotate("0", (p.get_x() + p.get_width() / 2., 0),
                            ha='center', va='center', xytext=(0, 5), textcoords='offset points', color='black', weight='bold', size=13)

    plt.tight_layout()

    plt.show()

"""Age_Group

We can observe an increase in the proportion of players with injury probability in the age range of 27 to 30 years, compared to the other groups.

BMI_Classification
"""

plot_dual_chart(df, 'BMI', 'BMI_Category', y_limit1=180, y_limit2=350)

"""Player_Weight"""

plot_histogram_kde_and_boxplot(df, 'Player_Weight', 'Likelihood_of_Injury')

"""Player_Height"""

plot_histogram_kde_and_boxplot(df, 'Player_Height', 'Likelihood_of_Injury')

"""Training_Intensity

We can observe that the patterns of injury probability invert in the density plot. In training sessions with lower intensity, the number of players without risk of injury exceeds the number of players at risk, while in training sessions with higher intensity, the number of players at risk of injury surpasses those without risk.
"""

plot_histogram_kde_and_boxplot(df, 'Training_Intensity', 'Likelihood_of_Injury')

"""Recovery_Time"""

plot_histogram_kde_and_boxplot(df, 'Recovery_Time', 'Likelihood_of_Injury')

"""Likelihood_of_Injury"""

li_count = df['Likelihood_of_Injury'].value_counts()

# Plot pie chart | Plotar o gráfico de pizza
plt.figure(figsize=(5, 5))
plt.pie(li_count, labels=li_count.index, autopct='%1.1f%%', startangle=140, colors=['#8CFCA4', '#FF6961'])
plt.title('Distribution of Likelihood_of_Injury', weight='bold', size=13)
plt.axis('equal')
plt.show()

"""Our target column, Likelihood_of_Injury, displays a perfectly balanced data distribution

##Data Preprocessing

Through the OneHotEncoder, we will transform the categorical variables into binary numeric representations.
"""

import pandas as pd

# Assuming your dataset is stored in a DataFrame called 'df'

# Perform one-hot encoding on 'BMI_Category'
df_encoded = pd.get_dummies(df, columns=['BMI_Category'])

# Display the encoded dataset
df_encoded.head()

"""Correlation Between Columns"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Compute the correlation matrix
correlation_matrix = df_encoded.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Correlation Heatmap')
plt.show()

"""The heatmap reveals a positive correlation between height and being overweight, suggesting taller players might be more prone to overweight conditions. BMI unsurprisingly has strong positive correlations with weight, and age groups show expected patterns with negative correlations between younger and older groups. Interestingly, there's a weak positive correlation between all BMI classifications, potentially due to their relation to body mass.

##Training Models
"""

from sklearn.model_selection import train_test_split

X = df_encoded.iloc[:, :6]  # Columns up to 'Recovery_Time'

# Selecting the target variable 'Likelihood_of_Injury'
y = df_encoded['Likelihood_of_Injury']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.head()

X_test.head(5)

"""##Decision Tree"""

from sklearn.tree import DecisionTreeClassifier

dec_tree_model=DecisionTreeClassifier()
dec_tree_model.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix
y_pred=dec_tree_model.predict(X_test)
cm=confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

dec_tree_acc=dec_tree_model.score(X_test, y_test)
print("Decision Accuracy: {:.2f}%" .format(dec_tree_acc * 100))

"""##Logistic Regression"""

from sklearn.linear_model import LogisticRegression

log_reg_model=LogisticRegression()
log_reg_model.fit(X_train,y_train)

y_pred=log_reg_model.predict(X_test)
cm=confusion_matrix(y_test, y_pred)
print(cm)

print(classification_report(y_test, y_pred))

log_reg_acc=log_reg_model.score(X_test, y_test)
print("Decision Accuracy: {:.2f}%" .format(log_reg_acc * 100))

"""##Random Forest"""

from sklearn.ensemble import RandomForestClassifier

ran_forest_model=RandomForestClassifier()
ran_forest_model.fit(X_train,y_train)

y_pred=ran_forest_model.predict(X_test)
cm=confusion_matrix(y_test, y_pred)
print(cm)

ran_forest_acc=ran_forest_model.score(X_test, y_test)
print("Decision Accuracy: {:.2f}%" .format(ran_forest_acc * 100))

"""##Gradient Boosting"""

from sklearn.ensemble import GradientBoostingClassifier

grad_bossting_model=GradientBoostingClassifier()
grad_bossting_model.fit(X_train,y_train)

y_pred=grad_bossting_model.predict(X_test)
cm=confusion_matrix(y_test, y_pred)
print(cm)

grad_bossting_acc=grad_bossting_model.score(X_test, y_test)
print("Decision Accuracy: {:.2f}%" .format(grad_bossting_acc * 100))

"""##Support Vector Machine"""

from sklearn.svm import LinearSVC

supp_vector_model=LinearSVC()
supp_vector_model.fit(X_train, y_train)

y_pred=supp_vector_model.predict(X_test)
cm=confusion_matrix(y_test, y_pred)
print(cm)

supp_vec_acc=supp_vector_model.score(X_test, y_test)
print("Decision Accuracy: {:.2f}%" .format(supp_vec_acc * 100))

model_names= ["Decision Tree","Logistic Regression", "Random Forest Classifier","Gradient Boosting","LinearSVC"]
accuracies=[dec_tree_acc, log_reg_acc, ran_forest_acc,grad_bossting_acc, supp_vec_acc]

import numpy as np
import matplotlib.pyplot as plt
colors = plt.cm.viridis(np.linspace(0, 1, len(model_names)))

plt.figure(figsize=(10, 8))

bars = plt.bar(model_names, accuracies, color=colors)

plt.ylabel('Accuracy')

plt.title('Accuracy of Different Models')

plt.xticks(rotation=45, ha='right')

for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, f'{acc:.2f}',
             ha='center', va='bottom')

plt.show()

"""Hence we are done performing Exploratory Data Analysis and Preprocessing On Dataset.

doing hyper parameter tuning
"""

import pickle
filename="savemodel.pkl"
pickle.dump(ran_forest_model, open(filename, 'wb'))

