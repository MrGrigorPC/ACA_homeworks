import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from knn import KNN
data = load_breast_cancer()
X, y = data.data, data.target
# Divide data into train and test splits
# Fill in the code here
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.4)
# Load your KNN class from knn.py and instantiate it with k=3
my_model = KNN(3)
# Fill in the code here
# Fit your KNN classifier on the training data
# Fill in the code here
my_model.fit(X_train, y_train)
# Use your KNN classifier to predict labels for the test data
my_model_predictions = my_model.predict(X_test)
#  Fill in the code here
# Compare the results with sklearn's KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
sklearn_knn = KNeighborsClassifier(n_neighbors=3)
sklearn_knn.fit(X_train, y_train)
sklearn_predictions = sklearn_knn.predict(X_test)
# Compare the predictions from both classifiers
from sklearn.metrics import accuracy_score
print(f"Accuracy of scikit learn model {accuracy_score(y_test, sklearn_predictions)}")
print(f"Accuracy of our model {accuracy_score(y_test, my_model_predictions)}")
# Fill in the code here