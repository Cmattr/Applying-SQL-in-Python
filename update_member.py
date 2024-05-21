from main import connect_database

#imput variables
member_id = input("input the member ID: ")
update_name = input("input the updated name for this member: ")
update_age = int(input("input the updated age for this member "))

# establish connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        update_member = (update_name, update_age, member_id)

        #SQL query to update members
        query = "UPDATE members SET name = %s, age = %s WHERE id = %s"
         
         #implement the query
        cursor.execute(query, update_member)
        conn.commit()
        print("Member details have been updated")
    # close cursor and connection
    finally:
        conn.close()
        cursor.close()