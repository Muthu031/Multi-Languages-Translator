from database.db import MariaDBConnection

lesson = []
def getLesson():
    # Create a database connection
    db_connection = MariaDBConnection()
    db_connection.connect()

    # Execute a sample query
    query = "SELECT * FROM lesson"
    results = db_connection.execute_query(query)
    for row in results:
        lesson.append(row[1])
    # Close the database connection
    db_connection.close()
    return lesson
