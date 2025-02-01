import psycopg2
import os

def insert_data(data):
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cleaned_data (
            id SERIAL PRIMARY KEY,
            Date TIMESTAMP,
            Message_ID INTEGER,
            Channel_Title TEXT,
            Channel_Username TEXT,
            Message TEXT,
            Message_Date TIMESTAMP,
            Media_Path TEXT
        )
    ''')

    # Insert data
    for _, row in data.iterrows():
        cursor.execute('''
            INSERT INTO cleaned_data (Message_ID, Channel_Username, Message, Message_Date, Media_Path)
            VALUES (%s, %s, %s, %s, %s)
        ''', (row['Message_ID'], row['Channel_Username'], row['Message'], row['Message_Date'], row['Media_Path']))

    conn.commit()
    cursor.close()
    conn.close()