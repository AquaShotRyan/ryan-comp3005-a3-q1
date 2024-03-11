import psycopg2
import datetime

# connect to database
try: 
    conn = psycopg2.connect("dbname='students' user='postgres' host='localhost' password='pass'")
except:
    print("failed to connect to database")

# retrieves and diisplays all records from the students table
def getAllStudents():
    cur = conn.cursor() # open cursor to perform queries
    cur.execute("SELECT * FROM students;")

    # get list of all students
    allStudents = cur.fetchall()

    # loop through every student and print them out one by one
    for i in range(len(allStudents)):
        # get singular student
        student = allStudents[i]

        # get attributes
        id = student[0]
        first_name = student[1]
        last_name = student[2]
        email = student[3]
        year = student[4].year
        month = student[4].month
        day = student[4].day
        date = f"{year}/{month}/{day}"

        # print the student
        txt = "{:<5} {:<10} {:<10} {:<30} {:<10}"
        print(txt.format(id, first_name, last_name, email, date))
    
    cur.close()

# inserts a new student record into students table
def addStudent(first_name: str, last_name: str, email: str, enrollment_date: datetime.date):
    cur = conn.cursor() # open cursor to perform queries

    # perform INSERTION query using execute()
    cur.execute(
    """ 
    INSERT INTO students (first_Name, last_name, email, enrollment_date)
    VALUES (%(fName)s, %(lName)s, %(email)s, %(date)s);
    """,
    {'fName': first_name, 'lName': last_name, 'email': email, 'date': enrollment_date}
    )

    cur.close()

# updates the email address for a student with the specified student_id
def updateStudentEmail(student_id: int, new_email: str):
    cur = conn.cursor() # open cursor to perform queries

    # perform UPDATE query using execute()
    cur.execute(
    """
    UPDATE students
    SET email = %s
    WHERE student_id = %s;
    """, (new_email, student_id)# only 2 values, don't need to use dictionary
    )

    cur.close()

# deletes the record of the student with specified student_id
def deleteStudent(student_id: int):
    cur = conn.cursor() # open cursor to perform queries

    # perform DELETE query using execute()
    cur.execute(
    """
    DELETE FROM students
    WHERE student_id = %s;
    """, (student_id, )# need comma because it needs to be a tuple (or list or dictionary)
    )

    cur.close()

def main():
    getAllStudents()

    # make changes persist
    conn.commit()
    # close the connection
    conn.close()

main()