import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# 1. (Titanic Dataset)

train_df = pd.read_csv('Dataset/train.csv')
test_df = pd.read_csv('Dataset/test.csv')

# 1. Find the correlation between ‘survived’ (target column) and ‘sex’ column for the Titanic use case in class.
print('_' * 20)
print(train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))
print('_' * 20 + '\n')
# a. Do you think we should keep this feature?
# yes

# 2. Do at least two visualizations to describe or show correlations.

train_df.plot.hist(x='Survived', y='Age')
plt.show()

grid = sns.FacetGrid(train_df, row='Embarked', height=2.2, aspect=1.6)
grid.map(sns.pointplot, 'Pclass', 'Survived', 'Sex', palette='deep', order=[1, 2, 3], hue_order=None)
grid.add_legend()
plt.show()

# 3. Implement Naïve Bayes method using scikit-learn library and report the accuracy.

# Removing non-number columns and unfilled rows
train_df = train_df.drop(['Name', 'Ticket', 'Cabin', 'Survived'], axis=1)
test_df = test_df.drop(['Name', 'Ticket', 'Cabin'], axis=1)
combine = [train_df, test_df]

for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map({'female': 1, 'male': 0})
    dataset.dropna(axis=0, inplace=True)

X = train_df.iloc[:, :-1].values
y = train_df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

X_train = train_df.iloc[:, :-1].values
y_train = train_df.iloc[:, -1].values

X_test = test_df.iloc[:, :-1].values
y_test = test_df.iloc[:, -1].values

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Summary of the predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Accuracy score
print('accuracy is', accuracy_score(y_pred, y_test))
