from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('galactus.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(data)
    return jsonify({'prediction': str(prediction)})

if __name__ == '__main__':
    app.run(port=8080)
