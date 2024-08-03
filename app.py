from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
app = Flask(__name__)
data = pd.read_csv('housing.csv')
data.dropna(inplace=True)
data['total_rooms'] = np.log1p(data['total_rooms'])
data['total_bedrooms'] = np.log1p(data['total_bedrooms'])
data['population'] = np.log1p(data['population'])
data['households'] = np.log1p(data['households'])
data = data.join(pd.get_dummies(data.ocean_proximity)).drop(['ocean_proximity'], axis=1)

X = data.drop(['median_house_value'], axis=1)
y = data['median_house_value']
dt_regressor = DecisionTreeRegressor(random_state=42)
dt_regressor.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    bedroom_ratio = float(request.form['bedroom_ratio'])
    population_level = request.form['population']
    income_level = float(request.form['median_income'])

    population = data['population'].quantile(0.75) if population_level == 'high' else data['population'].quantile(0.25)

    new_data = pd.DataFrame({
        'bedroom_ratio': [bedroom_ratio],
        'population': [population],
        'median_income': [income_level],
        'total_rooms': [data['total_rooms'].mean()],
        'total_bedrooms': [data['total_bedrooms'].mean()],
        'households': [data['households'].mean()],
        'longitude': [data['longitude'].mean()],
        'latitude': [data['latitude'].mean()],
    })

    for column in X.columns:
        if column not in new_data.columns:
            new_data[column] = 0

    new_data = new_data[X.columns]
    prediction = dt_regressor.predict(new_data)

    return render_template('result.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
