import mysql.connector

def add_column_city():
    try:
        username = 'root'
        password = 'sales_emp'
        database_name = 'Office'
        connection = mysql.connector.connect(user=username, password=password, database=database_name)
        cursor = connection.cursor()
        add_column_query = "ALTER TABLE salesman ADD COLUMN city VARCHAR(255)"
        cursor.execute(add_column_query)
        connection.commit()
        print("New column 'city' added successfully.")

    except mysql.connector.Error as e:
        print("Error: ", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def update_salary_mumbai():
    try:
        username = 'root'
        password = 'sales_emp'
        database_name = 'Office'
        connection = mysql.connector.connect(user=username, password=password, database=database_name)
        cursor = connection.cursor()
        update_salary_query = "UPDATE salesman SET Salary = Salary * 1.05 WHERE city = 'Mumbai'"
        cursor.execute(update_salary_query)
        connection.commit()
        print("Salary updated successfully for salespersons in Mumbai.")
    except mysql.connector.Error as e:
        print("Error: ", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

add_column_city()
update_salary_mumbai()
