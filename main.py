from preprocessing import preprocess
from prediction import predict

X_train, y_train, X_test, y_test, X_predict, y_predict, scaler_y = preprocess()

predict(X_predict, y_predict, scaler_y)