def validate_grade():
    while True:
        try:
            grade = float(input("Enter student grade (0-100) = "))

            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")