from main import connect_database

# establish connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #SQL query to retrieve and display members
        query = "SELECT * FROM members"

        #implement the query
        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

    # close cursor and connection
    finally:
        cursor.close()
        conn.close()