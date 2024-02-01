student_details = {
	'John': {'age': 20, 'grade': 'A', 'major': 'Computer Science'},
	'Emma': {'age': 21, 'grade': 'B', 'major': 'Mathematics'},
	'Michael': {'age': 19, 'grade': 'A', 'major': 'Physics'},
	# Add more students here
}


def find_student_details(student_name):
	if student_name in student_details:
		return student_details[student_name]
	else:
		return "not found"
# Main program
if __name__ == "__main__":
	# Get input from the user
	name = input("Enter the student's name: ")

	# Find and display the details of the entered student
	details = find_student_details(name)
	print(details)
