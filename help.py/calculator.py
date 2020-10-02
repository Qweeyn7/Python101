

expected_salary = 0

# Initialize a dictionary with a base salary value.
expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}

# Initialize the user's info as an empty dictionary.
user_profile = True


def calculate_expected_salary_from_user_experience(user_information, user_trade_tools,
                                                   user_experience, number_of_education_years, candidate_type_str):
    """
      A function for calculating the expected salary based on the user's
      state, and their years of experience.
  """

    # Get the user's state from the incoming user_information object
    state = user_information["State"]

    # Set the base salary, based on the user's state
    base_salary = expected_salaries[state]

    # Initialize a new_expected_salary variable, which is set to the base_salary
    new_expected_salary = base_salary

    if isinstance(user_information, dict):
        print("All Fields have been completed.")
        print()
    else:
        print("This is not a dictionary. It is {}".format(type(user_information)))
        print()

    # Re-calculate the salary based on the user's experience.
    if int(user_experience) == 1:
        new_expected_salary = base_salary - 5000
        print("Unfortunately with your limited experience we will have to deduct $5k from your base salary.")
    elif int(user_experience) == 2:
        new_expected_salary = base_salary + 2000
        print("With your level of experience, expect a $2k bump in your base salary.")
    elif int(user_experience) == 3:
        new_expected_salary = base_salary + 5000
        print("Exactly what we are looking for! Expect a $5K added to your base salary.")
    elif int(user_experience) == 4:
        new_expected_salary = base_salary + 10000
        print(
            "We're giving you an additional $10k increase to your base salary for the many years of experience you "
            "have "
            "in this field.")

    candidate_developer = False
    candidate_designer = False

    candidate_type_wording_map = {
        "developer": "coding languages",
        "designer": "design programs"
    }

    candidate_type_wording = candidate_type_wording_map[candidate_type_str]

    if len(user_trade_tools) < 3:
        new_expected_salary = new_expected_salary - 7500
        print("Learn more " + candidate_type_wording + ": $7.5K was deducted from the expected salary.")
    elif len(user_coding_languages) > 3:
        new_expected_salary = new_expected_salary + 10000
        print("Learning more than 3 " + candidate_type_wording + " added $10K to expected salary.")
    else:
        new_expected_salary = new_expected_salary + 5000
        print("Knowing 3 " + candidate_type_wording + " or less only added $5K to expected salary.")
    if int(number_of_education_years) > 3:
        new_expected_salary = new_expected_salary + 10000
        print("Dedication to learning added $10K to base salary ")
    elif int(number_of_education_years) < 3:
        new_expected_salary = new_expected_salary - 7500
        print("Number for years of education needs improvement: Deduct $7.5K from base salary.")
    else:
        new_expected_salary = new_expected_salary - 2000
        print("Continue learning to increase salary: added $2K to expected salary.")
    print("Expect around $" + str(new_expected_salary) + " annually for this position.")
    print()
    return new_expected_salary


current_salary = 0


def calculate_expected_salary_from_coding_experience(current_salary, user_languages, user_experience, user_trade_tools):
    # Re-calculate the salary, based off the user experience, and the number of languages they know.
    new_expected_salary = current_salary
    if int(user_experience) == 1:
        if len(user_languages) < 2:
            new_expected_salary = new_expected_salary - 10000
            print("Learn more Coding Languages: Deduct $10k from expected salary.")
        elif len(user_languages) == 2:
            new_expected_salary = new_expected_salary + 5000
        else:
            new_expected_salary = new_expected_salary + 2500
    if int(user_experience) == 2:
        if len(user_languages) == 2:
            new_expected_salary = new_expected_salary - 5000
        elif len(user_languages) == 3:
            new_expected_salary = new_expected_salary + 7000
        else:
            new_expected_salary = new_expected_salary + 4500
    if len(user_languages) == 3:
        new_expected_salary = new_expected_salary + 7000
        print("Great! We can add a minimum of $7k to your annual salary for the amount of Coding Languages you know.")
    if int(user_experience) == 3:
        if len(user_languages) < 3:
            new_expected_salary = new_expected_salary - 5000
        elif len(user_coding_languages) == 4:
            new_expected_salary = new_expected_salary + 9000
        else:
            new_expected_salary = new_expected_salary + 6500
    if len(user_languages) == 4:
        new_expected_salary = new_expected_salary + 9000
        print(
            "Perfect! You are a model candidate for the position, we can negotiate a $9k bump in you annual salary "
            "after "
            "for the amount of Coding Languages you know.")
    if int(user_experience) == 4:
        if len(user_languages) == 4:
            new_expected_salary = new_expected_salary + 9000
        elif len(user_languages) == 5:
            new_expected_salary = new_expected_salary + 11000
        else:
            new_expected_salary = new_expected_salary + 8500
    if len(user_languages) == 5:
        new_expected_salary = new_expected_salary + 11000
        print(
            "With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual salary.")
    else:
        candidate_designer = True
        new_expected_salary = current_salary

    if int(user_experience) == 1:
        if len(user_trade_tools) < 2:
            new_expected_salary = new_expected_salary - 10000
            print("Learn more Coding Languages: Deduct $10k from expected salary.")
        elif len(user_trade_tools) == 2:
            new_expected_salary = new_expected_salary + 5000
        else:
            new_expected_salary = new_expected_salary + 2500
        if int(user_experience) == 2:
            if len(user_trade_tools) == 2:
                new_expected_salary = new_expected_salary - 5000
            elif len(user_trade_tools) == 3:
                new_expected_salary = new_expected_salary + 7000
            else:
                new_expected_salary = new_expected_salary + 4500
        if len(user_trade_tools) == 3:
            new_expected_salary = new_expected_salary + 7000
            print(
                "Great! We can add a minimum of $7k to your annual salary for the amount of Coding Languages you know.")
        if int(user_experience) == 3:
            if len(user_trade_tools) < 3:
                new_expected_salary = new_expected_salary - 5000
            elif len(user_coding_languages) == 4:
                new_expected_salary = new_expected_salary + 9000
            else:
                new_expected_salary = new_expected_salary + 6500
        if len(user_trade_tools) == 4:
            new_expected_salary = new_expected_salary + 9000
            print(
                "Perfect! You are a model candidate for the position, we can negotiate a $9k bump in you annual "
                "salary after "
                "for the amount of Coding Languages you know. ")
        if int(user_experience) == 4:
            if len(user_trade_tools) == 4:
                new_expected_salary = new_expected_salary + 9000
            elif len(user_trade_tools) == 5:
                new_expected_salary = new_expected_salary + 11000
            else:
                new_expected_salary = new_expected_salary + 8500
        if len(user_trade_tools) == 5:
            new_expected_salary = new_expected_salary + 11000
            print(
                "With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual "
                "salary.")

    return new_expected_salary

