from datetime import datetime

expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}


def capture_user_info():
    user_dob_old = False
    user_age = False
    user_full_name = False
    user_state = False
    user_country = False
    user_number_of_education_years = False

    # Hynson: added a new variable to determine if we've captured all the info.
    info_captured = False
    user_info = None
    print("Welcome candidate! Please enter in your information.")

    # Hynson: now adding a while loop that continues until info_captured is True

    while not (info_captured):
        try:
            if not user_dob_old:
                user_dob_old = input("Enter Date of Birth (MM/DD/YYYY):")
            if not user_age:
                user_age = int(input("Enter Current Age:"))
            if not user_full_name:
                user_full_name = input("Enter Full Name:")

            # TODO: Here's a challenge. Build this list valid states from the expected_salaries dictionary.
            #   Remember, dictionaries are made up of “keys” and “values”.
            valid_state = ("CA", "NY", "FL", "NC", "TX")

            for state in valid_state:
                print(state)
            if not user_state:
                user_state = input('Enter State (Please enter the 2 letter abbreviation:)')
            if user_state not in valid_state:
                raise KeyError()
            if not user_country:
                user_country = input("Enter Country:")

            is_active = True
            if not user_number_of_education_years:
                user_number_of_education_years = int(input("Enter the number of years you've been learning code."))
                print()

            datetimeobject = datetime.strptime(user_dob_old, '%m/%d/%Y')
            user_dob = datetimeobject.strftime('%B %d, %Y')
            user_info = {"DOB": user_dob, "Age": user_age, "Full Name": user_full_name, "Country": user_country,
                         "State": user_state, "is_active": id(is_active),
                         "Years of Education": user_number_of_education_years}

            # Hynson: now that we've got the data, set the info_captured flag to True
            info_captured = True

            # Hynson: added a return statement here
            return user_info

        except ValueError:
            print("Please answer all questions.")
            # Hynson: be sure to set this to False so we can continue to stay in the loop and pull data
            info_captured = False

        except KeyError:
            user_state = False
            # Hynson: be sure to set this to False so we can continue to stay in the loop and pull data
            info_captured = False
            print("Please enter valid State.")

    return None


def capture_user_experience():
    candidate_exp = input(
        "How many years of experience do you have developing software?\n[1] Less than 1 year experience.\n"
        "[2] 1-3 years of experience.\n[3] 3-8 years of experience.\n[4]"
        "8+ years of experience.\n")

    candidate_exp = int(candidate_exp)
    print()

    # Hynson: added a return statement here
    return candidate_exp


def capture_user_coding_languages():
    user_coding_languages: str = input("Which Coding Languages do you know? (Separate each language by commas)\n")
    print()
    print("Before split():" + user_coding_languages)
    user_coding_languages = user_coding_languages.split(",")
    print("After split():" + str(user_coding_languages))
    print()

    # Hynson: added a return statement here
    return user_coding_languages


def calculate_expected_salary(user_coding_languages, user_information, candidate_exp):
    # Hynson: added expected_salaries as a global
    global new_expected_salary, expected_salaries

    # Hynson: we didn't get around to discussing this more but I'm changing this up to give it more of a purpose.
    # if isinstance(user_information, dict):
    #     print("This is valid.")
    # else:
    #     print("This is not a dictionary. It is {}".format(type(user_information)))
    #     print()
    if not (isinstance(user_information, dict)):
        print("This is valid.")
        raise Exception('user_information must be a dictionary')

    expected_salary = 0
    new_expected_salary = 0

    # Hynson: the line below isn't needed. i commented it out
    # new_expected_salary = calculate_expected_salary(user_coding_languages, user_information, candidate_exp)

    if candidate_exp == 1:
        expected_salary = expected_salaries[user_information["State"]]
        new_expected_salary = expected_salary - 5000
        print("Unfortunately with your limited experience we will have to deduct $5k from your base salary.")
        print()
    elif candidate_exp == 2:
        expected_salary = expected_salaries[user_information["State"]]
        new_expected_salary = expected_salary + 2000
        print("With your level of experience expect a $2k bump in your base salary.")
        print()
    elif candidate_exp == 3:
        expected_salary = expected_salaries[user_information["State"]]
        new_expected_salary = expected_salary + 5000
        print("Exactly what we are looking for! Expect a $5K added to your base salary.")
        print()
    elif candidate_exp == 4:
        expected_salary = expected_salaries[user_information["State"]]
        new_expected_salary = expected_salary + 10000
        print(
            "We're giving you an additional $10k increase to your base salary for the many years of experience you "
            "have "
            "in this field.")
        print()
    return new_expected_salary


# Determine whether or not to prompt for the questionnaire
should_ask_questions = True

while should_ask_questions:
    # 1. capture user inform through questionnaire, create a new function, call fn and assign to a variable
    candidate_info = capture_user_info()

    # 1b. get user experience
    candidate_exp = capture_user_experience()

    # 1c. get number of coding languages
    user_coding_languages = capture_user_coding_languages()

    # 2. process information to calculate salary
    print(user_coding_languages)
    print(candidate_info)
    print(candidate_exp)

    expected_salary = calculate_expected_salary(user_coding_languages, candidate_info, candidate_exp)

    # 3. display salary
    # print("Hey your expected salary is XYZ")

    # 4. if add another user, then rerun questionnaire
    print("Would you like to add another candidate?")
    add_another = input("Add another?")

    if add_another.upper() == "Y":
        should_ask_questions = True

    # else : print all fo user info
    else:
        should_ask_questions = False
        # print(candidate_info)

if candidate_exp == 1:
    if len(user_coding_languages) < 2:
        new_expected_salary = new_expected_salary - 10000
        print("Learn more Coding Languages: Deduct $10k from expected salary.")
        print()
    elif len(user_coding_languages) == 2:
        new_expected_salary = new_expected_salary + 5000
    else:
        new_expected_salary = new_expected_salary + 2500
        print()
if candidate_exp == 2:
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
if candidate_exp == 3:
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
if candidate_exp == 4:
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
    if capture_user_info()["State"] == item in expected_salaries:
        print("You’re base expected salary for just living in " + str(user_state) + " could have been $" + str(
            expected_salaries[item]) + ".")
        break

    # Hynson: everything below this can be deleted.
    # user_wants_to_add_another = input("Do you want to enter another another candidate? ").upper
    # if user_wants_to_add_another == "Y":
    #     should_ask_questions = True
    # else:
    #     print(capture_user_info())
    #     print()
    #     should_ask_questions = False