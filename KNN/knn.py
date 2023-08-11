from collections import Counter
class KNN:
    def __init__(self, k=3):
        """
        Initialize the KNN classifier with a given value of K.

        Parameters:
        k (int): The number of nearest neighbors to consider for classification (default is 3).
        """
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        """
        Fit the KNN classifier to the training data.

        Parameters:
        X_train (array-like, shape (n_samples, n_features)): The training data features.
        y_train (array-like, shape (n_samples,)): The corresponding training data labels.
        """
        self.X_train = X_train
        self.y_train = y_train

    def euclidean_distance(self, point1, point2):
        """
        Calculate the Euclidean distance between two points.

        Parameters:
        point1 (array-like, shape (n_features,)): The first point coordinates.
        point2 (array-like, shape (n_features,)): The second point coordinates.

        Returns:
        float: The Euclidean distance between the two points.
        """
        # Implement the Euclidean distance calculation here
        euc_distance = 0;
        for i in range(len(point1)):
          euc_distance += (point1[i] - point2[i])**2
        return euc_distance**(1/2)
    def predict(self, X_test):
        """
        Predict the class labels for test data using the KNN classifier.

        Parameters:
        X_test (array-like, shape (n_samples, n_features)): The test data features.

        Returns:
        array-like, shape (n_samples,): The predicted class labels for the test data.
        """
        # Implement the prediction logic using KNN here
        predictions = []
        for test_point in X_test:
          distances = []
          for train_point, train_label in zip(self.X_train, self.y_train):
              distance = self.euclidean_distance(test_point, train_point)
              distances.append((distance, train_label))
          distances.sort(key = lambda x : x[0])
          k_nearest = distances[:self.k]
          k_nearest_labels = map(lambda x: x[1], k_nearest)
          predictions.append(Counter(k_nearest_labels).most_common()[0][0])
        return predictions