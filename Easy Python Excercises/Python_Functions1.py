# Easy function for Hello World

def hello_world():
    return "Hello World!"

def get_hello_world():
    return "Hello World!"


##########################################################################################################

# Accepts a given number as a function parameter.
#checks if the given number is even or odd.
#prints "even" if the number is even.
#prints "odd" if the number is odd.
#has a default value of 7 if no number if supplied.

def check_even_odd(number=7):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


##########################################################################################################

# Python function to classify people as either 
#adults (greater than or equal to 18 years old) or 
#children (less than 18 years old)

def classify_age(age):
    if age >= 18:
        return "adult"
    else:
        return "child"

##########################################################################################################

# RIVM Vaccine Registration
## Write a Python function which prints out the vaccine registration date, vaccine and location for a user supplied year of birth.

def get_vaccination_location(year_of_birth):
    if year_of_birth == '1931 or earlier':
        print("Location: Groningen")
    elif year_of_birth == '1932 - 1936':
        print("Location: Arnhem")
    elif year_of_birth == '1937 - 1941':
        print("Location: Breda")
    elif year_of_birth == '1942 - 1946':
        print("Location: Harlingen")
    elif year_of_birth == '1947 - 1951':
        print("Location: Edam")
    elif year_of_birth == '1952 - 1955':
        print("Location: Amsterdam")
    elif year_of_birth == '1956 - 1957':
        print("Location: Sittard")
    elif year_of_birth == '1958 - 1960':
        print("Location: Rotterdam")
    elif year_of_birth == '1961 - 1971':
        print("Location: Groningen")
    elif year_of_birth == '1972 - 1981':
        print("Location: Arnhem")
    elif year_of_birth == '1982 - 1991':
        print("Location: Breda")
    elif year_of_birth == '1992 or later':
        print("Location: Maastricht")
    else:
        print("Invalid year of birth. Please provide a valid year.")



def ask_question(response):
    if response == 'Y':
        return True
    elif response == 'N':
        return False
    else:
        print("Invalid response. Please reply with (Y)es or (N)o")
        return None

def flowchart_logic():
    symptoms = ask_question('Y')
    contact = ask_question('N')
    
    if symptoms:
        cough = ask_question('Y')
        if cough:
            fever = ask_question('Y')
            if fever:
                print("Self-isolate, get tested, and contact healthcare provider")
            else:
                print("Monitor symptoms")
        else:
            shortness_of_breath = ask_question('Y')
            if shortness_of_breath:
                print("Self-isolate, get tested, and contact healthcare provider")
            else:
                print("Monitor symptoms")
    elif contact:
        print("Monitor symptoms")
    else:
        print("No symptoms or contact. No action needed.")