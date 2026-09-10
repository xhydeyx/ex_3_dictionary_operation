student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# First, display the complete record using for loop, printing and some string formatting only
print("Student Record:")
for key, value in student.items():
    print(f"{key}: {value}")

# Check if there's a key called 'email'. If not, ask the user to enter an email
if 'email' not in student:
    email = input("Enter email: ")
    student['email'] = email

# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string
new_city = input("Enter new city: ").strip()
while new_city == "":
    new_city = input("City cannot be empty. Enter new city: ").strip()
student['city'] = new_city

# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method
if student.get('phone') is None:
    print("Phone number not found.")
    phone = input("Enter phone number: ")
    student['phone'] = phone

# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.
student['contact'] = {
    'phone': student.get('phone'),
    'email': student.get('email')
}

# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores
student['courses'] = {
    'Python': 88,
    'Databases': 91,
    'Software Engineering': 84
}

# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead. 
total = 0
count = 0
for score in student['courses'].values():
    total += score
    count += 1
average = total / count

# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score. 
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".
if average >= 90:
    status = "Excellent"
elif average >= 75:
    status = "Good"
elif average >= 60:
    status = "Pass"
else:
    status = "At Risk"
student['academic_status'] = status

# Add the logic to search for a course. 
# If the course is found, print the course name and score. If not, print "Course not found".
search_course = input("Enter course name to search: ")
if search_course in student['courses']:
    print(f"{search_course}: {student['courses'][search_course]}")
else:
    print("Course not found")

# Add the logic to update a course score. 
# Ask the user to enter the course name and the new score. 
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100
update_course = input("Enter course name to update: ")
if update_course in student['courses']:
    new_score_str = input(f"Enter new score for {update_course} (0-100): ")
    if new_score_str.isdigit():
        new_score = int(new_score_str)
        if 0 <= new_score <= 100:
            student['courses'][update_course] = new_score
            print(f"Updated {update_course} score to {new_score}.")
        else:
            print("Score must be between 0 and 100.")
    else:
        print("Invalid score. Please enter a number.")
else:
    print("Course not found.")

# Recaclculate the average score and update the academic status after the course score has been updated.
total = 0
count = 0
for score in student['courses'].values():
    total += score
    count += 1
average = total / count
if average >= 90:
    status = "Excellent"
elif average >= 75:
    status = "Good"
elif average >= 60:
    status = "Pass"
else:
    status = "At Risk"
student['academic_status'] = status

# Display the final formatted student record with all the updated information, including the average score and academic status.
print("\n=====================================")
print("        STUDENT RECORD")
print("=====================================\n")
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}\n")
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}\n")
print("COURSE RESULTS")
for course, score in student['courses'].items():
    print(f"{course}: {score}")
print(f"\nAverage Score: {average:.1f}")
print(f"Academic Status: {student['academic_status']}\n")
print("=====================================")
# It should look like the following: 
""" 
=====================================
        STUDENT RECORD
=====================================

Name: Alice Wong
Student ID: ST1024
Age: 21
Program: Software Engineering
City: Shanghai
GPA: 3.6

CONTACT
Phone: 13800001111
Email: alice.wong@university.edu

COURSE RESULTS
Python: 88
Databases: 91
Software Engineering: 84

Average Score: 87.7
Academic Status: Good

===================================== """

