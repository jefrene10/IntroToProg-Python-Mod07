# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Starter Script
#   EEnriquez, 08/12/24, Updated code for better consistency and data handling
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:
    """
    Class that defines the person data.

    ChangeLog:
    - EEnriquez, 08/12/24, Created Class

    Properties:

    - first_name (str): The student's first name
    - last_name (str): The student's last name.

    Inherited by:

        Student class

    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    # TODO Create a getter and setter for the first_name property (Done)
    @property
    def first_name(self) -> str:
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha():
            self.__first_name = value
        else:
            raise ValueError("First name should not contain numbers.")

    # TODO Create a getter and setter for the last_name property (Done)
    @property
    def last_name(self) -> str:
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha():
            self.__last_name = value
        else:
            raise ValueError("Last name should not contain numbers.")

    # TODO Override the __str__() method to return Person data (Done)
    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}"


# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    """
    A class that represents student data.

    ChangeLog:
    - EEnriquez, 08/12/24, Created Class

    Properties:

    - course_name (str): The student's course name.

    Inherited properties:

    - first_name (str): The student's first name
    - last_name (str): The student's last name.
    """

    # TODO call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name = first_name, last_name = last_name)
        # TODO add a assignment to the course_name property using the course_name parameter (Done)
        self.course_name = course_name

    # TODO add the getter for course_name (Done)
    @property
    def course_name(self) -> str:
        return self._course_name.title()

    # TODO add the setter for course_name (Done)
    @course_name.setter
    def course_name(self, value: str):
        if all(char.isalnum() or char.isspace() for char in value) or not value:
            self._course_name = value
        else:
            raise ValueError("Course name must be alphanumeric.")

    # TODO Override the __str__() method to return the Student data (Done)
    def __str__(self) -> str:
        return f"{super().__str__()}, {self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list[Student]):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        EEnriquez, 08/12/24, Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            with open(file_name, "r") as file:
                file_data = json.load(file)
            for row in file_data:
                student_data.append(Student(row["first_name"], row["last_name"], row["course_name"]))
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list[Student]):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        EEnriquez, 08/12/24, Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be written to the file

        :return: None
        """
        file_data = []
        for student in student_data:
            file_data.append({'first_name': student.first_name,
                              'last_name': student.last_name,
                              'course_name': student.course_name})
        file = None
        # write dictionary rows into JSON and display to end user
        try:
            file = open(file_name, "w")
            json.dump(file_data, file, indent=1)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        # close file if not already
        finally:
            if not file.closed and file is not None:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    EEnriquez, 08/12/24, Created class


    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        EEnriquez, 08/12/24, Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        EEnriquez, 08/12/24, Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        EEnriquez, 08/12/24, Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list[Student]):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        EEnriquez, 08/12/24, Created function

        :param student_data: list of Student objects to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} {student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list[Student]):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        EEnriquez, 08/12/24, Created function

        :param student_data: list of Student objects to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = Student(first_name=student_first_name, last_name=student_last_name, course_name=course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
