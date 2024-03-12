import operations # import functions needed for app
import datetime

# convert date in 'YYYY/MM/DD' string format into datetime.date object
def parseDate(date: str):
    split = date.split('/')
    year = int(split[0])
    month = int(split[1])
    day = int(split[2])
    
    return datetime.date(year, month, day)

def main():
    while True:# while loop for repeatedly showing a menu
        print(
        """
Select an option by typing in its number
(0) - Reset table with default values
(1) - Print all students
(2) - Add a student
(3) - Update a student's email
(4) - Delete a student
(5) - Exit the application
        """
        )
        ans = int(input("SELECTION: "))# ask for option to perform
        match ans:
            case 0:
                operations.initialize()
                print("Students table reset")
            case 1:# print all students
                operations.getAllStudents()
            case 2:# add a student
                fName = input("first_name: ")
                lName = input("last_name: ")
                email = input("email: ")
                date = input("enrollment_date (i.e 2023/2/2 for Feb 2, 2023): ")
                operations.addStudent(fName, lName, email, parseDate(date))
                print(f"Added {fName}.")
            case 3:# update an email
                update_id = int(input("student_id: "))
                new_email = input("email: ")
                operations.updateStudentEmail(update_id, new_email)
                print(f"Updated email for student {update_id}")
            case 4:# delete a student
                delete_id = int(input("student_id: "))
                operations.deleteStudent(delete_id)
                print(f"Deleted student {delete_id}")
            case 5:# exit application
                print("Exiting the application.")
                break
                
    
main()