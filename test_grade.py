from grade import letter_grade, class_average, highest_score


def test_letter_grade():
    assert letter_grade(95) == "A"
    assert letter_grade(90) == "A"
    assert letter_grade(85) == "B"
    assert letter_grade(75) == "C"
    assert letter_grade(65) == "D"
    assert letter_grade(50) == "F"
    print("test_letter_grade: ALL PASSED")


def test_class_average():
    assert class_average([100, 80, 60]) == 80.0
    assert class_average([90, 90, 90]) == 90.0
    assert class_average([50]) == 50.0
    print("test_class_average: ALL PASSED")


def test_highest_score():
    assert highest_score([70, 85, 90, 60]) == 90
    assert highest_score([50]) == 50
    assert highest_score([-10, -20, -5]) == -5
    print("test_highest_score: ALL PASSED")


# Run tests
test_letter_grade()
test_class_average()
test_highest_score()

print("--- All tests passed! ---")