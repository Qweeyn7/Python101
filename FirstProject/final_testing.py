#  ask the user to input their experiance by asking them a question using the input() function
"""http://www.w3schools.com/python/ref_func_input.asp"""

#  use an if/elif/else statement to check to see if the user chose option 1,2,3, or 4
"""http://www.w3schools.com/python/python_conditions.asp"""

# TODO - create a fjunction to calc salary based state

# homework - else enter a default message if the user does not choose a valid option
from datetime import datetime

from Lesson6 import Lesson6

print( "Welcome candidate! Please enter in your information." )
user_dob_old = False
user_age = False
user_full_name = False
user_state = False
user_country = False
user_number_of_education_years = False
expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}
user_info = True
loop_val = True
is_active = True

while loop_val:
    try:
        if not user_dob_old:
            user_dob_old = input("Enter Date of Birth (MM/DD/YYYY):")
        if not user_age:
            user_age = int(input("Enter Current Age:"))
        if not user_full_name:
            user_full_name = input("Enter Full Name:")
        valid_state = list(expected_salaries.keys())
        for state in valid_state:
            print(state)
        if not user_state:
            user_state = input('Enter State (Please enter the 2 letter abbreviation:)')
        if user_state not in valid_state:
            raise KeyError()
        if not user_country:
            user_country = input("Enter Country:")
        if not user_number_of_education_years:
            user_number_of_education_years = int(input("Enter the number of years you've been learning code."))
            print()
        datetimeobject = datetime.strptime( user_dob_old, '%m/%d/%Y' )
        user_dob = datetimeobject.strftime( '%B %d, %Y' )
        user_profile = Lesson6( user_dob, user_age, user_full_name, user_country, user_state,
                                user_number_of_education_years )

        user_info = {'DOB': user_profile.user_dob, "Age": user_profile.user_age,
                     "Full Name": user_profile.user_full_name,
                     "Country": user_profile.user_country, "State": user_profile.user_state,
                     "is_active": id( is_active ),
                     "Years of Education": user_profile.user_number_of_education_years}

        users_experience = input(
            "How many years of experience do you have developing software?\n[1] Less than 1 year experience.\n"
            "[2] 1-3 years of experience.\n[3] 3-8 years of experience.\n[4]"
            "8+ years of experience.\n" )

        users_experience = int( users_experience )
        print()

        user_coding_languages: str = input( "Which Coding Languages do you know? (Separate each language by commas)\n" )
        print()
        print( "Before split():" + user_coding_languages )
        user_coding_languages = user_coding_languages.split( "," )
        print( "After split():" + str( user_coding_languages ) )
        print()

        #calculate_expected_salary()

        another_candidate = input( "Would you like to enter another candidate? Y/N \n" )
        print()
        if another_candidate == "Y":
            loop_val = True
        else:
            loop_val = False
            print( user_info )
            print()
        break

    except ValueError:
        print("Please answer all questions.")
    except KeyError:
        user_state = False
        print("Please enter valid State.")



# TODO: move these into calculate_expected_salaary
#expected_salary = 0
#new_expected_salary = 0


def calculate_expected_salary(number_of_edu_years, user_information, years_of_experience):
    if isinstance(user_information, dict):
        print("This is valid.")
    else:
        print("This is not a dictionary. It is {}".format(type(user_information)))
        print()

    if int(users_experience) == 1:
        expected_salary = expected_salaries[user_state]
        new_expected_salary = expected_salary - 5000
        print("Unfortunately with your limited experience we will have to deduct $5k from your base salary.")
        print()
    elif int(users_experience) == 2:
        expected_salary = expected_salaries[user_state]
        new_expected_salary = expected_salary + 2000
        print("With your level of experience expect a $2k bump in your base salary.")
        print()
    elif int(users_experience) == 3:
        expected_salary = expected_salaries[user_state]
        new_expected_salary = expected_salary + 5000
        print("Exactly what we are looking for! Expect a $5K added to your base salary.")
        print()
    elif int(users_experience) == 4:
        expected_salary = expected_salaries[user_state]
        new_expected_salary = expected_salary + 10000
        print(
            "We're giving you an additional $10k increase to your base salary for the many years of experience you "
            "have "
            "in this field.")
        print()
    expected_salary = 0
    new_expected_salary = 0

    return new_expected_salary


new_expected_salary = calculate_expected_salary(user_number_of_education_years, user_age, users_experience)

if int(users_experience) == 1:
    if len(user_coding_languages) < 2:
        new_expected_salary = new_expected_salary - 10000
        print("Learn more Coding Languages: Deduct $10k from expected salary.")
        print()
    elif len(user_coding_languages) == 2:
        new_expected_salary = new_expected_salary + 5000
    else:
        new_expected_salary = new_expected_salary + 2500
        print()
if int(users_experience) == 2:
    if len(user_coding_languages) == 2:
        new_expected_salary = new_expected_salary - 5000
    elif len(user_coding_languages) == 3:
        new_expected_salary = new_expected_salary + 7000
    else:
        new_expected_salary = new_expected_salary + 4500
if len(user_coding_languages) == 3:
    new_expected_salary = new_expected_salary + 7000
    print("Great! We can add a minimum of $7k to your annual salary for the amount of Coding Languages you know.")
    print()
if int(users_experience) == 3:
    if len(user_coding_languages) < 3:
        new_expected_salary = new_expected_salary - 5000
    elif len(user_coding_languages) == 4:
        new_expected_salary = new_expected_salary + 9000
    else:
        new_expected_salary = new_expected_salary + 6500
if len(user_coding_languages) == 4:
    new_expected_salary = new_expected_salary + 9000
    print(
        "Perfect! You are a model candidate for the position, we can negotiate a $9k bump in you annual salary after "
        "for the amount of Coding Languages you know. ")
    print()
if int(users_experience) == 4:
    if len(user_coding_languages) == 4:
        new_expected_salary = new_expected_salary + 9000
    elif len(user_coding_languages) == 5:
        new_expected_salary = new_expected_salary + 11000
    else:
        new_expected_salary = new_expected_salary + 8500
if len(user_coding_languages) == 5:
    new_expected_salary = new_expected_salary + 11000
    print(
        "With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual salary.")
    print()

print("Expect $" + str(new_expected_salary) + " for your level of experience.")
print()

for item in expected_salaries:
    if user_state == item:
        print("You’re base expected salary for just living in " + str(user_state) + " could have been $" + str(
            expected_salaries[item]) + ".")
        print()
        break
