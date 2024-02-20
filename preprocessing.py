import pandas as pd
from config.configuration import Config
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess():
    columns_to_drop = ['Run', 'Event']
    df = pd.read_csv(Config.data_dir)
    df = df.drop(columns=columns_to_drop)
    df = df.dropna(subset=['M'])
    X_columns = df.columns.difference(['M'])
    X_values = df[X_columns]
    y_values = df['M'].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X_values, y_values, random_state=42, test_size=0.2)
    X_test, X_predict, y_test, y_predict = train_test_split(X_test, y_test, random_state=42, test_size=0.01)
    scaler_X = StandardScaler()
    scaler_y = StandardScaler()

    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)
    X_predict = scaler_X.transform(X_predict)

    y_train = scaler_y.fit_transform(y_train.reshape(-1, 1)).flatten()
    y_test = scaler_y.transform(y_test.reshape(-1, 1)).flatten()

    return X_train, y_train, X_test, y_test, X_predict, y_predict, scaler_y
