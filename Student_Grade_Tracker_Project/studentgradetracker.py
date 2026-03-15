import pandas as pd
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
                df = pd.DataFrame(students)
                df.to_csv('student_grade_records.csv', index = False)

                print(f"Data for the student {name1} saved successfully!")

            except ValueError:
                print("Invalid input. Please enter the valid marks for the given {subject}.")

        elif choice == '2':
            filename = "student_grade_records.csv"

            if not students:
                print("\nNo data stored yet. Please add a student record first.")
            else:
                try:
                    df = pd.DataFrame(students)
                        
                    df.to_csv(filename, index = False)
                    print(f"Sucessfully saved the record to {filename}")
                    print("\n---Current Grade Report ---")

                    print(df.to_string(index=False))

                    avg = df['grade'].mean() # Optional but will make things much faster
                    print("-" * 30)
                    print(f"Total Students: {len(df)}")
                    print(f"Overall Class Average: {avg:.2f}")
                    print("-" * 30)

                except Exception as e:
                    print(f"Error in trying to save or display records: {e}")
        
        elif choice == '3':
            print("Exiting Program.....\nGoodBye!")
            break

        else:
            print("Invalid choice. Please enter 1,2 or 3")

if __name__ == "__main__":
    main()
