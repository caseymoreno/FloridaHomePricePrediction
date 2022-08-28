from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Contrl-Allow-Origin', '*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    sq_feet = float(request.form['sq_feet'])
    location = (request.form['location'])
    beds = int(request.form['beds'])
    baths = float(request.form['baths'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,beds,sq_feet,baths)
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()