import MySQLdb


def query_data():
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user="root", password="", database="YourDatabaseName")
    cursor = db.cursor()

    # Query data from the table
    query_data_query = "SELECT * FROM Employees"

    cursor.execute(query_data_query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the data
    for row in rows:
        print(row)

    # Close the connection
    db.close()


# Call the function to query and fetch data
query_data()