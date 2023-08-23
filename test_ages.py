from ages import check_age


def test_invalid_age():
    expected_result = 'Passed invalid age'
    age = -1
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_child_age():
    expected_result = 'You are still a child'
    age = 9
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_working_age():
    expected_result = 'You need to find a job'
    age = 25
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_retirement_age():
    expected_result = 'Happy retirement!'
    age = 70
    actual_result = check_age(age)
    assert actual_result == expected_result
