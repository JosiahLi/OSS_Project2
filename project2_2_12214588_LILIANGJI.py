# %%
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


def sort_dataset(dataset_df):
    # TODO: Implement this function
    return dataset_df.sort_values(by='year', ascending=True)


def split_dataset(dataset_df):
    # TODO: Implement this function
    data = dataset_df.drop("salary", axis=1)
    label = dataset_df['salary'] * 0.001
    return data[:1718], data[1718:], label[:1718], label[1718:]


def extract_numerical_cols(dataset_df):
    # TODO: Implement this function
    num_col = ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly',
               'war']
    return dataset_df[num_col]


def train_predict_decision_tree(X_train, Y_train, X_test):
    # TODO: Implement this function
    dt_reg = DecisionTreeRegressor()
    dt_reg.fit(X_train, Y_train)
    return dt_reg.predict(X_test)


def train_predict_random_forest(X_train, Y_train, X_test):
    # TODO: Implement this function
    rf_reg = RandomForestRegressor()
    rf_reg.fit(X_train, Y_train)
    return rf_reg.predict(X_test)


def train_predict_svm(X_train, Y_train, X_test):
    # TODO: Implement this function
    pipe = make_pipeline(StandardScaler(), SVR())
    pipe.fit(X_train, Y_train)
    return pipe.predict(X_test)


def calculate_RMSE(labels, predictions):
    # TODO: Implement this function
    return np.sqrt(np.mean((predictions - labels) ** 2))


if __name__ == '__main__':
    # DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
    data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

    sorted_df = sort_dataset(data_df)
    X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

    X_train = extract_numerical_cols(X_train)
    X_test = extract_numerical_cols(X_test)

    dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
    rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
    svm_predictions = train_predict_svm(X_train, Y_train, X_test)

    print("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
    print("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
    print("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))
