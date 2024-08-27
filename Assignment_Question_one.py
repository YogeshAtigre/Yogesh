import maskpass , re
def check_password_strength(passwd):
    contains_upper = False
    contains_lower = False
    contains_digit = False
    contains_special = False

    # To check the lenght of the provided passwsord is greater than 8 characters
    if len(passwd)<8:
        return False
    else:
        for char in passwd:
            # To check if the provided password contains uppercase letters
            if char.isupper():
                contains_upper = True
            # To check if the provided password contains lowercase letters
            if char.islower():
                contains_lower = True
            # To check if the provided password contains digits from 0 to 9
            if char.isdigit() and '1' <= char <= '9':
                contains_digit = True
            # To check if the provided password contains special characters
            if re.search(r'[!@#$%^&*(),.?":{}|<>]', char):
                contains_special = True
        if contains_upper and contains_lower and contains_digit and contains_special:
            return True
    return False   
# To mask the password provided by user for security 
passwd= maskpass.advpass()

# To display final result to the user
if check_password_strength(passwd) == True:
    print ("The provided password is very strong")
else:
    print("The password should be at least 8 characters long , must contain both uppercase and lowercase letters and must contain at least one digit and must contain at least one special character")