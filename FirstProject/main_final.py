#  ask the user to input their experiance by asking them a question using the input() function
'''http://www.w3schools.com/python/ref_func_input.asp'''

#  use an if/elif/else statement to check to see if the user chose option 1,2,3, or 4
"""http://www.w3schools.com/python/python_conditions.asp"""

#  if the user chose option 1, print out "Expect between $40,000 and $60,000 for your level of experience"

#  else if the user chose option 2, print out "Expect between $60,000 and $80,000 for your level of experience"

#  else if the user chose option 3, print out "Expect between $80,000 and $120,000 for your level of experience"

# else if the user chose option 4, print out "Expect at least $130,000 for your level of experience"


# homework - else enter a default message if the user does not choose a valid option
while True:
    try:
        user_dob = input("Enter Date of Birth (MM/DD/YYYY):")
        user_age = int(input("Enter Current Age:"))
        user_full_name = input("Enter Full Name:")
        user_country = input("Enter Country:")
        user_state = input("Enter State (Please enter the 2 letter abbreviation):")
        is_active = True
        user_number_of_education_years = input("Enter the number of years you've been learning code.")
        user_info = {"DOB": user_dob, "Age": user_age, "FullName": user_full_name, "Country": user_country, "State":
                     user_state, "is_active": is_active, "EducationYears":user_number_of_education_years}
        break
    except ValueError:
        print("Please answer all questions.")

expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}
valid_states = ("CA", "NY", "FL", "NC", "TX")

users_experience = input(
    "How many years of experience do you have developing software?\n[1] Less than 1 year experience.\n"
    "[2] 1-3 years of experience.\n[3] 3-8 years of experience.\n[4]"
    "8+ years of experience.\n")

if int(users_experience) == 1:
    print("Expect between $40,000 and $60,000 for your level of experience.")

elif int(users_experience) == 2:
    print("Expect between $60,000 and $80,000 for your level of experience.")

elif int(users_experience) == 3:
    print("Expect between $80,000 and $120,000 for your level of experience.")

elif int(users_experience) == 4:
    print("Expect at least $130,000 for your level of experience.")

else:
    print("Sorry, invalid option selected.")

user_coding_languages = input("Which Coding Languages do you know? (Separate each language by commas)\n")

print("Before split():" + user_coding_languages)
user_coding_languages = user_coding_languages.split(",")
print("After split():" + str(user_coding_languages))

if len(user_coding_languages) < 3:
    print("Learn more Coding Languages, deduct $10k from expected salary.")

elif len(user_coding_languages) == 3:
    print("Great! We can add a minimum of $5k to your annual salary.")

elif len(user_coding_languages) >= 5:
    print("With your proficiency with multiple Coding Languages, we can negotiate a $15k bump in your annual salary.")

elif len(user_coding_languages) == 4:
    print(
        "Perfect! You are a model candidate for the position, we can negotiate a $10k bump in you annual salary after "
        "quarterly reviews ")

if input("Do you want to enter another another candidate? ").upper == "Y":
    loop_val = True
else:
    print(user_info)
