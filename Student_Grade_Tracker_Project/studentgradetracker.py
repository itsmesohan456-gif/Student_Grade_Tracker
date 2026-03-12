import csv
import os


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades)  / len(grades)

def main():
    students = []

    while True:

        print("--- Welcome to Student Grade Tracker ---")

        print("1. Add Student Data")
        print("2. View Stored Data of Students")
        print("3. Exit the Program")

        choice = input("\nSelect an option (1-3):")

    
        if choice == '1':
            name1 = input("\nEnter the student's name:")

            subject = input("Enter subject of the student:")

            try:
                grade = float(input(f"Enter marks for the subject {subject}:"))

                student_data = {
                "name": name1,
                "subject": subject,
                "grade": grade
                }
                students.append(student_data)

                print(f"Data for the student {name1} saved successfully!")

            except ValueError:
                print("Invalid input. Please enter the valid marks for the given {subject}.")

        elif choice == '2':
            filename = "student_grade_records.csv"
            fields = ['ID', 'Name', 'Subject', 'Grade']

            if not students:
                print("\nNo data stored yet. Please add a student record first.")
            else:
                try:
                    with open(filename, mode = 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(fields)
                        print("\n--- Current Grade Report ---")

                        all_grades = []
                        for s in students:
                            print(f"Student: {s['name']}  | Subject: {s['subject']}  | Grade: {s['grade']}")

                            writer.writerow([s.get('id', 'N/A'), s['name'], s['subject'], s['grade']])
            
                        all_grades.append(s['grade'])

                        avg = calculate_average(all_grades)
                        print(f"\nTotal Students: {len(students)}")
                        print(f"Overall Class Average: {avg:.2f}")

                    print(f"\nSucessfully saved the record to {filename}")
                except Exception as e:
                    print(f"Error in trying to save the record in CSV: {e}")
        
        elif choice == '3':
            print("Exiting Program.....\nGoodBye!")
            break

        else:
            print("Invalid choice. Please enter 1,2 or 3")

if __name__ == "__main__":
    main()
