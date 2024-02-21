from tensorflow import keras
from tensorflow.keras.models import load_model
from config.configuration import Config
import numpy as np


def predict(x, y, scaler_y):
    loaded_model = load_model(Config.model_path)
    raw_predictions = loaded_model.predict(np.array(x))
    final_predictions = scaler_y.inverse_transform(raw_predictions)
    # print(final_predictions[7], "------------", y[7])

    return final_predictions, y