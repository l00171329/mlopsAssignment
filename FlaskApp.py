from flask import Flask, request
from joblib import load
import numpy as np

app = Flask(__name__)
model = load("HousePriceModel.pkl")

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict_price():
    area = request.args.get('area')
    rooms = request.args.get('rooms')
    bedrooms = request.args.get('bedrooms')
    bathrooms = request.args.get('bathrooms')
    stories = request.args.get('stories')
    parking = request.args.get('parking')

    if any(arg is None for arg in [area, rooms, bedrooms, bathrooms, stories, parking]):
        return "Invalid input provided"

    try:
        area_float = float(area)
        rooms_int = int(rooms)
        bedrooms_int = int(bedrooms)
        bathrooms_int = int(bathrooms)
        stories_int = int(stories)
        parking_int = int(parking)
    except ValueError:
        return "Invalid input provided"

    prediction = model.predict([[area_float, rooms_int, bedrooms_int, bathrooms_int, stories_int, parking_int]])
    prediction = np.round(prediction[0], 2)
    return "The predicted house price is $" + str(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
