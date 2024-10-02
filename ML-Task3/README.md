# Predicting India's Per Capita Income Based on GDP Using Linear Regression

## Overview

This project focuses on predicting India's per capita income using GDP as the primary independent variable. The prediction is performed using a linear regression model, which establishes a relationship between GDP and per capita income to make future projections. 

The project is implemented using Python and leverages data manipulation, visualization, and machine learning libraries such as Pandas, Matplotlib, and Scikit-learn. The objective is to demonstrate how economic factors like GDP can be used to predict per capita income in a country.

## Table of Contents
- [Project Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The dataset used for this project includes data points on India's Gross Domestic Product (GDP) and corresponding per capita income figures over several years. The data is sourced from publicly available economic datasets.

- **Features:**
  - Year: The year of record.
  - GDP: The Gross Domestic Product of India for the respective year.

- **Target:**
  - Per Capita Income: The calculated per capita income for the respective year.

The dataset can be loaded into the project via a CSV file or directly fetched using any API (if available).

## Installation

To run this project, you will need Python 3.x and several Python libraries. You can install the required libraries using `pip` by running the following command:

```bash
pip install -r requirements.txt
```

The primary dependencies include:
- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/per-capita-income-prediction.git
   cd per-capita-income-prediction
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook or script to train the model and make predictions:

   ```bash
   jupyter notebook "Predicting India's Per Capita Income Based on GDP Using Linear Regression.ipynb"
   ```

4. Follow along with the notebook to visualize the data, train the model, and evaluate its performance.

### Example

The code below shows a basic usage of the linear regression model implemented in this project:

```python
# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('India_GDP_Data.csv')

# Split data into training and testing sets
X = data[['GDP']]
y = data['Per Capita Income']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Visualize the results
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('GDP vs Per Capita Income')
plt.xlabel('GDP')
plt.ylabel('Per Capita Income')
plt.show()
```

## Model Evaluation

The model is evaluated using several metrics, including:
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R-squared (R²) score**

These metrics help to determine how well the linear regression model fits the data and how accurate the predictions are.

## Results

The project concludes with predictions of per capita income based on India's GDP data. The linear regression model provides a simple yet effective way to understand how changes in GDP affect per capita income.

The visualizations in the project demonstrate the relationship between GDP and per capita income and highlight the model's prediction accuracy.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome, from code enhancements to documentation improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
