import csv

# Global list to store student records
students = []

def add_student():
    try:
        name = input("Enter student's name: ")
        roll_number = input("Enter roll number: ")

        marks = []
        for i in range(1, 4):
            while True:
                try:
                    mark = float(input(f"Enter marks for Subject {i}: "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Marks should be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")

        total = sum(marks)
        average = round(total / 3, 2)

        student = {
            "Name": name,
            "Roll Number": roll_number,
            "Subject 1": marks[0],
            "Subject 2": marks[1],
            "Subject 3": marks[2],
            "Total Marks": total,
            "Average Marks": average
        }

        students.append(student)
        print("Student added successfully.\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_all():
    if not students:
        print("No student records found.\n")
        return
    for idx, s in enumerate(students, start=1):
        print(f"--- Student {idx} ---")
        for key, value in s.items():
            print(f"{key}: {value}")
        print()

def save_to_csv(filename='students.csv'):
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = ["Name", "Roll Number", "Subject 1", "Subject 2", "Subject 3", "Total Marks", "Average Marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Records saved to {filename} successfully.\n")
    except Exception as e:
        print(f"Failed to write to file: {e}")

def main_menu():
    while True:
        print("\n📘 Student Data Tracker CLI")
        print("1. Add Student")
        print("2. Display All Records")
        print("3. Save Records to CSV")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all()
        elif choice == '3':
            save_to_csv()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.\n")

if __name__ == "__main__":
    main_menu()
