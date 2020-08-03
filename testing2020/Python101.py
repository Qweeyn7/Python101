users_experience = input(
    "How many years of experience do you have?\n[1] Less than 1 year experience.\n"
    "[2] 1-3 years of experience.\n[3] 3-8 years of experience.\n[4]"
    "8+ years of experience.\n")

users_experience = int(users_experience)
print()

users_coding_languages = str(
    input("Which Coding Languages do you know? (Separate each language by a comma)\n"))
print("Before Split: " + users_coding_languages)

users_coding_languages = users_coding_languages.split(",")
print("After Split: " + str(users_coding_languages))

if users_experience == 1:
    print("Expect between $40K & $60K for your level of experience.")
    if len(users_coding_languages) < 3:
        print("Learn more Coding Languages: Deduct $10k from expected salary.")

elif users_experience == 2:
    print("Expect between $60K & $80K for your level of experience.")
    if len(users_coding_languages) < 3:
        print("Learn more Coding Languages: Deduct $5k from expected salary.")

elif users_experience == 3:
    print("Expect between $80K & $120K for your level of experience.")

elif users_experience == 4:
    print("Expect at least $130K for your level of experience.")
    if len(users_coding_languages) > 5:
        print(
            "With your proficiency with multiple Coding Languages, we can negotiate a $11k bump in your annual salary.")
else:
    print(10 * '*' + "Invalid input: Please use one of the four options above." + 10 * '*')
