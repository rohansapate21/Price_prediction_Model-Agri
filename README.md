# Crop Price Prediction Application

This application uses a Random Forest machine learning model to predict crop prices based on various factors including year, month, district, crop type, and rainfall.

## Features

- Predict crop prices based on input parameters
- Visualize price trends throughout the year
- View predictions in both chart and table formats

## Installation

### For Windows Users:

1. Simply double-click the `setup.bat` file to install all required dependencies.
2. Follow the on-screen instructions.

### For All Users:

1. Open a terminal or command prompt
2. Navigate to the application directory
3. Run the setup script:
   ```
   python setup.py
   ```

## How to Run the Application

### For Windows Users:

1. After installation, double-click the `start_app.bat` file to launch the application.
2. Your default web browser will automatically open with the application interface.
3. The Flask server will run in the background.
4. To stop the application, close the command prompt window.

### For All Users:

1. Open a terminal or command prompt
2. Navigate to the application directory
3. Run the start script:
   ```
   python start_app.py
   ```
4. Your default web browser will open with the application interface
5. Press Ctrl+C in the terminal when you want to stop the application

## Using the Application

1. Fill in all the required fields in the form:
   - Year: The year for price prediction
   - Month: The specific month you're interested in
   - District: The agricultural district
   - Crop: The type of crop for price prediction
   - Rainfall: The amount of rainfall in millimeters

2. Click "Predict Price" to generate the prediction

3. View the results:
   - A line chart showing the predicted price trend across all months
   - A table displaying the detailed price predictions for each month

## Troubleshooting

If you encounter any issues:
1. Make sure all required Python packages are installed by running the setup script
2. Check that the Python version is 3.6 or higher
3. Verify that the model file `random_forest_model.pkl` is present in the application directory

## Credits

This application uses:
- Flask for the backend API
- Chart.js for data visualization
- Random Forest algorithm for price prediction 