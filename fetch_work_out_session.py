from main import connect_database

# establish connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #SQL query to retieve and display work out sessions
        query = "SELECT * FROM workoutsessions"

        #implement the query
        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

    # close cursor and connection
    finally:
        cursor.close()
        conn.close()