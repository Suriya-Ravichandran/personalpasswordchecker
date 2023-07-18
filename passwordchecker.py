def check_password_strenght(password):
    len_weight=2
    com_weight=1
    patt_weight=1
    
    #Lenght criterion
    len_score=min(len(password)/8,1)*len_weight
    
    #complexity criterion
    has_uppercase=any(char.isupper() for char in password)
    has_lowercase=any(char.islower() for char in password)
    has_digit=any(char.isdigit() for char in password)
    has_special=any(not char.isalnum() for char in password)
    com_score=(has_uppercase + has_lowercase + has_digit + has_special)/4 * com_weight

    #pattern critertion
    patt=['123','abc','qwerty','@123','password']#add more patterns as needed
    patt_score= -patt_weight
    for pattern in patt:
        if pattern in password.lower():
            patt_score +=patt_weight

    #calculate over all strength_score
    strenght_score = len_score + com_score + patt_score
    return strenght_score

#main program
password = input("Enter your password: ")
strenght_score = check_password_strenght(password)

#Evaluate password strength level
if strenght_score >=2:
    strenght_level="strong"
elif strenght_score >=1:
    strenght_level="medium"
else:
    strenght_level ="week"
print("password strength level:" + strenght_level) 

