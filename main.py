import numpy
import joblib
from flask import Flask,jsonify


app = Flask(__name__)
model=joblib.load("model.joblib")

#
#@app.route('/predict_api',methods=['POST'])
#def predict_api():
   # '''
    #For direct API calls trought request
    #'''
    #data = request.get_json(force=True)
    #prediction = model.predict([np.array(list(data.values()))])

    #output = prediction[0]
    #return jsonify(output)
@app.route('/predict_api/<int:feature1>/<int:feature2>/<int:feature3>/<int:feature4>', methods=['GET'])
def predict_api(feature1, feature2, feature3, feature4):
    # Convert the input features to a numpy array
    input_data = numpy.array([[feature1, feature2, feature3, feature4]])

    # Make the prediction using the model
    prediction = model.predict(input_data)

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
