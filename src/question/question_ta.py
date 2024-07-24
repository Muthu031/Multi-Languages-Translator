from datetime import datetime
from database.db import MariaDBConnection  
from model.translate import getRespone

def get_all_question(db):
    query = "SELECT question_id, sub_topic_key, question_text FROM question WHERE sub_topic_key BETWEEN 1 AND 1"
    return db.execute_query(query)

def get_last_question_id(db):
    query_question = "SELECT question_id FROM question ORDER BY question_id DESC LIMIT 1"
    result_question = db.execute_query(query_question)
    last_question_id = result_question[0][0] if result_question else None

    query_question_TA = "SELECT question_id FROM question_ta ORDER BY question_id DESC LIMIT 1"
    result_question_TA = db.execute_query(query_question_TA)
    last_question_TA_id = result_question_TA[0][0] if result_question_TA else None

    print(f"Last question_id in question table: {last_question_id}")
    print(f"Last question_id in question_ta table: {last_question_TA_id}")

    if last_question_id is not None and (last_question_TA_id is None or last_question_id > last_question_TA_id):
        return last_question_id
    else:
        return last_question_TA_id

def extract_numeric_part(question_id):
    numeric_part = ''.join(filter(str.isdigit, question_id))
    return int(numeric_part)

def generate_new_question_id(last_question_id):
    if last_question_id:
        last_number = extract_numeric_part(last_question_id)
        new_number = last_number + 1
    else:
        new_number = 1
    return f"NT-QN-TA-{str(new_number).zfill(4)}"

def getQuestion():
    db = MariaDBConnection()
    db.connect()

    try:
        question = get_all_question(db)
        last_question_id = get_last_question_id(db)
        lang = "ta_IN"

        if question:
            for question_id, sub_topic_key, question_text in question:
                new_question_id = generate_new_question_id(last_question_id)
                last_question_id = new_question_id

                translated_text = getRespone(question_text, lang)
                translated_question = translated_text[0] if isinstance(translated_text, list) else translated_text

                print(f"Translated Tamil question: {translated_question}")

                insert_query = """
                INSERT INTO question_ta(question_id, sub_topic_key, question_text, language, translated_by, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """
                insert_data = (new_question_id, sub_topic_key, translated_question, 'TA', 'mbart', datetime.now())

                rowcount = db.execute_update(insert_query, insert_data)
                # print(f"Inserted {rowcount} row(s)")

        else:
            print("No data found")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        db.close()