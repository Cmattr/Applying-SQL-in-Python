from main import connect_database

#imput variables
member_id = int(input("input a new user id (must be a number): "))
member_name = input("input new members name: ")
member_age = int(input("Input new member age: "))
conn = connect_database()

# establish connection
if conn is not None:
    try: 
        cursor = conn.cursor()

        # input New member details
        new_member = (member_id, member_name, member_age)

        #SQL Query to input a new member
        query = "INSERT INTO Members (id, name, age) VALUES(%s, %s, %s)"

        #implement the query
        cursor.execute(query, new_member)
        conn.commit()
        print("New customer added successfully")

    # close cursor and connection
    finally:
        cursor.close()
        conn.close()