import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.preprocessing import LabelEncoder

def apply_model(dataset_path, model_name):
    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Assume the last column is the target variable
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Encode categorical variables
    le = LabelEncoder()
    for column in X.select_dtypes(include=['object']):
        X[column] = le.fit_transform(X[column])

    # Encode target variable if it's categorical
    if y.dtype == 'object':
        y = le.fit_transform(y)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Select and train the model
    if model_name == 'linear_regression':
        model = LinearRegression()
        metric_name = 'Mean Squared Error'
    elif model_name == 'logistic_regression':
        model = LogisticRegression()
        metric_name = 'Accuracy'
    elif model_name == 'decision_tree':
        model = DecisionTreeClassifier()
        metric_name = 'Accuracy'
    elif model_name == 'random_forest':
        model = RandomForestClassifier()
        metric_name = 'Accuracy'
    else:
        raise ValueError(f"Unknown model: {model_name}")

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate the performance metric
    if metric_name == 'Accuracy':
        metric_value = accuracy_score(y_test, y_pred)
    else:
        metric_value = mean_squared_error(y_test, y_pred)

    return f"Model: {model_name}\n{metric_name}: {metric_value:.4f}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ml_script.py <dataset_path> <model_name>")
        sys.exit(1)

    dataset_path = sys.argv[1]
    model_name = sys.argv[2]

    try:
        result = apply_model(dataset_path, model_name)
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")