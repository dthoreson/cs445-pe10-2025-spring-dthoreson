import datetime

def calculate_age(year, month, day):
    #start off with figuring out the current date, month and year
    today = datetime.date.today()
    #take in user inputs and put them in the same format as our today variable
    given_birthday = datetime.date(year, month, day)
    #check to make sure they match
    print(today, given_birthday)
    #check the two years we will be comparing
    print(today.year, given_birthday.year)
    #find the age by simply subtracting the current year from the birth year given
    age = today.year - given_birthday.year

    return age

birth_year = 1996
birth_month = 2
birth_day = 29

age = calculate_age(birth_year, birth_month, birth_day)
print(f"Your age is: {age}")


#for edge cases, we would add stuff like checking for accurate inputs from the user to ensure the date is a valid date and also
#for the ages that are under a year old, we would create a separate section in the code to check for these cases to give the proper age