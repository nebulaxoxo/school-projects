import mysql.connector

def display_records():
    username = 'root'
    password = 'nebula_3F0'
    database_name = 'assignments'
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(user=username, password=password, database=database_name)
        cursor = connection.cursor()
        query = "SELECT * FROM Employee WHERE Salary > 75000"
        cursor.execute(query)
        records = cursor.fetchall()
        if records:
            print("Records with Salary greater than 75000:")
            for record in records:
                print(record)
        else:
            print("No records found.")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

display_records()