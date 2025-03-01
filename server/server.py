from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    response = jsonify({
        'locations': util.home()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    location = request.form['location']
    sqft = float(request.form['sqft'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    response = jsonify({
        'estimated_price': util.estimate_price(location, sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print('Server is running')
    app.run()