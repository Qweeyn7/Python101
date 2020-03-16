from datetime import datetime

loop_val = True  # you should have a field for the loop
user_list = []  # make a list of dictionaries, otherwise each time through your loop, your values will be overwritten

while loop_val:
    user_info = {}  # create an empty dictionary here - it will continue to accumulate each time through your loop.
    user_dob_old = False
    user_age = False
    user_full_name = False
    user_state = False
    user_country = False
    user_number_of_education_years = False
    try:
        if not user_dob_old:
            user_dob_old = input("Enter Date of Birth (MM/DD/YYYY):")
        if not user_age:
            user_age = int(input("Enter Current Age:"))
        if not user_full_name:
            user_full_name = input("Enter Full Name:")
        valid_state = ("CA", "NY", "FL", "NC", "TX")
        for state in valid_state:
            print(state)
        if not user_state:
            user_state = input("Enter State (Please enter the 2 letter abbreviation:)")
        if user_state not in valid_state:
            raise KeyError()
        if not user_country:
            user_country = input("Enter Country:")
        if not user_number_of_education_years:
            user_number_of_education_years = int(input("Enter the number of years you've been learning code."))
            is_active = True

        datetimeobject = datetime.strptime(user_dob_old, "%m/%d/%Y")
        user_dob = datetimeobject.strftime("%B %d, %Y")

##you can add the information to your dictionary this way
        user_info["DOB"] = user_dob
        user_info["Age"] = user_age
        user_info["Full Name"] = user_full_name
        user_info["Country"] = user_country
        user_info["State"] = user_state
        user_info["is_active"] = is_active
        user_info["Years of Education"] = user_number_of_education_years

        user_list.append(user_info)  ##Append your dictionary into your list of dictionaries

    except ValueError:
        print("Please answer all questions.")
    except KeyError:
        user_state = False
        print("Please enter valid State.")

        expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}

        users_experience = input(
            "How many years of experience do you have developing software?\n[1] Less than 1 year experience.\n"
            "[2] 1-3 years of experience.\n[3] 3-8 years of experience.\n[4]"
            "8+ years of experience.\n")
        users_experience = int(users_experience)
        print()

        user_coding_languages: str = input("Which Coding Languages do you know? (Separate each language by commas)\n")
        print("Before split():" + user_coding_languages)
        user_coding_languages = user_coding_languages.split(",")
        print("After split():" + str(user_coding_languages))
        print()

expected_salary = 0
new_expected_salary = 0

if int(users_experience) == 1:
    expected_salary = expected_salaries[user_info["State"]]
    new_expected_salary = expected_salary - 5000
    print("Unfortunately with your limited experience we will have to deduct $5k from your base salary.")
    print()
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
    expected_salary = expected_salaries[user_info["State"]]
    new_expected_salary = expected_salary + 2000
    print("With your level of experience expect a $2k bump in your base salary.")
    print()
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
    expected_salary = expected_salaries[user_info["State"]]
    new_expected_salary = expected_salary + 5000
    print("Exactly what we are looking for! Expect a $5K added to your base salary.")
    print()
    if len(user_coding_languages) < 3:
        new_expected_salary = new_expected_salary - 5000
    elif len(user_coding_languages) == 4:
        new_expected_salary = new_expected_salary + 9000
    else:
        new_expected_salary = new_expected_salary + 6500
if len(user_coding_languages) == 4:
    new_expected_salary = new_expected_salary + 9000
    print("Perfect! You are a model candidate for the position, we can negotiate a $9k bump in you annual salary after "
          "for the amount of Coding Languages you know. ")
    print()

if int(users_experience) == 4:
    expected_salary = expected_salaries[user_info["State"]]
    new_expected_salary = expected_salary + 10000
    print("We're giving you an additional $10k increase to your base salary for the many years of experience you have "
          "in this field.")
    print()
    if len(user_coding_languages) == 4:
        new_expected_salary = new_expected_salary + 9000
    elif len(user_coding_languages) == 5:
        new_expected_salary = new_expected_salary + 11000
    else:
        new_expected_salary = new_expected_salary + 8500
if len(user_coding_languages) == 5:
    new_expected_salary = new_expected_salary + 11000
    print("With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual salary.")
    print()

print("Expect $" + str(new_expected_salary) + " for your level of experience.")
print()

for item in expected_salaries:
    if user_info["State"] == item in expected_salaries:
        print("You’re base expected salary for just living in " + str(user_state) + " could have been $" + str(
            expected_salaries[item]) + ".")
        break

more_candidates = input("Do you want to enter another another candidate?")

if more_candidates.upper() != "Y":
    loop_val = False

pass

# now, print out all the ones you've collected, no matter how many (as long as there's one)
for user in user_list:
    print(user)
