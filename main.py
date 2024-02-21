from preprocessing import preprocess
from prediction import predict
from flask import Flask, request
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

X_train, y_train, X_test, y_test, X_predict, y_predict, scaler_y = preprocess()
predictions, GroundTruths = predict(X_predict, y_predict, scaler_y)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict', methods=['Get'])
def predict():

    """Predicts the Mass for the Test dataset and prints 
    the Mass of the chosen particle.
    ---
    parameters:
        - name : line_number
          in : query
          type : number
          required : true
    responses:
        200:
            description : The output values
    """

    line_number=request.args.get('line_number')
    return 'The predicted value is ' + str(predictions[int(line_number)]) + ". And the Ground truth is " + str(GroundTruths[int(line_number)])

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=int("1000"), debug=True)