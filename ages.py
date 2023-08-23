

def check_age(user_age_input: int) -> str:
    if user_age_input <= 0:
        return 'Passed invalid age'
    elif user_age_input >= 1:
        if user_age_input >= 19:
            if user_age_input >= 66:
                return 'Happy retirement!'
            elif user_age_input <= 65:
                return 'You need to find a job'
        elif user_age_input <= 18:
            return 'You are still a child'
