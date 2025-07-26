from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']
    result = {
        "crop": "Maize",
        "pest": "Fall Armyworm",
        "severity": "High",
        "suggestion": "Spray Emamectin Benzoate 5% SG"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
