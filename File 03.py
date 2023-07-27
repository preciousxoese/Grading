#Grading system for infinite users until the user types 'Exit'

def calculate_grade(score):
    if  score <= 100 and score >= 79.5:
        return "A", 4.0, "Excellent"
    elif score >= 74.5:
        return "B+", 3.5, "Very Good"
    elif score >= 69.5:
        return "B", 3.0, "Good" 
    elif score >= 64.5:
        return "C+", 2.5, "Average"
    elif score >= 59.5:
        return "C", 2.0, "Fair"
    elif score >= 54.5:
        return "D+", 1.5, "Barely Satisfactory"
    elif score >= 49.5:
        return "D", 1.0, "Weak Pass"
    else:
        return "E", 0, "Fail"


def main():
    try:
        while True:
            raw_score = input("Enter the score (type 'EXIT' to quit): ")
            if raw_score.upper() == "EXIT":
                break

            try:
                raw_score = float(raw_score)
            except ValueError:
                print("Invalid input. Please enter a valid score.")
                continue

            grade, grade_point, interpretation = calculate_grade(raw_score)
            print(f"Grade: {grade}\nGrade Point: {grade_point}\nInterpretation: {interpretation}")

        print("Grading system has been terminated successfully.")

    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
