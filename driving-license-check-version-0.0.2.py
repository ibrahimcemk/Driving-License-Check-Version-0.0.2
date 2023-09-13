# Get user's name and age
name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))

# Check if the user is eligible for a driver's license
if age < 16:
    print(f"Sorry, {name}, if you are under 16 years old, you cannot get a driver's license.")
else:
    # Get the user's education status
    education = input('Please Enter Your Education Status: "Primary school", "Middle school", "High School", "Undergraduate", "Master Degree", "Ph. D.", "Associate Degree": ')

    # Determine eligibility based on education
    if education == "Primary school" or education == "Middle school":
        print(f"Sorry, {name}, you did not receive it because your education level ({education}) is not sufficient for a driver's license.")
    else:
        print(f"Congratulations, {name}! Based on your age and education ({education}), you are eligible to get a driver's license.")
    
    # Ask the user if they have any questions
    ask_question = input("Do you have any questions about getting a driver's license? (yes/no): ").strip().lower()
    if ask_question == "yes":
        print("Feel free to ask your questions. We're here to help!")
    else:
        print("If you have any questions in the future, don't hesitate to ask. Have a great day!")
       
    input("break")        


