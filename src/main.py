from database.db import MariaDBConnection
from model.translate import getRespone
from lesson.convert_en_to_ta import getLesson
from question.question_ta import getQuestion
import asyncio

languages = {
    "Tamil": "ta_IN",
    "Telugu": "te_IN",
    "Hindi": "hi_IN"
}

def main():
    getQuestion()
    # asyncio.run(getQuestion())
    
    
    # getLesson()
    # Create a database connection
    # db_connection = MariaDBConnection()
    # db_connection.connect()

    # Execute a sample query
    # query = "SELECT * FROM users"
    # results = db_connection.execute_query(query)
    # for row in results:
    #     print(row)

    # Close the database connection
    # db_connection.close()

    # Translate a sample text to Tamil
    # lang = languages["Tamil"]
    # translation = getRespone("Hello, world!", lang)
    # print("Translated text:", translation)

if __name__ == "__main__":
    main()