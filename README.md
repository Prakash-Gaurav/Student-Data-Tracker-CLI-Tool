# Student-Data-Tracker-CLI-Tool
A Python-based CLI app for managing student records. Add, display, and save student data with marks calculation. Built using Python and CSV file handling, it's a simple and efficient tool for educators and administrators to manage student data.

---

## Project Setup
This project requires Python 3.x. No external libraries are strictly necessary beyond the standard library modules csv and os.


### Requirements
- Python 3.x
- Save the whole CLI code inside a folder as "student_data_tracker.py" file.
- Create a virtual Environment using:
```bash
python -m venv student_env
```
- Activate the environment:
```bash
student_env\Scripts\Activate
```

### Running the Script

```bash
python student_data_tracker.py
```



## Features

**1. Add Student (add_student function):**
- This option allows users to input details for a new student. They'll be prompted to enter the student's name, roll number, and marks for three subjects.

- The application includes robust input validation to ensure that marks entered are numerical and fall within the valid range of 0 to 100.

- Once all details are entered, the system automatically calculates the total marks and average marks for the student.

- The student's data is then stored as a dictionary and added to an in-memory list.

**2. Display All Records (display_all function):**
- Selecting this option will show all student records currently stored in the application's memory.

- If no students have been added yet, a message indicating "No student records found" will be displayed.

- Each student's details, including their name, roll number, individual subject marks, total marks, and average marks, are presented in a clear, formatted manner, with marks and averages rounded to two decimal places for readability.

**3. Calculate Overall Average Marks:** 
- This new option calculates the average of the "Average Marks" from all students currently in the system. It provides a quick overview of the collective performance of all recorded students.

**4. Save Records to CSV (save_to_csv function):**
- This feature allows users to export all the student data to a Comma Separated Values (CSV) file.

- By default, the file will be named students.csv and will be saved in the same directory where user run the script.

- The CSV file will include clear headers for each data field (Name, Roll Number, Subject 1, Subject 2, Subject 3, Total Marks, Average Marks), making it easy to open and analyze in spreadsheet software like Microsoft Excel or Google Sheets.

- The application includes comprehensive exception handling for file operations to gracefully manage potential issues during the saving process.

**5. Exit:**
- This option allows users to gracefully exit the application, ending the program execution.

**Note:**
The main_menu function serves as the central interactive component of the application. It operates within a continuous while True loop, presenting users with a clear set of options: adding a student, displaying all records, saving records to CSV, or exiting the program. The function accepts user input for their choice and uses an if-elif-else structure to direct control to the appropriate function. It gracefully handles invalid choices by printing an informative message and allows the user to exit the program cleanly.



---

## Columns in CSV
- Name
- Roll Number
- Subject 1
- Subject 2
- Subject 3
- Total Marks
- Average Marks

---

## Terminal Interface Overview
```
PS C:\Users\ADMIN\Desktop\VS code student_data_tracker> student_env\scripts\activate
(student_env) PS C:\Users\ADMIN\Desktop\VS code student_data_tracker> python student_data_tracker.py

📘 Student Data Tracker CLI
1. Add Student
2. Display All Records
3. Save Records to CSV
4. Exit
Enter your choice (1-4): 1
Enter student's name: Prakash Gaurav
Enter roll number: 19
Enter marks for Subject 1: 91
Enter marks for Subject 2: 89
Enter marks for Subject 3: 85
Student added successfully.


📘 Student Data Tracker CLI
1. Add Student
2. Display All Records
3. Save Records to CSV
4. Exit
Enter your choice (1-4): 2
--- Student 1 ---
Name: Prakash Gaurav
Roll Number: 19
Subject 1: 91.0
Subject 2: 89.0
Subject 3: 85.0
Total Marks: 265.0
Average Marks: 88.33


📘 Student Data Tracker CLI
1. Add Student
2. Display All Records
3. Save Records to CSV
4. Exit
Enter your choice (1-4): Akash Gaurav
Invalid choice. Please select from 1 to 4.


📘 Student Data Tracker CLI
1. Add Student
2. Display All Records
3. Save Records to CSV
4. Exit
Enter your choice (1-4): 1
Enter student's name: Akash Gaurav
Enter roll number: 2
Enter marks for Subject 1: 91
Enter marks for Subject 2: 95
Enter marks for Subject 3: 90
Student added successfully.


📘 Student Data Tracker CLI
1. Add Student
2. Display All Records
3. Save Records to CSV
4. Exit
Enter your choice (1-4): 2
--- Student 1 ---
Name: Prakash Gaurav
Roll Number: 19
Subject 1: 91.0
Subject 2: 89.0
Subject 3: 85.0
Total Marks: 265.0
Average Marks: 88.33

--- Student 2 ---
Name: Akash Gaurav
Roll Number: 2
Subject 1: 91.0
Subject 2: 95.0
Subject 3: 90.0
Total Marks: 276.0
Average Marks: 92.0


📘 Student Data Tracker CLI
1. Add Student
2. Display All Records
3. Save Records to CSV
4. Exit
Enter your choice (1-4): 3
Records saved to students.csv successfully.


📘 Student Data Tracker CLI
1. Add Student
2. Display All Records
3. Save Records to CSV
4. Exit
Enter your choice (1-4): 4
Exiting program. Goodbye!
```
