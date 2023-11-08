from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the food data CSV file into a pandas DataFrame
food_data = pd.read_csv('food_data.csv')

# Function to predict nutrients based on the food item
def predict_nutrients(food_item):
    # Your code to predict nutrients based on the food item goes here
    # For example, you can use the loaded food_data DataFrame to look up nutrients for the given food_item
    nutrients = food_data.loc[food_data['Food Item'] == food_item, ['Carbohydrates', 'Fats', 'Proteins']].to_dict(orient='records')
    return nutrients[0] if nutrients else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the food_item from the request data
    food_item = request.form['food-item']

    # Call the predict_nutrients() function with the food_item argument
    nutrients = predict_nutrients(food_item)

    # Check if nutrients are found for the given food_item
    if nutrients:
        # Return the nutrients as a response in JSON format
        return jsonify(nutrients)
    else:
        # Return an error message if nutrients are not found for the given food_item
        return jsonify({'error': 'Nutrients not found'})

if __name__ == '__main__':
    app.run(debug=True)
