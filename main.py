import operations # import functions needed for app
import datetime
import os

# convert date in 'YYYY/MM/DD' string format into datetime.date object
def parseDate(date: str):
    split = date.split('/')
    print(split)
    year = int(split[0])
    month = int(split[1])
    day = int(split[2])
    
    return datetime.date(year, month, day)

def main():
    while True:
        print(
        """
        Select an option by typing in its number
        (1) - Print all students
        (2) - Add a student
        (3) - Update a student's email
        (4) - Delete a student
        """
        )
        ans = int(input("SELECTION: "))
    
main()