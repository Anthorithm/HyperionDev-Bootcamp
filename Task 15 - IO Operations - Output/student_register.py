# This script allows for registering students for an exam venue by writing their ID numbers to a file.

def register_students():
    # Ask for the number of students to register
    num_students = int(input("How many students are registering? "))

    # Open the file for writing student ID numbers
    with open('reg_form.txt', 'w') as file:
        # Loop through the number of students to register
        for _ in range(num_students):
            # Ask for each student's ID number
            student_id = input("Enter the next student ID number: ")
            # Write the student ID and a dotted line for signature to the file
            file.write(f"{student_id}\n----------------------\n")

if __name__ == "__main__":
    register_students()

     # No need to explicitly call file.close(), it's automatically handled

