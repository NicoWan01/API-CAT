	# Creating the Student class: We’ll define a Student class with attributes for the student’s name and grades. The grades will be stored as a dictionary with subjects as keys and corresponding grades as values. Here’s an example implementation:
class Student:
	    def __init__(self, name):
	        self.name = name
self.grades = {}  # Initialize an empty dictionary for grades
	
def add_grade(self, subject, grade):
	        """
	        Adds a grade for a subject.
	
	        Args:
	            subject (str): Name of the subject.
	            grade (float): Grade obtained by the student.
	
	        Returns:
 	            None
	        """
self.grades[subject] = grade

def get_average_grade(self):
	        """
	        Calculates and returns the average grade for the student.

	        Returns:
	            float: Average grade.
	        """
if not self.grades:
	            return 0.0  # No grades available
total_grades = sum(self.grades.values())
return total_grades / len(self.grades)
	
	# Example usage:
student1 = Student("Florence")
student1.add_grade("History", 87)
student1.add_grade("Biology", 90)
print(f"{student1.name}'s average grade: {student1.get_average_grade()}")

# Creating the Classroom class: We’ll define a Classroom class with methods to manage students. Here’s an example implementation:

class Classroom:
	    def __init__(self):
	        self.students = []  # Initialize an empty list for students
	
def add_student(self, student):
	        """
	        Adds a student to the classroom.
	
	        Args:
	            student (Student): An instance of the Student class.

	        Returns:
	            None
	        """
self.students.append(student)
	
def display_all_students(self):
        """
	        Displays details of all students in the classroom.
	
	        Returns:
	            None
	        """
for student in self.students:
            print(f"Student: {student.name}, Grades: {student.grades}")
	
def get_class_average(self, subject):
	        """
	        Calculates and returns the class average for a specific subject.
	
	        Args:
	            subject (str): Name of the subject.
	
	        Returns:
	            float: Class average for the subject.
	        """
total_grades = 0
num_students = len(self.students)
for student in self.students:
	            if subject in student.grades:
	                total_grades += student.grades[subject]
	        return total_grades / num_students if num_students > 0 else 0.0
	
	# Example usage:
classroom = Classroom()
classroom.add_student(student1)
	# Add more students if needed
classroom.display_all_students()
print(f"Class average for Math: {classroom.get_class_average('Math')}")
