from main import connect_database

# establish connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #SQL query to combine workoutsessions and members and return the details of individuals between the ages of 25-30
        query = """
     SELECT w.session_id as session_id, m.id as id, m.name AS name, m.age AS age, w.trainer_id as trainer_id
     FROM members m, workoutsessions w
     where w.session_id = m.id And m.age BETWEEN 25 and 30
        """

        #implement the query
        cursor.execute(query)
        
        for order in cursor.fetchall():
            print(order)

    except Exception as e:
        print(f"Error: {e}")
    
    # close cursor and connection
    finally:
        cursor.close()
        conn.close()