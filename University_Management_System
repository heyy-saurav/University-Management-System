# --- 1. Person Class (Base Class) ---
class Person:
    def __init__(self, person_id: str, name: str):
        if not person_id:
            print("Warning: Person ID should not be empty.")
        if not name:
            print("Warning: Person name should not be empty.")
        self._id = person_id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}"

    def to_dict(self):
        return {
            'id': self._id,
            'name': self._name
        }

# --- 2. Student Class ---
class Student(Person):
    def __init__(self, student_id: str, name: str, major: str):
        super().__init__(student_id, name)
        if not major:
            print("Warning: Student major should not be empty.")
        self._major = major
        self._enrolled_course_codes = []  

    def get_major(self):
        return self._major

    def set_major(self, new_major: str) :
        if not new_major:
            print("Warning: Major should not be empty.")
        self._major = new_major

    def get_enrolled_course_codes(self) :
        return list(self._enrolled_course_codes)

    def enroll_course(self, course_code: str):
        if not course_code:
            print("Error: Course code cannot be empty.")
            return 
        if course_code not in self._enrolled_course_codes:
            self._enrolled_course_codes.append(course_code)

    def drop_course(self, course_code: str):
        if not course_code:
            print("Error: Course code cannot be empty.")
            return 
        if course_code in self._enrolled_course_codes:
            self._enrolled_course_codes.remove(course_code)

    def display_details(self):
        return (f"{super().__str__()}, Type: Student, Major: {self._major}, "
                f"Enrolled Courses: {len(self._enrolled_course_codes)}")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            'type': 'student',
            'major': self._major,
            'enrolled_course_codes': self._enrolled_course_codes
        })
        return data

# --- 3. Faculty Class ---
class Faculty(Person):
    def __init__(self, faculty_id: str, name: str, department: str):
        super().__init__(faculty_id, name) 
        if not department:
            print("Warning: Faculty department should not be empty.")
        self._department = department
        self._assigned_course_codes = [] 
    def get_department(self):
        return self._department

    def set_department(self, new_department: str):
        if not new_department:
            print("Warning: Department should not be empty.")
        self._department = new_department

    def get_assigned_course_codes(self):
        return list(self._assigned_course_codes)

    def assign_course(self, course_code: str) :
        if not course_code:
            print("Error: Course code cannot be empty.")
            return 
        if course_code not in self._assigned_course_codes:
            self._assigned_course_codes.append(course_code)

    def unassign_course(self, course_code: str):
        if not course_code:
            print("Error: Course code cannot be empty.")
            return 
        if course_code in self._assigned_course_codes:
            self._assigned_course_codes.remove(course_code)

    def display_details(self):
        return (f"{super().__str__()}, Type: Faculty, Department: {self._department}, "
                f"Assigned Courses: {len(self._assigned_course_codes)}")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'type': 'faculty',
            'department': self._department,
            'assigned_course_codes': self._assigned_course_codes
        })
        return data

# --- 4. Course Class ---
class Course:
    def __init__(self, course_code: str, title: str, credits: int, prerequisites: list = None):
        if not course_code:
            print("Warning: Course code should not be empty.")
        if not title:
            print("Warning: Course title should not be empty.")
        if not credits or credits <= 0:
            print("Warning: Credits should be a positive number.")
        if prerequisites is None:
            prerequisites = []
        self._course_code = course_code
        self._title = title
        self._credits = credits
        self._prerequisite_codes = list(prerequisites) 
        self._enrolled_student_ids = []  
        self._assigned_faculty_id = None 

    def get_course_code(self):
        return self._course_code

    def get_title(self) :
        return self._title

    def get_credits(self) :
        return self._credits


    def get_prerequisite_codes(self): 
        return list(self._prerequisite_codes)

    def get_enrolled_student_ids(self) :
        return list(self._enrolled_student_ids)

    def get_assigned_faculty_id(self): 
        return self._assigned_faculty_id

    def set_assigned_faculty_id(self, faculty_id) :
        if faculty_id is not None and not faculty_id:
            print("Warning: Faculty ID should not be empty if provided.")
        self._assigned_faculty_id = faculty_id

    def add_prerequisite(self, prerequisite_code: str):
        if not prerequisite_code:
            print("Error: Prerequisite code cannot be empty.")
            return
        if prerequisite_code not in self._prerequisite_codes:
            self._prerequisite_codes.append(prerequisite_code)

    def add_student_id(self, student_id: str):
        if not student_id:
            print("Error: Student ID cannot be empty.")
            return 
        if student_id not in self._enrolled_student_ids:
            self._enrolled_student_ids.append(student_id)

    def remove_student_id(self, student_id: str) :
        if not student_id:
            print("Error: Student ID cannot be empty.")
            return 
        if student_id in self._enrolled_student_ids:
            self._enrolled_student_ids.remove(student_id)

    def display_details(self):
        faculty_info = f"Assigned Faculty ID: {self._assigned_faculty_id}" if self._assigned_faculty_id else "No faculty assigned"
        prereqs = ", ".join(self._prerequisite_codes) if self._prerequisite_codes else "None"
        return (f"Course Code: {self._course_code}, Title: {self._title}, Credits: {self._credits}\n"
                f"  Prerequisites: {prereqs}\n"
                f"  Enrolled Students: {len(self._enrolled_student_ids)}\n"
                f"  {faculty_info}")

    def to_dict(self):
        return {
            'course_code': self._course_code,
            'title': self._title,
            'credits': self._credits,
            'prerequisite_codes': self._prerequisite_codes,
            'enrolled_student_ids': self._enrolled_student_ids,
            'assigned_faculty_id': self._assigned_faculty_id
        }

# --- 5. University Class ---
class University:
    def __init__(self):
        self._students: dict = {} 
        self._faculty: dict = {} 
        self._courses: dict = {} 


    def add_student(self, student) : 
        if student.get_id() in self._students: 
            print(f"Error: Student with ID '{student.get_id()}' already exists.")
            return False
        self._students[student.get_id()] = student 
        print(f"Student '{student.get_name()}' added successfully.") 
        return True

    def remove_student(self, student_id: str) :
        if student_id not in self._students:
            print(f"Error: Student with ID '{student_id}' not found.")
            return False

        student = self._students[student_id]
        if student.get_enrolled_course_codes(): 
            print(f"Error: Student '{student.get_name()}' is enrolled in courses. Drop them first.") 
            return False

        for course_code in list(student._enrolled_course_codes):
            if course_code in self._courses:
                self._courses[course_code].remove_student_id(student_id)

        del self._students[student_id]
        print(f"Student '{student_id}' removed successfully.")
        return True

    def add_faculty(self, faculty) : 
        if faculty.get_id() in self._faculty: 
            print(f"Error: Faculty with ID '{faculty.get_id()}' already exists.")
            return False
        self._faculty[faculty.get_id()] = faculty
        print(f"Faculty '{faculty.get_name()}' added successfully.")
        return True

    def remove_faculty(self, faculty_id: str) :
        if faculty_id not in self._faculty:
            print(f"Error: Faculty with ID '{faculty_id}' not found.")
            return False

        faculty = self._faculty[faculty_id]
        if faculty.get_assigned_course_codes():
            print(f"Error: Faculty '{faculty.get_name()}' is assigned to courses. Unassign them first.") 
            return False
        
        for course_code in list(faculty._assigned_course_codes):
            if course_code in self._courses:
                if self._courses[course_code].get_assigned_faculty_id() == faculty_id: 
                    self._courses[course_code].unassign_faculty_id()

        del self._faculty[faculty_id]
        print(f"Faculty '{faculty_id}' removed successfully.")
        return True

    def add_course(self, course):
        if course.get_course_code() in self._courses: 
            print(f"Error: Course with code '{course.get_course_code()}' already exists.")
            return False
        self._courses[course.get_course_code()] = course 
        print(f"Course '{course.get_title()}' added successfully.") 
        return True

    def remove_course(self, course_code: str):
        if course_code not in self._courses:
            print(f"Error: Course with code '{course_code}' not found.")
            return False

        course = self._courses[course_code]
        if course.get_enrolled_student_ids():
            print(f"Error: Course '{course.get_title()}' has enrolled students. Drop them first.") 
            return False
        if course.get_assigned_faculty_id():
            print(f"Error: Course '{course.get_title()}' has an assigned faculty. Unassign them first.") 
            return False

        for student_id in list(self._students.keys()):
            student = self._students[student_id]
            if course_code in student.get_enrolled_course_codes(): 
                student.drop_course(course_code)

        for faculty_id in list(self._faculty.keys()):
            faculty = self._faculty[faculty_id]
            if course_code in faculty.get_assigned_course_codes():
                faculty.unassign_course(course_code)

        del self._courses[course_code]
        print(f"Course '{course_code}' removed successfully.")
        return True

    def enroll_student_in_course(self, student_id: str, course_code: str) :
        student = self._students.get(student_id)
        course = self._courses.get(course_code)

        if not student:
            print(f"Error: Student with ID '{student_id}' not found.")
            return False
        
        if not course:
            print(f"Error: Course with code '{course_code}' not found.")
            return False

        if course_code in student.get_enrolled_course_codes():
            print(f"Info: Student '{student.get_name()}' is already enrolled in '{course.get_title()}'.") 
            return False

       
        for prereq_code in course.get_prerequisite_codes(): 
            if prereq_code not in student.get_enrolled_course_codes():
                print(f"Error: Student '{student.get_name()}' has not met prerequisite '{prereq_code}' for '{course.get_title()}'.")
                return False
        student.enroll_course(course_code)
        course.add_student_id(student_id)
        print(f"Student '{student.get_name()}' enrolled in '{course.get_title()}' successfully.")
        return True

    def drop_student_from_course(self, student_id: str, course_code: str):
        student = self._students.get(student_id)
        course = self._courses.get(course_code)

        if not student:
            print(f"Error: Student with ID '{student_id}' not found.")
            return False
        
        if not course:
            print(f"Error: Course with code '{course_code}' not found.")
            return False

        if course_code not in student.get_enrolled_course_codes(): 
            print(f"Info: Student '{student.get_name()}' is not enrolled in '{course.get_title()}'.") 
            return False
        student.drop_course(course_code)
        course.remove_student_id(student_id)
        print(f"Student '{student.get_name()}' dropped from '{course.get_title()}' successfully.")
        return True

    def assign_faculty_to_course(self, faculty_id: str, course_code: str):
        faculty = self._faculty.get(faculty_id)
        course = self._courses.get(course_code)

        if not faculty:
            print(f"Error: Faculty with ID '{faculty_id}' not found.")
            return False
        if not course:
            print(f"Error: Course with code '{course_code}' not found.")
            return False

        if course.get_assigned_faculty_id() == faculty_id:
            print(f"Info: Faculty '{faculty.get_name()}' is already assigned to '{course.get_title()}'.") 
            return False
        
        if course.get_assigned_faculty_id() is not None: 
            current_assigned_faculty = self._faculty.get(course.get_assigned_faculty_id()) 
            if current_assigned_faculty:
                current_assigned_faculty.unassign_course(course_code)
            print(f"Info: Unassigned previous faculty '{course.get_assigned_faculty_id()}' from '{course.get_title()}'.") 
        course.set_assigned_faculty_id(faculty_id) 
        faculty.assign_course(course_code)
        print(f"Faculty '{faculty.get_name()}' assigned to '{course.get_title()}' successfully.")
        return True

    def unassign_faculty_from_course(self, faculty_id: str, course_code: str):
        faculty = self._faculty.get(faculty_id)
        course = self._courses.get(course_code)

        if not faculty:
            print(f"Error: Faculty with ID '{faculty_id}' not found.")
            return False
        if not course:
            print(f"Error: Course with code '{course_code}' not found.")
            return False

        if course.get_assigned_faculty_id() != faculty_id:
            print(f"Info: Faculty '{faculty.get_name()}' is not assigned to '{course.get_title()}'.") 
            return False
        course.set_assigned_faculty_id(None)
        faculty.unassign_course(course_code)
        print(f"Faculty '{faculty.get_name()}' unassigned from '{course.get_title()}' successfully.") 
        return True

    def get_course_roster(self, course_code: str): 
        course = self._courses.get(course_code)
        if not course:
            print(f"Error: Course with code '{course_code}' not found.")
            return []

        roster = []
        for student_id in course.get_enrolled_student_ids(): 
            student = self._students.get(student_id)
            if student: 
                roster.append(student)
            else:
                print(f"Warning: Student ID '{student_id}' found in course '{course_code}' roster but student object does not exist in the system.")
        return roster

    def display_all_students(self):
        if not self._students:
            print("\nNo students registered.")
            return
        print("\n--- All Students ---")
        for student in self._students.values():
            print(student.display_details())
        print("--------------------")

    def display_all_faculty(self) :
        if not self._faculty:
            print("\nNo faculty registered.")
            return
        print("\n--- All Faculty ---")
        for faculty in self._faculty.values():
            print(faculty.display_details())
        print("--------------------")

    def display_all_courses(self):
        if not self._courses:
            print("\nNo courses registered.")
            return
        print("\n--- All Courses ---")
        for course in self._courses.values():
            print(course.display_details())
        print("-------------------")

# --- 6. Console Application ---
def get_valid_input(prompt: str, input_type=str, min_value=None, max_value=None): 
    while True:
        try:
            value = input(prompt).strip()
            if not value and input_type == str:
                print("Input cannot be empty. Please try again.")
                continue
            if input_type == int:
                value = int(value)
                if min_value is not None and value < min_value:
                    print(f"Input must be at least {min_value}. Please try again.")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Input must be at most {max_value}. Please try again.")
                    continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


def main():
    university = University() # Initialize university; data is empty on each run

    while True:
        print("\n===== University Management System =====")
        print("1. Manage Students")
        print("2. Manage Faculty")
        print("3. Manage Courses")
        print("4. Enroll/Drop Student in Course")
        print("5. Assign/Unassign Faculty to Course")
        print("6. View Course Roster")
        print("7. Display All Students")
        print("8. Display All Faculty")
        print("9. Display All Courses")
        print("0. Exit")
        print("========================================")

        choice = get_valid_input("Enter your choice: ", int, 0, 9)

        if choice == 1: # Manage Students
            while True:
                print("\n--- Manage Students ---")
                print("1. Add Student")
                print("2. Remove Student")
                print("3. Back to Main Menu")
                student_choice = get_valid_input("Enter your choice: ", int, 1, 3)

                if student_choice == 1:
                    student_id = get_valid_input("Enter student ID: ")
                    name = get_valid_input("Enter student name: ")
                    major = get_valid_input("Enter student major: ")
                    new_student = Student(student_id, name, major)
                    university.add_student(new_student)
                    input("Press Enter to continue...")
                elif student_choice == 2:
                    student_id = get_valid_input("Enter student ID to remove: ")
                    university.remove_student(student_id)
                    input("Press Enter to continue...")
                elif student_choice == 3:
                    break

        elif choice == 2: # Manage Faculty
            while True:
                print("\n--- Manage Faculty ---")
                print("1. Add Faculty")
                print("2. Remove Faculty")
                print("3. Back to Main Menu")
                faculty_choice = get_valid_input("Enter your choice: ", int, 1, 3)

                if faculty_choice == 1:
                    faculty_id = get_valid_input("Enter faculty ID: ")
                    name = get_valid_input("Enter faculty name: ")
                    department = get_valid_input("Enter faculty department: ")
                    new_faculty = Faculty(faculty_id, name, department)
                    university.add_faculty(new_faculty)
                    input("Press Enter to continue...")
                elif faculty_choice == 2:
                    faculty_id = get_valid_input("Enter faculty ID to remove: ")
                    university.remove_faculty(faculty_id)
                    input("Press Enter to continue...")
                elif faculty_choice == 3:
                    break

        elif choice == 3: # Manage Courses
            while True:
                print("\n--- Manage Courses ---")
                print("1. Add Course")
                print("2. Remove Course")
                print("3. Add Prerequisite to Course")
                print("4. Back to Main Menu")
                course_choice = get_valid_input("Enter your choice: ", int, 1, 4)

                if course_choice == 1:
                    course_code = get_valid_input("Enter course code (e.g., CS101): ")
                    title = get_valid_input("Enter course title: ")
                    credits = get_valid_input("Enter credits: ", int, 1)
                    prereq_input = get_valid_input("Enter prerequisite course codes (comma-separated, leave blank if none): ")
                    prerequisites = [p.strip() for p in prereq_input.split(',') if p.strip()]
                    new_course = Course(course_code, title, credits, prerequisites)
                    university.add_course(new_course)
                    input("Press Enter to continue...")
                elif course_choice == 2:
                    course_code = get_valid_input("Enter course code to remove: ")
                    university.remove_course(course_code)
                    input("Press Enter to continue...")
                elif course_choice == 3:
                    course_code = get_valid_input("Enter course code to add prerequisite to: ")
                    prereq_code = get_valid_input("Enter prerequisite course code to add: ")
                    course = university._courses.get(course_code)
                    if course:
                        if prereq_code not in university._courses:
                            print(f"Warning: Prerequisite course '{prereq_code}' does not exist in the system. Adding prerequisite anyway.")
                        course.add_prerequisite(prereq_code)
                        print(f"Prerequisite '{prereq_code}' added to '{course_code}'.")
                    else:
                        print(f"Error: Course '{course_code}' not found.")
                    input("Press Enter to continue...")
                elif course_choice == 4:
                    break

        elif choice == 4: # Enroll/Drop Student in Course
            while True:
                print("\n--- Enroll/Drop Student ---")
                print("1. Enroll Student in Course")
                print("2. Drop Student from Course")
                print("3. Back to Main Menu")
                enroll_drop_choice = get_valid_input("Enter your choice: ", int, 1, 3)

                if enroll_drop_choice == 1:
                    student_id = get_valid_input("Enter student ID: ")
                    course_code = get_valid_input("Enter course code to enroll in: ")
                    university.enroll_student_in_course(student_id, course_code)
                    input("Press Enter to continue...")
                elif enroll_drop_choice == 2:
                    student_id = get_valid_input("Enter student ID: ")
                    course_code = get_valid_input("Enter course code to drop from: ")
                    university.drop_student_from_course(student_id, course_code)
                    input("Press Enter to continue...")
                elif enroll_drop_choice == 3:
                    break

        elif choice == 5: # Assign/Unassign Faculty to Course
            while True:
                print("\n--- Assign/Unassign Faculty ---")
                print("1. Assign Faculty to Course")
                print("2. Unassign Faculty from Course")
                print("3. Back to Main Menu")
                assign_unassign_choice = get_valid_input("Enter your choice: ", int, 1, 3)

                if assign_unassign_choice == 1:
                    faculty_id = get_valid_input("Enter faculty ID: ")
                    course_code = get_valid_input("Enter course code to assign to: ")
                    university.assign_faculty_to_course(faculty_id, course_code)
                    input("Press Enter to continue...")
                elif assign_unassign_choice == 2:
                    faculty_id = get_valid_input("Enter faculty ID: ")
                    course_code = get_valid_input("Enter course code to unassign from: ")
                    university.unassign_faculty_from_course(faculty_id, course_code)
                    input("Press Enter to continue...")
                elif assign_unassign_choice == 3:
                    break

        elif choice == 6: # View Course Roster
            course_code = get_valid_input("Enter course code to view roster: ")
            roster = university.get_course_roster(course_code)
            if roster:
                print(f"\n--- Roster for Course '{course_code}' ---")
                for student_item in roster:
                    print(student_item.display_details())
                print("------------------------------------")
            else:
                if course_code in university._courses:
                    print(f"\nNo students enrolled in course '{course_code}'.")
            input("Press Enter to continue...")

        elif choice == 7: # Display All Students
            university.display_all_students()
            input("Press Enter to continue...")

        elif choice == 8: # Display All Faculty
            university.display_all_faculty()
            input("Press Enter to continue...")

        elif choice == 9: # Display All Courses
            university.display_all_courses()
            input("Press Enter to continue...")

        elif choice == 0:
            print("Exiting University Management System. Goodbye!")
            break

if __name__ == "__main__":
    main()
