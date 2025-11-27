def get_student_input(num_subjects):
    name = input("Enter Student Nmae : ")
    marks = []
    print(f"--- Enter marks for {num_subjects} Subjects ---")
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for Subject {i+1} : "))
        marks.append(mark)
    return name, marks
def calculate_metrics(marks_list):
    total_score = sum(marks_list)
    average_score = total_score / len(marks_list)
    return total_score, average_score

def calculate_metrics(marks):
    total_score = sum(marks)
    average_score = total_score / len(marks)
    return total_score, average_score


def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def display_report_card(name, marks, total, average, grade):
    print("\n" + "="*30)
    print(f"REPORT CARD: {name.upper()}")
    print("="*30)
    print(f"Marks Obtained: {marks}")
    print(f"Total Score:    {total:.2f}")
    print(f"Average:        {average:.2f}%")
    print("-" * 30)
    print(f"FINAL GRADE:    {grade}")
    
    if grade == 'F':
        print("Result:         FAIL")
    else:
        print("Result:         PASS")
    print("="*30 + "\n")


def main():
    print("Welcome to the Student Grade Calculator")
    
    num_subjects = int(input("Enter number of subjects: "))

    student_name, student_marks = get_student_input(num_subjects)

    total, avg = calculate_metrics(student_marks)

    final_grade = determine_grade(avg)

    display_report_card(student_name, student_marks, total, avg, final_grade)


if __name__ == "__main__":
    main()
