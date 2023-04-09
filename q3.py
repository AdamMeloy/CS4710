import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# 2. (Glass Dataset)

glass_df = pd.read_csv('Dataset/glass.csv')

# 1. Implement Naïve Bayes method using scikit-learn library.
# a. Use the glass dataset available in Link also provided in your assignment.

X = glass_df.iloc[:, :-1].values
y = glass_df.iloc[:, -1].values

# b. Use train_test_split to create training and testing part.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

X_train = glass_df.iloc[:, :-1].values
y_train = glass_df.iloc[:, -1].values

X_test = glass_df.iloc[:, :-1].values
y_test = glass_df.iloc[:, -1].values

# 2. Evaluate the model on testing part using score and
# classification_report(y_true, y_pred)pip

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(f'gaussian naive bayes\n{classification_report(y_test, y_pred)}')

# Accuracy score
print(f'accuracy is {accuracy_score(y_pred, y_test)}\n')

# 1. Implement linear SVM method using scikit library
# a. Use the glass dataset available in Link also provided in your assignment.
# b. Use train_test_split to create training and testing part.

# 2. Evaluate the model on testing part using score and
# Do at least two visualizations to describe or show correlations in the Glass Dataset.

classifier = SVC(kernel='linear')
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(f'linear svm\n{classification_report(y_test, y_pred)}')

# Accuracy score
print(f'accuracy is {accuracy_score(y_pred, y_test)}\n')

# Which algorithm you got better accuracy? Can you justify why?
# Linear SVM resulted in a higher accuracy overall, and has higher averages for precision, recall, and f1-score.
