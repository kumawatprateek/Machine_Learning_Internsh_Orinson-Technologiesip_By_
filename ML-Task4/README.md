# Student Performance Prediction Using Machine Learning

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [User Input for Predictions](#user-input-for-predictions)
- [Visualizations](#visualizations)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to predict student performance using various machine learning algorithms. The model predicts whether a student is likely to pass or fail based on their study habits, attendance rates, previous grades, parental education levels, and participation in extracurricular activities. 

The project includes data preprocessing, model training using logistic regression, evaluation of the model performance, and visualizations to understand the data better.

## Dataset
The dataset used in this project is named `student_performance_prediction.csv`. It contains the following features:
- **Student ID**: Unique identifier for each student.
- **Study Hours per Week**: Number of hours a student studies each week.
- **Attendance Rate**: Percentage of classes attended by the student.
- **Previous Grades**: Student's previous grades in percentage.
- **Participation in Extracurricular Activities**: Indicates whether the student participates in extracurricular activities (Yes/No).
- **Parent Education Level**: Highest education level attained by the student's parents (e.g., High School, Associate, Bachelor, Master).
- **Passed**: Target variable indicating whether the student passed (Yes) or failed (No).

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Seaborn
- Matplotlib

## Installation
To run this project, follow these steps:

1. Clone the repository:
   ```bash
   github.com/kumawatprateek/Machine_Learning_Internship_By_Orinson-Technologies/tree/main/ML-Task4
   ```

2. Navigate to the project directory:
   ```bash
   cd student-performance-prediction
   ```

3. Install the required packages:
   ```bash
   pip install pandas numpy scikit-learn seaborn matplotlib
   ```

## Usage
1. Load the dataset by ensuring `student_performance_prediction.csv` is in the project directory.
2. Run the Jupyter Notebook file (or Python script) provided in the repository.
3. Follow the steps outlined in the notebook for data preprocessing, model training, and predictions.

## Model Training and Evaluation
- The dataset is split into training and testing sets to evaluate the model's performance.
- A logistic regression model is trained on the training set.
- The model is evaluated using metrics such as accuracy, confusion matrix, and classification report.

## User Input for Predictions
The model allows users to input specific data about a student to predict whether they are likely to pass or fail. The user is prompted for:
- Study Hours per Week
- Attendance Rate
- Previous Grades
- Participation in Extracurricular Activities (Yes/No)
- Parent Education Level

## Visualizations
Visualizations are provided to help understand the relationships between different features and student performance. Key visualizations include:
- Scatter plot of Study Hours vs. Previous Grades.
- Histogram of Attendance Rate distribution by Pass/Fail status.
- ROC curve to evaluate the model's performance.

### Example of the Dataset

| Student ID | Study Hours per Week | Attendance Rate | Previous Grades | Participation in Extracurricular Activities | Parent Education Level | Passed |
|------------|----------------------|------------------|------------------|----------------------------------------------|------------------------|--------|
| S00001     | 12.5                 | NaN              | 75.0             | Yes                                          | Master                 | Yes    |
| S00002     | 9.3                  | 95.3             | 60.6             | No                                           | High School            | No     |


## Results
The model achieved an accuracy of approximately **52.59%** on the test dataset. The confusion matrix and classification report provide insights into the model's prediction performance.

## Contributing
Contributions to improve the project are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
