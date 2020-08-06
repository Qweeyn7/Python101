expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}
expected_salary = 0
# new_expected_salary = 0

'''
    returns dict(
            calculated_salary = 90000
            reasons = list() 
            user = dict()  
        )
'''
def calculate_expected_salary_from_user_experience(user_information, user_trade_tools,
                                                   user_experience, number_of_education_years):
    """
      A function for calculating the expected salary based on the user's
      state, and their years of experience.
  """

    # Get the user's state from the incoming user_information object
    state = user_information.user_state

    # Set the base salary, based on the user's state
    base_salary = expected_salaries[state]

    # Initialize a new_expected_salary variable, which is set to the base_salary
    new_expected_salary = base_salary

    # Output message
    output = {
        "salary": base_salary,
        "reasons": list(),
        "message": "",
    }

    if isinstance(user_information, dict):
        # return "All Fields have been completed."
        # print()
        # output += "\nAll Fields have been completed."

        output["message"] = "\nAll Fields have been completed."
    else:
        # return "This is not a dictionary. It is {}".format(type(user_information))
        # output += "This is not a dictionary. It is {}".format(type(user_information))
        # print()
        output["message"] = "This is not a dictionary. It is {}".format(type(user_information))

    # Re-calculate the salary based on the user's experience.
    if int(user_experience) == 1:
        new_expected_salary = base_salary - 5000
        output["reasons"].append("Unfortunately with your limited experience we will have to deduct $5k from your base salary.")
        # return "Unfortunately with your limited experience we will have to deduct $5k from your base salary."
    elif int(user_experience) == 2:
        new_expected_salary = base_salary + 2000
        # return "With your level of experience, expect a $2k bump in your base salary."
        output["reasons"].append(
            "With your level of experience, expect a $2k bump in your base salary.")
    elif int(user_experience) == 3:
        new_expected_salary = base_salary + 5000
        # return "Exactly what we are looking for! Expect a $5K added to your base salary."
        output["reasons"].append(
            "Exactly what we are looking for! Expect a $5K added to your base salary.")
    elif int(user_experience) == 4:
        new_expected_salary = base_salary + 10000
        # return (
        #     "We're giving you an additional $10k increase to your base salary for the many years of experience you "
        #     "have "
        #     "in this field.")
        output["reasons"].append(
            "We're giving you an additional $10k increase to your base salary for the many years of experience you "
            "have "
            "in this field.")


    candidate_developer = False
    candidate_designer = False

    candidate_type_wording_map = {
        "developer": "coding languages",
        "designer": "design programs"
    }

    candidate_type_wording = candidate_type_wording_map[user_information.candidate_type]

    # Calculate salary based on professional knowledge
    if len(user_trade_tools) < 3:
        new_expected_salary = new_expected_salary - 7500
        # print("Learn more " + candidate_type_wording + ": $7.5K was deducted from the expected salary.")
        output["reasons"].append(
            "Learn more " + candidate_type_wording + ": $7.5K was deducted from the expected salary.")
    elif len(user_trade_tools) > 3:
        new_expected_salary = new_expected_salary + 10000
        # print("Learning more than 3 " + candidate_type_wording + " added $10K to expected salary.")
        output["reasons"].append(
            "Learning more than 3 " + candidate_type_wording + " added $10K to expected salary.")
    else:
        new_expected_salary = new_expected_salary + 5000
        # print("Knowing 3 " + candidate_type_wording + " or less only added $5K to expected salary.")
        output["reasons"].append(
            "Knowing 3 " + candidate_type_wording + " or less only added $5K to expected salary.")

    # Calculate salary based on education experience
    if int(number_of_education_years) > 3:
        new_expected_salary = new_expected_salary + 10000
        # return "Dedication to learning added $10K to base salary "
        output["reasons"].append("Dedication to learning added $10K to base salary ")

    elif int(number_of_education_years) < 3:
        new_expected_salary = new_expected_salary - 7500
        # return "Number for years of education needs improvement: Deduct $7.5K from base salary."
        output["reasons"].append("Number for years of education needs improvement: Deduct $7.5K from base salary.")
    else:
        new_expected_salary = new_expected_salary - 2000
        # return "Continue learning to increase salary: added $2K to expected salary."
        output["reasons"].append("Continue learning to increase salary: added $2K to expected salary.")


    # return "Expect around $" + str(new_expected_salary) + " annually for this position."
    # print()

    output["reasons"].append("Expect around $" + str(new_expected_salary) + " annually for this position.")
    output["salary"] = new_expected_salary
    output["user"] = user_information

    # return new_expected_salary
    return output


def calculate_expected_salary_from_coding_experience(current_expected_salary_info, user_languages, user_experience, user_trade_tools):
    # Re-calculate the salary, based off the user experience, and the number of languages they know.

    output = current_expected_salary_info
    new_expected_salary = output["salary"]

    # If user has 1 year of exp
    if int(user_experience) == 1:
        if len(user_languages) < 2:
            new_expected_salary = new_expected_salary - 10000
            output["reasons"].append("Learn more Coding Languages: Deduct $10k from expected salary.")
            # return "Learn more Coding Languages: Deduct $10k from expected salary."
        elif len(user_languages) == 2:
            new_expected_salary = new_expected_salary + 5000
        else:
            new_expected_salary = new_expected_salary + 2500

    # If user has 2 years of exp
    if int(user_experience) == 2:
        if len(user_languages) == 2:
            new_expected_salary = new_expected_salary - 5000
        elif len(user_languages) == 3:
            new_expected_salary = new_expected_salary + 7000
            output["reasons"].append(
                "Great! We can add a minimum of $7k to your annual salary for the amount of Coding Languages you know.")
        else:
            new_expected_salary = new_expected_salary + 4500

    # if len(user_languages) == 3:
    #     new_expected_salary = new_expected_salary + 7000
    #     return "Great! We can add a minimum of $7k to your annual salary for the amount of Coding Languages you know."

    # If user has 3 years of exp
    if int(user_experience) == 3:
        if len(user_languages) < 3:
            new_expected_salary = new_expected_salary - 5000
        elif len(user_languages) == 4:
            new_expected_salary = new_expected_salary + 9000
            output["reasons"].append(
                "Perfect! You are a model candidate for the position, we can negotiate a $9k bump in you annual salary "
                "after "
                "for the amount of Coding Languages you know.")
        else:
            new_expected_salary = new_expected_salary + 6500

    # If user knows 4 coding languages
    # if len(user_languages) == 4:
    #     new_expected_salary = new_expected_salary + 9000
        # return (
        #     "Perfect! You are a model candidate for the position, we can negotiate a $9k bump in you annual salary "
        #     "after "
        #     "for the amount of Coding Languages you know.")

    # If user has 4 years of exp
    if int(user_experience) == 4:
        if len(user_languages) == 4:
            new_expected_salary = new_expected_salary + 9000
        elif len(user_languages) == 5:
            new_expected_salary = new_expected_salary + 11000
            output["reasons"].append(
                "With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual salary."
            )
        else:
            new_expected_salary = new_expected_salary + 8500

    # if len(user_languages) == 5:
    #     new_expected_salary = new_expected_salary + 11000
    #     return (
    #         "With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual salary.")
    # else:
    #     candidate_designer = True

    if int(user_experience) == 1:
        if len(user_trade_tools) < 2:
            new_expected_salary = new_expected_salary - 10000
            # return "Learn more Coding Languages: Deduct $10k from expected salary."
            output["reasons"].append("Learn more Coding Languages: Deduct $10k from expected salary.")
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
            # return (
            #     "Great! We can add a minimum of $7k to your annual salary for the amount of Coding Languages you know.")
            output["reasons"].append("Great! We can add a minimum of $7k to your annual salary for the amount of Coding Languages you know.")

    if int(user_experience) == 3:
        if len(user_trade_tools) < 3:
            new_expected_salary = new_expected_salary - 5000
        elif len(user_trade_tools) == 4:
            new_expected_salary = new_expected_salary + 9000
        else:
            new_expected_salary = new_expected_salary + 6500

        if len(user_trade_tools) == 4:
            new_expected_salary = new_expected_salary + 9000
            # return (
            #     "Perfect! You are a model candidate for the position, we can negotiate a $9k bump in you annual "
            #     "salary after "
            #     "for the amount of Coding Languages you know. ")
            output["reasons"].append(
                "Perfect! You are a model candidate for the position, we can negotiate a $9k bump in you annual "
                "salary after "
                "for the amount of Coding Languages you know.")

    if int(user_experience) == 4:
        if len(user_trade_tools) == 4:
            new_expected_salary = new_expected_salary + 9000
        elif len(user_trade_tools) == 5:
            new_expected_salary = new_expected_salary + 11000
        else:
            new_expected_salary = new_expected_salary + 8500
        if len(user_trade_tools) == 5:
            new_expected_salary = new_expected_salary + 11000
            # return (
            #     "With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual "
            #     "salary.")
            output["reasons"].append(
                "With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual "
                "salary.")

    output["salary"] = new_expected_salary

    return output
