user_experience = input("How many years experience do you have developing software?\n[1] Less than 1 year" 
                        "\n[2] 1-3 years of experience  \n[3] 3-8 years of experience  \n[4]"
                        " 8+ years of experience \n")
user_dob = input("Enter Date of birth: ")
user_full_name = input("Enter full name:")
user_country = input("Enter Country:")
user_state = input("Enter state:")
user_is_active = input("Active or not Active:")
user_info = {"DOB" : user_dob, "Fullname" : user_full_name, "Country" : user_country, "State" : user_state, "Active/NotActive" : user_is_active}
user_coding_languages = input("Which coding languages do you know? (seperate each language by commas)")
print("Before split():" + user_coding_languages)
user_coding_languages = user_coding_languages.split(",")
print("After split():" + str(user_coding_languages))
if len(user_coding_languages) < 3:
    print("learn some more coding languages; deduct $10k from expected salary")
elif len(user_coding_languages) == 3:
    print("Nice start! You can add min $5k to your annual salary by learning 2 or more additional languages")
elif len(user_coding_languages) >= 5:
    print("You are a Master of Languages you can negotiate an additional $5k to your salary ")
elif len(user_coding_languages) == 4:
    print("Good job! you are right on track to becoming a Master of code")
if int(user_experience) == 1:
    print("Expect between $40,000 for your level of experience")
elif int(user_experience) == 2:
    print("Expect between $60,000 and $80,000 for your level of experience")
elif int(user_experience) == 3:
    print("Expect between $80,000 and $120,000 for your level of experience")
elif int(user_experience) == 4:
    print("Expect at least 130,000 for your level of experience")
else:
    print("Enter Valid Option either 1, 2, 3, or 4")
try:
  print(user_dob)
except:
  print("An exception has occured enter dob")
print(user_info)