from flask import Flask  # import Flask
from flask import render_template
from flask import request

from calculate_api.UserProfile import UserProfile, Developer, Designer
from calculate_api.utilities import calculator

app = Flask(__name__)  # activate the Flask application/ instantiate the Flask object


@app.route('/hello_world')
def hello_world():
    return "Hello, Tribe!"


@app.route('/')
def candidate_form():
    """

    :return:
    """
    return render_template('index.html')


@app.route('/calculate_salary', methods=['POST'])
def calculate_salary():
    if request.method == "POST":
        candidate_type = request.form["profession"]

        number_of_exp_years = int(request.form["experience"])

        user_coding_languages = request.form['languages']
        user_trade_tools = user_coding_languages.split(",")

        user_design_tools = request.form['designTools']
        user_trade_tools = user_design_tools.split(",")

        dob = request.form['dob']

        full_name = request.form['fullName']

        age = int(request.form['age'])

        country = request.form['country']

        state = request.form['state']
        number_of_education_years = int(request.form['educationYears'])

        print(request.form)

    candidate_developer = False
    candidate_designer = False

    job_type = ''

    if int(candidate_type) == 1:
        candidate_developer = True
        candidate_designer = False
        user_profile = Developer(dob, age, full_name, country, state,
                                 number_of_education_years, user_trade_tools)
    elif int(candidate_type) == 2:
        candidate_developer = False
        candidate_designer = True
        user_profile = Designer(dob, age, full_name, country, state,
                                number_of_education_years, user_trade_tools)
    else:
         user_profile = UserProfile(dob, age, full_name, country, state,
                                number_of_education_years)

        # return "OK" - mhynson - Not needed for now





    calculator.expected_salary = calculator.calculate_expected_salary_from_user_experience(user_profile,
                                                                                           user_trade_tools,
                                                                                           number_of_exp_years,
                                                                                           number_of_education_years)

    calculator.expected_salary = calculator.calculate_expected_salary_from_coding_experience(calculator.expected_salary,
                                                                                             user_coding_languages, number_of_exp_years, user_trade_tools)

    # return calculator.expected_salary
    print(calculator.expected_salary)

    return render_template('calculate_salary.html', output=calculator.expected_salary)