# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: Classes and Methods
# Change Log: (Who, When, What)
# Nana Adomako,12/05/2023,Created Script
# ------------------------------------------------------------------------------------------ #



import json

class Student:
    def __init__(self, first_name="", last_name="", course_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.course_name = course_name

    def to_dict(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "course_name": self.course_name}

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course_name}"

class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name, student_data):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                student_data.extend(Student(**item) for item in data)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Error reading data from {file_name}. Starting with an empty list.")

    @staticmethod
    def write_data_to_file(file_name, student_data):
        try:
            with open(file_name, 'w') as file:
                json.dump([student.to_dict() for student in student_data], file, indent=2)
            print(f"Data written to {file_name} successfully.")
        except Exception as e:
            print(f"Error writing data to file: {e}")

class IO:
    @staticmethod
    def output_error_messages(message, error=None):
        print(f"Error: {message}\nDetails: {error}" if error else f"Error: {message}")

    @staticmethod
    def output_menu(menu):
        print(menu)

    @staticmethod
    def input_menu_choice():
        return input("Enter your choice (1-4): ")

    @staticmethod
    def input_student_data(student_data):
        student_data.append(Student(input("Enter student's first name: "), input("Enter student's last name: "), input("Enter course name: ")))

if __name__ == "__main__":
    MENU = """
    ---- Course Registration Program ----
      Select from the following menu:  
        1. Register a Student for a Course
        2. Show current data  
        3. Save data to a file
        4. Exit the program
    -----------------------------------------
    """
    FILE_NAME = "Enrollments.json"
    menu_choice = ""
    students = []

    FileProcessor.read_data_from_file(FILE_NAME, students)

    while menu_choice != "4":
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == "1":
            IO.input_student_data(students)
        elif menu_choice == "2":
            print(*students, sep='\n')
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
