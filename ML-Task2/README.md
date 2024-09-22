# Student Score Predictor 🎓📊

This project is a **machine learning**-powered **web application** that predicts the posttest scores of students based on a variety of features like school setting, teaching method, and pretest scores. The application is built using **Streamlit** for the frontend and a pre-trained **Random Forest model** for predictions.

## Features

- 🌐 **Web App Interface**: User-friendly interface built with Streamlit.
- 📈 **Posttest Score Prediction**: Predicts student posttest scores based on inputs such as school type, pretest scores, and more.
- ⚙️ **Random Forest Model**: The prediction is powered by a Random Forest model trained on student data.
- 📊 **Data Inputs**:
  - School setting (Urban, Suburban, Rural)
  - School type (Public, Non-Public)
  - Teaching method (Standard, Experimental)
  - Gender (Male, Female)
  - Lunch type (Free/Reduced, Standard)
  - Number of students in class
  - Pretest score

## Dataset

The dataset used for training the model contains information about students' test scores, including:
- `school`: Name of the school
- `school_setting`: The setting of the school (Urban, Suburban, or Rural)
- `school_type`: Type of the school (Public or Non-Public)
- `teaching_method`: The teaching method used (Standard or Experimental)
- `gender`: Gender of the student (Male or Female)
- `lunch`: Whether the student qualifies for free/subsidized lunch
- `pretest`: The pretest score of the student

## How to Run the Application 🚀

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/student-score-predictor.git
    cd student-score-predictor
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run main_app.py
    ```

4. **Input features**: Enter the required student details (school type, pretest score, etc.) and click the "Predict" button to see the predicted posttest score.

## Model Training 🧠

- The model used is a **Random Forest Regressor**, trained on the dataset.
- It predicts the posttest score based on the provided features.
- Below is a **visualization of the model's** performance, showing how well the predicted scores align with the actual scores.
- (mod1.png)
- The model file `rf_model.pkl` is loaded into the Streamlit app for predictions.

## Files in the Repository 📂

- `main_app.py`: The Streamlit application for the user interface and prediction logic.
- `Predict Test Scores of students.ipyn`: This Jupyter notebook processes the data, loads it, and builds the machine learning model.
- `rf_model.pkl`: The pre-trained Random Forest model used for predictions.
- `README.md`: This file, providing an overview of the project.
- `requirements.txt`: A list of dependencies needed to run the project.

## Installation and Setup

- Ensure you have Python 3.6+ installed.
- Install the necessary Python libraries by running:
    ```bash
    pip install -r requirements.txt
    ```

### Libraries Used:
- **Streamlit**: For building the web application.
- **Scikit-learn**: For the machine learning model.
- **Numpy**: For numerical operations.
- **Seaborn**: For creating visualizations and improving the aesthetics of plots.
- **Matplotlib**: For generating plots and visualizations to analyze data and model performance.
- **Pandas**: For data manipulation, including loading, cleaning, and processing the dataset.

## Future Improvements 🛠️

- Add more advanced models (e.g., Gradient Boosting or Neural Networks) and compare performance.
- Allow more feature inputs for better predictions.
- Deploy the app on platforms like **Heroku** or **Streamlit Cloud** for wider accessibility.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Contributions**: Feel free to fork this repository, submit pull requests, or create issues for suggestions and bug reports.

### Author:
- **[Prateek Kumawat]** - [GitHub](https://github.com/kumawatprateek)

