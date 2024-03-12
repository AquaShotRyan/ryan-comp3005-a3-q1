# ryan-comp3005-a3-q1
### How to run
1. Install python (this program uses 3.11.8)
2. Install psycopg2 with ``` pip install psycopg2 ```
3. Run postgres
4. Create ```students``` table in postgres with
```
CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	enrollment_date DATE
);
```
6. Add login info to ``` operations.py ```
7. Navigate to the project folder
8. Run ``` py main.py ``` in the terminal
