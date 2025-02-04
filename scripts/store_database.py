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
            INSERT INTO cleaned_data (Message_ID, Channel_Title, Channel_Username, Message, Message_Date, Media_Path)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (row['ID'], row['Channel Title'], row['Channel Username'], row['Message'], row['Date'], row['Media Path']))

    conn.commit()
    cursor.close()
    conn.close()