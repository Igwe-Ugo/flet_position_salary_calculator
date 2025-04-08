# Salary Calculator App

A Flet-based web application that predicts salaries based on position levels using polynomial regression. The app provides a user-friendly interface for employees to estimate their prospective income.

## Features

- **Position Selection**: Dropdown with available positions from the dataset
- **Salary Prediction**: Uses machine learning (polynomial regression) to predict salaries
- **Responsive UI**: Clean, modern interface with proper form validation
- **Result Display**: Shows predicted salary in proper currency format

## Technologies Used

- **Frontend**: [Flet](https://flet.dev/) (Python framework for building web apps)
- **Backend**: Python
- **Machine Learning**: Scikit-learn (LinearRegression, PolynomialFeatures)
- **Data Handling**: Pandas

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Igwe-Ugo/flet_position_salary_calculator
   cd flet_position_salary_calculator

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3.  Run the application;
    ```bash
    python main.py

## File Structure
salary-calculator/
├── main.py                # Main application file
├── predictions.py         # Machine learning model and predictions
├── Position_Salaries.csv  # Dataset file
├── requirements.txt       # Dependencies file
├── README.md              # This file
└── screenshot.png         # Application screenshot

## Dataset
The application uses a CSV file (Position_Salaries.csv) with the following structure:
Position,Level,Salary
Business Analyst,1,45000
Junior Consultant,2,50000
...

## How it works
1.  The application loads position and salary data from the CSV file
2.  Trains a polynomial regression model (degree=5) on the data
3.  Provides a form for users to:
4.  Enter their name and email
4.  Select their position from a dropdown
5.  Predicts the salary when the form is submitted
6.  Displays the results in a clean card format

## Customization
1.  You can customize the application by:
2.  Modifying the styling constants in main.py
3.  Adding more positions to the dataset
4.  Changing the regression model parameters in predictions.py

## Future Improvements
1.  Add user authentication
2.  Implement salary comparison with industry averages
3.  Add visualization of salary progression
4.  Make the app responsive for mobile devices

## License
Distributed under the MIT License. See [LICENSE](https://opensource.org/license/mit) for more information.

## Contact
Your Name - Igwe Ugochukwu Edwin - [Email](ugo2000igwe12@gmail.com)
Project Link: https://github.com/Igwe-Ugo/flet_position_salary_calculator
