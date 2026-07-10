import pickle
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

DATA_URL = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv'

# Match the notebook's preprocessing and encoding
clean_data = {
    'sex': {'male': 1, 'female': 0},
    'smoker': {'no': 0, 'yes': 1},
    'region': {'northwest': 0, 'northeast': 1, 'southeast': 2, 'southwest': 3},
}

data = pd.read_csv(DATA_URL)
data_copy = data.copy().replace(clean_data)

X = data_copy[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = data_copy['charges']

model = GradientBoostingRegressor(max_depth=2, n_estimators=100, learning_rate=0.2)
model.fit(X, y)

with open('gbr.pkl', 'wb') as f:
    pickle.dump(model, f)

print('Saved model to gbr.pkl based on the notebook training workflow')
