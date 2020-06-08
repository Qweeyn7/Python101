# UserProfile.py

"""
user_info = {"DOB": user_dob, "Age": user_age, "Full Name": user_full_name, "Country": user_country, "State":
 user_state, "is_active": id(is_active), "Years of Education": user_number_of_education_years}
"""


class UserProfile:
    def __init__(self, user_dob, user_age, user_full_name, user_country, user_state, user_number_of_education_years):
        self.password = "A password has been created for you."
        self.email = "Email Field Empty."
        self.is_active = None
        self.user_dob = user_dob
        self.user_age = user_age
        self.user_full_name = user_full_name
        self.user_state = user_state
        self.user_country = user_country
        self.user_number_of_education_years = user_number_of_education_years

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password

    def get_email(self):
        return self.email

    def set_email(self, user_email):
        self.email = user_email

    def get_age(self):
        return self.age

    def set_age(self, user_age):
        self.age = user_age

    def create_user_id(self):
        random_id = id(self.user_full_name)
        return random_id

    def get_user_country(self):
        return self.country

    def set_user_country(self, new_country):
        self.user_country = new_country


class Designer(UserProfile):
    def __init__(self, user_dob, user_age, user_full_name, user_country, user_state, user_number_of_education_years,
                 software_toolbox):
        super().__init__(user_dob, user_age, user_full_name, user_country, user_state,
                         user_number_of_education_years)
        self.software_programs = software_toolbox

    def get_software_programs(self):
        return self.software_programs

    def set_software_programs(self, new_software_toolbox):
        self.software_programs = new_software_toolbox


class Developer(UserProfile):
    def __init__(self, user_dob, user_age, user_full_name, user_country, user_state, user_number_of_education_years,
                 coding_toolbox):
        super().__init__(user_dob, user_age, user_full_name, user_country, user_state,
                         user_number_of_education_years)
        self.coding_languages = coding_toolbox

    def get_coding_languages(self):
        return self.coding_lanuages

    def set_coding_languages(self, user_coding_languages):
        self.coding_languages = user_coding_languages
