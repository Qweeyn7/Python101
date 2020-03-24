import datetime
# from User_Profile import UserProfile

valid_state = ("NY", "WA", "TX", "IL", "NC", "CA")
expected_salaries = {"NY": 60000, "CA": 70000,
                     "TX": 50000, "NC": 50000,
                     "IL": 60000, "WA": 70000}


# noinspection PyUnboundLocalVariable
def projected_expected_salary(user_experience_years_coding, user_STATE, number_of_education_years):
    expected_salary = expected_salaries[user_STATE]

    if user_experience_years_coding == 1:
        new_expected_salary = expected_salary - 6000
    elif user_experience_years_coding == 2:
        new_expected_salary = expected_salary - 4000
    elif user_experience_years_coding == 3:
        new_expected_salary = expected_salary + 10000
    elif user_experience_years_coding == 4:
        new_expected_salary = expected_salary + 30000
    else:
        # Print Info
        print('Invalid input')

    if len(coding_lang) < 3:
        new_expected_salary = new_expected_salary + (len(coding_lang) * 500)
    elif len(coding_lang) > 3:
        new_expected_salary = expected_salary + (len(coding_lang) * 500)
    else:
        new_expected_salary = expected_salary - 4500
    if number_of_education_years > 3:
        new_expected_salary = new_expected_salary + (user_exp * 200)
    else:
        new_expected_salary = new_expected_salary - 5000
    print('\033[0;36m With your level of experience, you can expect around $' + str(new_expected_salary) + '.')

while True:
    try:
        user_name = input("Enter full name: ")
        if user_name == '':
            raise ValueError()
        d_o_b = input("Enter date of birth: ")
        if d_o_b == '':
            raise ValueError()
        age = input("How old art thou: ")
        age = int(age)
        user_state = input("Please enter your state"
                           "\nNY, WA, TX, IL, NC, CA"
                           "\nState: ")
        user_state = user_state.upper()
        if user_state not in valid_state:
            raise KeyError()
        user_country = input("Country: ")
        user_country = user_country.upper()
        is_active = True
        break
    except ValueError:
        print('\033[0;31m * OH NO! missing/invalid input. Please enter a valid input * \033[0m')
    except KeyError:
        print('\033[0;31m * OH NO! missing/invalid input. Please enter a valid state * \033[0m')
    except TypeError:
        print(
            '\033[0;31m * OH NO! The entry that you input is invalid for this section. Please enter a valid input * '
            '\033[0m')

while True:
    try:
        # Ask user experience
        num_of_years_learning = input("Please enter how many years have you been learning to coding: ")
        num_of_years_learning = int(num_of_years_learning)
        break
    except ValueError:
        print(
            '\033[0;31m * OH NO! Missing input. Please enter number of years you have been learning to code * \033[0m')

while True:
    try:
        user_exp = input("How many years of experience do you have developing software?"
                         "\n [1] - Less than 1 year(s) of experience"
                         "\n [2] - 1-3 year(s) of experience"
                         "\n [3] - 4-8 year(s) of experience"
                         "\n [4] - 9+ year(s) of experience"
                         "\n Specify year(s) of experience: ")
        user_exp = int(user_exp)
        if user_exp > 4:
            raise ValueError()
        break
    except ValueError:
        print('\033[0;31m * OH NO! Missing or invalid input. Please enter how many years of experience you have * '
              '\033[0m')

# Ask user to list known languages
coding_lang = input("How many languages do you know? (List and seperate them with commas)"
                    "\n For language"
                    "\n List Language(s): ")
coding_lang = coding_lang.split(",")

# Convert date of birth to Name of month date, year
dateformat = datetime.datetime.strptime(d_o_b, '%m/%d/%Y')
dob = dateformat.strftime('%B %d, %Y')

# Set set all objects from input values
user_profile = UserProfile(age)
user_profile.set_name(user_name)
Name = user_profile.get_name()
user_profile.set_dob(d_o_b)
DOB = user_profile.get_dob()
user_profile.set_state(user_state)
State = user_profile.get_state()
user_profile.set_country(user_country)
Country = user_profile.get_country()

# Create unique ID/Password
user_id = user_profile.create_unique_id()
print("A default password has been generated for account. Your current password is: ",
      user_profile.get_password())
try:
    if input("Would you like to change your password?: ") == "y":
        pw = input("Enter new password: ")
        if pw == '':
            raise ValueError()
        user_profile.set_password(pw)
    else:
        pw = user_profile.get_password()
except ValueError:
    print('\033[0;31m * OH NO! Missing or invalid input. Please enter how many years of experience you have * '
          '\033[0m')

# Make for loop for what user salary could have been
for item in expected_salaries:
    if user_profile.state == item in expected_salaries:
        print('\033[0;35m Hello ' + user_profile.name + '! Thank you for inputting your information. Your account '
                                                        'number is #' + str(
            user_id) + '.\n Base on the information you '
                       'provided; In the city of ' + str(
            user_profile.state) + ', the projected salary for programmers hovers around $'
              + str(expected_salaries[user_profile.state]) + '.')
        break
else:
    print('\033[0;31m * OH NO! State you have entered is not in database!! *')

projected_expected_salary(user_exp, user_profile.state, num_of_years_learning)

print("Your account information is as follows: "
      "\n Username: ", Name,
      "\n Age: ", age,
      "\n City: ", State,
      "\n Country: ", Country,
      "\n ID: ", user_id,
      "\n Password: ", pw)

