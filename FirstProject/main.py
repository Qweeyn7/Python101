from datetime import datetime

from UserProfile import UserProfile

print("Welcome candidate! Please enter in your information.")
print()

# Initialize the variables for the items that we will ask for the user to input.
#   They will default to False (or it could be None).
#   If the variable is not set, then we'll ask them to enter in that information.
user_dob_old = False
user_age = False
user_full_name = False
user_state = False
user_country = False
user_number_of_education_years = False

# Initialize expected salary to 0. We'll update this later, based on the user's information.
expected_salary = 0

# Initialize a dictionary with a base salary value.
expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}

# Initialize the user's info as an empty dictionary.
user_profile = True

# Initialize a flag that will determine whether or not ask for candidate information.
should_ask_for_info = True


def calculate_expected_salary_from_user_experience(user_information, user_exp):
    """
        A function for calculating the expected salary based on the user's
      state, and   their years of experience.
    """

    # Get the user's state from the incoming user_information object
    state = user_information.user_state

    # Set the base salary, based on the user's state
    base_salary = expected_salaries[state]

    # Initialize a new_expected_salary variable, which is set to the base_salary
    new_expected_salary = base_salary

    if isinstance(user_information, dict):
        print("This is valid.")
    else:
        print("This is not a dictionary. It is {}".format(type(user_information)))
        print()

    # Re-calculate the salary based on the user's experience.
    if int(user_exp) == 1:
        new_expected_salary = base_salary - 5000
        print("Unfortunately with your limited experience we will have to deduct $5k from your base salary.")
        print()
    elif int(user_exp) == 2:
        new_expected_salary = base_salary + 2000
        print("With your level of experience expect a $2k bump in your base salary.")
        print()
    elif int(user_exp) == 3:
        new_expected_salary = base_salary + 5000
        print("Exactly what we are looking for! Expect a $5K added to your base salary.")
        print()
    elif int(user_exp) == 4:
        new_expected_salary = base_salary + 10000
        print(
            "We're giving you an additional $10k increase to your base salary for the many years of experience you "
            "have "
            "in this field.")
        print()

    return new_expected_salary


def calculate_expected_salary_from_coding_experience(current_salary, user_languages, user_experience):
    """
        Re-calculate the salary, based off the user experience, and the number of languages they know.
    """
    new_expected_salary = current_salary
    if int(user_experience) == 1:
        if len(user_languages) < 2:
            new_expected_salary = new_expected_salary - 10000
            print("Learn more Coding Languages: Deduct $10k from expected salary.")
            print()
        elif len(user_languages) == 2:
            new_expected_salary = new_expected_salary + 5000
        else:
            new_expected_salary = new_expected_salary + 2500
            print()
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
        print()
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
            "for the amount of Coding Languages you know. ")
        print()
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
        print()

    return new_expected_salary


# Now, ask for a user's information as long as should_ask_for_info is True.
while should_ask_for_info:
    try:
        # Ask the user for various forms for information.
        if not user_dob_old:
            user_dob_old = input("Enter Date of Birth (MM/DD/YYYY):")

            # Convert the date of birth into a different format.
            dob_timestamp = datetime.strptime(user_dob_old, '%m/%d/%Y')
            user_dob = dob_timestamp.strftime('%B %d, %Y')

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

        is_active = True

        # Create a user profile from the info provided, using the UserProfile class.
        user_profile = UserProfile(user_dob, user_age, user_full_name, user_country, user_state,
                                   user_number_of_education_years)

        user_password = user_profile.get_password()
        print(user_password)
        print()
        new_password = input("Please enter a new password.")
        user_profile.set_password(new_password)
        print("Your new password is", new_password)
        user_password = user_profile.get_password()
        user_Id = user_profile.create_user_Id()
        print("Your unique Account Id is", user_Id)
        print()

        user_info = {
            "Date of Birth": user_profile.user_dob,
            "Current Age": user_profile.user_age,
            "Full Name": user_profile.user_full_name,
            "Country of Residence": user_profile.user_country,
            "state": user_profile.user_state,
            "Educational Years": user_profile.user_number_of_education_years
        }

        # Ask the user for the number of years of experience they have.
        users_experience = input(
            "How many years of experience do you have developing software?\n[1] Less than 1 year experience.\n"
            "[2] 1-3 years of experience.\n[3] 3-8 years of experience.\n[4]"
            "8+ years of experience.\n")
        users_experience = int(users_experience)
        print()

        # Ask the user about the coding languages they know.
        user_coding_languages = str(input("Which Coding Languages do you know? (Separate each language by commas)\n"))
        print()
        print("Before split():" + user_coding_languages)
        user_coding_languages = user_coding_languages.split(",")
        print("After split():" + str(user_coding_languages))
        print()

        # Calculate the expected salary based on the user's state and their experience.
        expected_salary = calculate_expected_salary_from_user_experience(user_profile, users_experience)

        # Re-calculate the expected salary based on the user's coding experience and languages.
        expected_salary = calculate_expected_salary_from_coding_experience(expected_salary, user_coding_languages,
                                                                           users_experience)

        # Re-calculate the expected salary based on

        # Ask the user if they would like to add another candidate.
        another_candidate = input("Would you like to enter another another candidate? (Y/N) \n")
        should_ask_for_info = another_candidate.upper() == "Y"

        # Reset the variables so that we can ask questions again.
        if should_ask_for_info:
            user_dob_old = False
            user_age = False
            user_full_name = False
            user_state = False
            user_country = False
            user_number_of_education_years = False
        else:
            # Display the user's info and expected salary, if we are not going to ask for another candidate.
            print("Expect $" + str(expected_salary) + " for your level of experience.")
            print()

            print(user_profile)
            print()

            for item in expected_salaries:
                if user_state == item in expected_salaries:
                    print("You're base expected salary for just living in " + str(
                        user_state) + " could have been $" + str(
                        expected_salaries[item]) + ".")
                    print()
                    print("Thank you for your input, we will contact you soon.")

    except ValueError:
        print("Please answer all questions.")

    except KeyError:
        user_state = False
        print("Please enter valid State.")

    # except TypeError:
    # user_profile = False
