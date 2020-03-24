valid_states = ("FL", "NY", "CA", "TX", "NC")  # You had a colon here, when it should have been an =.

expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}

user_full_name = input("Enter full name: \n")

user_dob = input("Enter Date of birth (mm/dd/yyyy): \n")

user_country = input("Enter Country: \n")

user_state = input("Choose your state you : \n")  # You want to define user state before calling it below.

print( valid_states[0] )  # You originally had it as user_state but user_state had no value
print( valid_states[1] )
print( valid_states[2] )
print( valid_states[3] )
print( valid_states[4] )

user_is_active = True

number_of_education_years = input("Please enter the how many years you have been coding: \n")

user_info = {"DOB": user_dob, "Full Name": user_full_name, 'Country': user_country, 'State': user_state,
             "user_is_active": user_is_active, "number_of_education_years": number_of_education_years}

new_expected_salary = 0  # Define before calling it below
expected_salary = 0  # Define before calling it below

users_experience = input(
    "How many years of experience do you have developing software? " "\n[1]Less than 1 year" "\n[2] 1-3 years of "
    "experience" "\n[3] 3-8 years of experience" "\n[4] 8+ years of experience\n" )  # Define before calling it below

users_coding_languages = input( "What languages do you know? (separate each language by a comma)" )  # Define before
# calling it below


if int( users_experience ) == 1: expected_salaries = expected_salaries[user_info["state"]]
new_expected_salary = expected_salary - 5000

if len( users_coding_languages ) < 3:
    new_expected_salary = new_expected_salary - 10000
    print( "Learn more Coding Languages; deduct an approx $10k from expected salary." )

elif len( users_coding_languages ) > 3:
    new_expected_salary = new_expected_salary + 10000

else:
    new_expected_salary = new_expected_salary + 5000

print( "Expect $" + str( new_expected_salary ) + " for you level of experience" )

if int( users_experience ) == 2:
    print( "Expect between $60,000 and $80,000 for you level of experience" )

if int( users_experience ) == 3:
    print( "Expect between $80,000 and $120,000 for you level of experience" )

elif int( users_experience ) == 4:
    print( "Expect at least $130,000 for you level of experience" )

else:
    print( "Please insert 1, 2, 3, or 4" )

print( "Before Split(): " + users_coding_languages )

users_coding_languages = users_coding_languages.split( "," )

print( "After Split(): " + str( users_coding_languages ) )
if len( users_coding_languages ) <= 3:

    print( "Learn more Coding Languages and deduct an approx $10k from expected salary" )
elif len( users_coding_languages ) == 3:

    print( "Great! We can add a minimum of an approx $5k to your annual salary." )

elif len( users_coding_languages ) >= 5:

    print(
        "With your knowledge with multiple Coding Languages, we can negotiate an approx $15k increase in your annual "
        "salary." )
elif len( users_coding_languages ) == 4:

    print( "Great! You are our ideal model candidate for the position, when are you available for interview?" )


print(user_info)
