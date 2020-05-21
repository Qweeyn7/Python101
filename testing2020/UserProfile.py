# Error message I'm getting is "create_unique_id" is undefined

#UserProfile.py
# UserProfile.py

"""
user_info = {"DOB": user_dob, "Age": user_age, "Full Name": user_full_name, "Country": user_country, "State":
    user_state, "is_active": id(is_active), "Years of Education": user_number_of_education_years}
"""


class UserProfile:
    def __init__(self, user_dob, user_age, user_full_name, user_country, user_state, user_number_of_education_years):
        self.password = "bad password"
        self.email = None
        self.is_active = True
        self.user_dob = user_dob
        self.user_age = user_age
        self.user_full_name = user_full_name
        self.user_state = user_state
        self.user_country = user_country
        self.user_number_of_education_years = user_number_of_education_years

        def get_age(self):
            return self.age

        def set_password(self, new_password):
            self.password = new_password

        def get_password(self):
            return self.password

        def create_user_id(self):
            random_id = id(self.user_full_name)
            return random_id

        def get_dob(self):
            return self.dob

        def set_full_name(self, full_name):
            self.full_name = full_name

        def get_country(self):
            return self.country

        def set_country(self, country):
            self.country = country

        def get_state(self):
            return self.state

        def set_state(self, state):
            self.state = state

        def get_number_of_experience_years(self):
            return self.number_of_education_years

        def set_number_of_experience_years(self, number_of_experience_years):
            self.number_of_experience_years = number_of_experience_years

        def get_number_of_education_years(self):
            return self.number_of_education_years

        def set_number_of_education_years(self, number_of_education_years):
            self.number_of_education_years = number_of_education_years