### Student Marks Predictor

## Overview

The Student Marks Predictor is a simple web application designed to predict student maths marks based on various input features. The application leverages machine learning techniques to provide accurate predictions and is built using Python with Flask as the web framework.

## Features

- **User Input:** Users can input various features related to students.
- **Prediction:** The application predicts student marks based on the input features.
- **Visualization:** Data visualizations using libraries like Seaborn and Matplotlib.

## Dataset
Features in data.csv:
1. **gender**: The gender of the student (e.g., female, male).
2. **race_ethnicity**: The race/ethnicity group to which the student belongs (e.g., group A, group B, group C).
3. **parental_level_of_education**: The highest level of education attained by the student's parents (e.g., bachelor's degree, master's degree, some college, associate's degree).
4. **lunch**: The type of lunch the student receives (e.g., standard, free/reduced).
5. **test_preparation_course**: Whether the student completed a test preparation course (e.g., none, completed).
6. **math_score**: The student's score in math.
7. **reading_score**: The student's score in reading.
8. **writing_score**: The student's score in writing.

## Project Structure

- `artifacts`: Contains pickle files of model and preprocessor. Also contains csv files of dataset.
- `notebooks(Optional)`: Contains jupyter notebook of the following modular programming.
- `src`: Folder contains files related to data injestion, data transformation, model trainer with training and prediction pipeline files. It also contains utils file which consist of helper functions. A logger file for logs nad exception file for exception handling.
- `templates`: HTML files for frontend. 
- `app.py`: Main application file containing the Flask web server and routes.
- `Dockerfile`: Docker configuration file for containerizing the application.
- `requirements.txt`: File containing all the dependencies required to run the application.

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Docker (optional, for containerization)

### Local Setup

1. **Clone the repository:**

   ```bash
   git clone git@github.com:ksak100/Student_marks_prediction_End_to_End.git
   cd Student_marks_prediction_End_to_End
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/predictdata`.

### Docker Setup

1. **Build the Docker image:**

   ```bash
   docker build -t student-marks-predictor .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 student-marks-predictor
   ```

   The application will be accessible at `http://127.0.0.1:5000/predictdata`.

## Dependencies

The application requires the following Python packages:

- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn
- dill
- flask

All dependencies are listed in the `requirements.txt` file and can be installed using `pip`.

## Usage

1. Open the application in your web browser.
2. Input the required features for the student.
3. Submit the form to get the predicted marks.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries, please contact [kunalsingh974@gmail.com].

## Flask app on local host
<img width="808" alt="image" src="https://github.com/user-attachments/assets/21809b1e-67d9-4a07-a9c5-cd2d5da965bc">

