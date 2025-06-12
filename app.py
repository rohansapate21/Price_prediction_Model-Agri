from flask import Flask, request, jsonify, send_file
import pickle
import numpy as np
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend to access backend

# Load the model once at startup
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Assuming the model expects inputs in order:
# Year, Month, District, Crop, Rainfall (all transformed to numeric internally if needed)
# For categorical features (District, Crop), encoding must be handled here similarly as used in training.
# For demonstration, I will assume District and Crop are categorical and map them to numeric indices here
# Ideally, encoding info should come from saved encoders or preprocessing pipeline.

# For this example, let's mock categorical encodings (replace these with your real mapping)
district_mapping = {
    'District1': 0,
    'District2': 1,
    'District3': 2,
    'District4': 3,
    'District5': 4,
}
crop_mapping = {
    'Wheat': 0,
    'Rice': 1,
    'Corn': 2,
    'Barley': 3,
    'Soybean': 4,
}

# Month names mapping for frontend display
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        year = int(data['year'])
        month = int(data['month'])
        district = data['district']
        crop = data['crop']
        rainfall = float(data['rainfall'])

        if district not in district_mapping or crop not in crop_mapping:
            return jsonify({'error': 'Unknown district or crop'}), 400

        district_num = district_mapping[district]
        crop_num = crop_mapping[crop]

        # Predict price for the given month input
        input_features = np.array([[year, month, district_num, crop_num, rainfall]])
        predicted_price = model.predict(input_features)[0]
        predicted_price = round(float(predicted_price), 2)

        # Create price trend data for all months of the selected year
        # For trend, to keep rainfall constant (as input rainfall) as example
        trend_prices = []
        for m in range(1, 13):
            feat = np.array([[year, m, district_num, crop_num, rainfall]])
            price = model.predict(feat)[0]
            price = round(float(price), 2)
            trend_prices.append(price)

        # Build response with months, prices, and requested month price
        response = {
            'year': year,
            'crop': crop,
            'months': month_names,
            'trend_prices': trend_prices,
            'requested_month': month_names[month-1],
            'requested_price': predicted_price,
            'table_data': []
        }

        # Build table data for all months
        for i, price in enumerate(trend_prices):
            response['table_data'].append({
                'year': year,
                'month': month_names[i],
                'price': price
            })

        return jsonify(response)

    except KeyError:
        return jsonify({'error': 'Missing required input fields'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid input type'}), 400
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

