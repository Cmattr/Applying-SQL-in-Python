from main import connect_database
from datetime import datetime

#imput variables
member_id = int(input("Enter your member ID: "))
Session_id = int(input("Enter a new session ID: "))
date = input("Enter a date (yyyy-mm-dd): ")
time = input("Enter a time: ")
activity = input("Enter the type of exercise: ")
trainer = int(input("Enter a trainer_id: "))

# establish connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        #SQL query to create a new work out session
        query = "INSERT INTO workoutsessions (session_id, member_id, session_date, session_time, activity, trainer_id) VALUES (%s, %s, %s, %s, %s, %s)"

        #implement the query
        cursor.execute(query, (Session_id, member_id, date, time, activity, trainer))
        conn.commit()
        print("Work out session successfully added to the calender")

    # close cursor and connection
    finally:
        cursor.close()
        conn.close()
        