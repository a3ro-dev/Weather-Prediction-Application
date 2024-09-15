### README.md

# Weather Prediction Application

This repository contains a weather prediction application built using Streamlit. The application predicts future temperatures and weather types based on past trends. It provides a sleek and intuitive user interface for input and displays the predictions dynamically.

## Table of Contents
- Features
- Installation
- Usage
- [File Structure](#file-structure)
- Contributing
- License

## Features
- Predict future temperatures and weather types based on past data.
- Dynamic and interactive UI built with Streamlit.
- Real-time progress updates and animated feedback during prediction.
- Option to visualize temperature predictions on a graph.
- Customizable input for previous and current temperatures and weather types.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/weather-prediction-app.git
    cd weather-prediction-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

3. Enter the required inputs for previous and current temperatures and weather types, select the number of times to predict, and the time of day. Click the "Predict" button to see the results.

## File Structure
```
weather-prediction-app/
│
├── modules/
│   └── weatherModel.py  # Contains the WeatherModel class for temperature and weather prediction
│
├── main.py              # Main Streamlit application file
│
├── requirements.txt     # List of required Python packages
│
└── README.md            # This README file
```

### weatherModel.py
This file contains the [`WeatherModel`] class, which is responsible for predicting temperatures and weather types based on past data. Key methods include:
- [`predict_temperature`]: Predicts future temperatures using exponential smoothing.
- [`predict_weather_type`]: Predicts future weather types based on past trends.
- [`predict`]: Combines temperature and weather type predictions.
- [`display_predictions`]: Prints the predicted temperatures and weather types.

### main.py
This file contains the Streamlit application code. It sets up the user interface, handles user inputs, and displays the predictions. Key functions include:
- [`perform_calculations`]: Simulates backend calculations with animated feedback and updates the progress bar.
- Streamlit UI setup: Initializes the app layout, input fields, and prediction results display.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.