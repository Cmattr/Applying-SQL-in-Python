from main import connect_database

#imput variables
session_id = int(input("input the session ID: "))
member_id = int(input("input the member ID: "))

# establish connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        #SQL query to delete a session from workoutsessions
        query = "DELETE FROM workoutsessions WHERE session_id = %s AND member_id = %s"

        #implement the query
        cursor.execute(query, (session_id, member_id))
        conn.commit()
        print(f"Work out session {session_id} has been deleted successfully")    

    # close cursor and connection
    finally:
        cursor.close()
        conn.close()
        