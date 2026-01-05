import json

class Person:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self): return self._id
    @property
    def name(self): return self._name

    def __str__(self): return f"ID: {self.id}, Name: {self.name}"

    def to_dict(self): return {"id": self._id, "name": self._name, "type": "person"}

class Student(Person):
    def __init__(self, id, name, branch):
        super().__init__(id, name)
        self._major = branch
        self._enrolled_course_codes = []

    @property
    def major(self): return self._major
    @major.setter
    def major(self, value): self._major = value
    @property
    def enrolled_course_codes(self): return list(self._enrolled_course_codes)

    def enroll_course(self, code): 
        if code not in self._enrolled_course_codes: self._enrolled_course_codes.append(code)

    def drop_course(self, code): 
        if code in self._enrolled_course_codes: self._enrolled_course_codes.remove(code)

    def display_details(self): 
        return f"{super().__str__()}, Major: {self.major}, Enrolled: {len(self._enrolled_course_codes)}"

    def to_dict(self): 
        return {"id": self._id, "name": self._name, "major": self._major, 
                "enrolled_courses": self._enrolled_course_codes, "type": "student"}

class Faculty(Person):
    def __init__(self, id, name, dept):
        super().__init__(id, name)
        self._department = dept
        self._assigned_course_codes = []

    @property
    def department(self): 
        return self._department
    @department.setter
    def department(self, value): 
        self._department = value
    @property
    def assigned_course_codes(self): 
        return list(self._assigned_course_codes)

    def assign_course(self, code): 
        if code not in self._assigned_course_codes: 
            self._assigned_course_codes.append(code)

    def unassign_course(self, code): 
        if code in self._assigned_course_codes: 
            self._assigned_course_codes.remove(code)

    def display_details(self): 
        return f"{super().__str__()}, Dept: {self.department}, Assigned: {len(self._assigned_course_codes)}"

    def to_dict(self): 
        return {"id": self._id, "name": self._name, "department": self._department, 
                "assigned_courses": self._assigned_course_codes, "type": "faculty"}

class Course:
    def __init__(self, code, title, credits, prereqs=None):
        self._course_code = code
        self._title = title
        self._credits = credits
        self._prerequisite_codes = prereqs if prereqs else []
        self._enrolled_student_ids = []
        self._assigned_faculty_id = None

    @property
    def course_code(self):
        return self._course_code
    @property
    def title(self): 
        return self._title
    @property
    def credits(self): 
        return self._credits
    @property
    def prerequisite_codes(self): 
        return list(self._prerequisite_codes)
    @property
    def enrolled_student_ids(self): 
        return list(self._enrolled_student_ids)
    @property
    def assigned_faculty_id(self): 
        return self._assigned_faculty_id
    @assigned_faculty_id.setter
    def assigned_faculty_id(self, value): 
        self._assigned_faculty_id = value

    def add_prerequisite(self, code): 
        if code not in self._prerequisite_codes: 
            self._prerequisite_codes.append(code)

    def add_student_id(self, sid): 
        if sid not in self._enrolled_student_ids:
            self._enrolled_student_ids.append(sid)

    def remove_student_id(self, sid): 
        if sid in self._enrolled_student_ids: 
            self._enrolled_student_ids.remove(sid)

    def assign_faculty_id(self, fid): 
        self._assigned_faculty_id = fid
    def unassign_faculty_id(self): 
        self._assigned_faculty_id = None

    def display_details(self): 
        return f"Code: {self.course_code}, Title: {self.title}, Credits: {self.credits}, " \
               f"Prereqs: {self._prerequisite_codes}, Enrolled: {len(self._enrolled_student_ids)}, " \
               f"Faculty: {self._assigned_faculty_id or 'None'}"

    def to_dict(self): 
        return {"course_code": self._course_code, "title": self._title, "credits": self._credits,
                "prerequisites": self._prerequisite_codes, "enrolled_students": self._enrolled_student_ids,
                "assigned_faculty_id": self._assigned_faculty_id}

# You can now instantiate and use these classes in a console interface or script.
students = {}
faculty = {}
courses = {}

def main():
    while True:
        print("\n=== University Management System ===")
        print("1. Add Student\n2. Add Faculty\n3. Add Course")
        print("4. Enroll Student in Course\n5. Assign Faculty to Course")
        print("6. View Course Roster\n7. Exit")
        choice = input("Choose: ")

        if choice == '1':
            sid = input("Student ID: ")
            name = input("Name: ")
            branch = input("Branch: ")
            if sid not in students:
                students[sid] = Student(sid, name, branch)
                print("Student added.")
            else:
                print("Student already exists.")

        elif choice == '2':
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            if fid not in faculty:
                faculty[fid] = Faculty(fid, name, dept)
                print("Faculty added.")
            else:
                print("Faculty already exists.")

        elif choice == '3':
            code = input("Course Code: ")
            title = input("Title: ")
            credits = int(input("Credits: "))
            prereqs = input("Prerequisites (comma-separated): ").split(",") if input("Any prereqs? y/n: ") == 'y' else []
            if code not in courses:
                courses[code] = Course(code, title, credits, prereqs)
                print("Course added.")
            else:
                print("Course already exists.")

        elif choice == '4':
            sid = input("Student ID: ")
            code = input("Course Code: ")
            if sid in students and code in courses:
                student = students[sid]
                course = courses[code]
                if all(p in student.enrolled_course_codes for p in course.prerequisite_codes):
                    student.enroll_course(code)
                    course.add_student_id(sid)
                    print("Enrollment successful.")
                else:
                    print("Prerequisites not satisfied.")
            else:
                print("Student or course not found.")

        elif choice == '5':
            fid = input("Faculty ID: ")
            code = input("Course Code: ")
            if fid in faculty and code in courses:
                faculty[fid].assign_course(code)
                courses[code].assign_faculty_id(fid)
                print("Faculty assigned.")
            else:
                print("Faculty or course not found.")

        elif choice == '6':
            code = input("Course Code: ")
            if code in courses:
                course = courses[code]
                print(course.display_details())
                for sid in course.enrolled_student_ids:
                    print(" -", students[sid].name)
            else:
                print("Course not found.")

        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()