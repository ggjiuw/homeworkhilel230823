

def check_age(user_age_input):
    if user_age_input <= 0:
        check_age_output = 'Passed invalid age'
    elif user_age_input >= 1:
        if user_age_input >= 19:
            if user_age_input >= 66:
                check_age_output = 'Happy retirement!'
            elif user_age_input <= 65:
                check_age_output = 'You need to find a job'
        elif user_age_input <= 18:
            check_age_output = 'You are still a child'

    return check_age_output


user_age = int(input('Enter your age > '))

print(check_age(user_age))
