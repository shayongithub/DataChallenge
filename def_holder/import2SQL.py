import csv

import pyodbc

# Windows Authentication
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=DESKTOP-RCI0U7A\SQLEXPRESS;'
    'Database=Test;'
    'Trusted_Connection=yes;')

cur = conn.cursor()

create_table_querry = "CREATE TABLE Diemthi(StudentID int,Name nvarchar(50),Day_Of_Birth int,Month_Of_Birth int,Year_Of_Birth int,Math float,Literature float,Social_Science float,Natural_Science float,History float,Geography float,Civic_Education float,Biology float,Physics float,Chemistry float,English float)"

cur.execute('DROP TABLE IF EXISTS diemthi')
cur.execute(create_table_querry)

data = []
id_start = 2071000
with open('../result.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        StudentID = id_start
        Name = row[0]
        Day_Of_Birth = int(row[1])
        Month_Of_Birth = int(row[2])
        Year_Of_Birth = int(row[3])
        Math = float(row[4])
        Literature = float(row[5])
        Social_Science = float(row[6])
        Natural_Science = float(row[7])
        History = float(row[8])
        Geography = float(row[9])
        Civic_Education = float(row[10])
        Biology = float(row[11])
        Physics = float(row[12])
        Chemistry = float(row[13])
        English = float(row[14])

        cur.execute("INSERT INTO diemthi(StudentID, Name, Day_Of_Birth,  Month_Of_Birth, Year_Of_Birth,"
                    "Math, Literature, Social_Science, Natural_Science, History, Geography, Civic_Education, "
                    "Biology, Physics, Chemistry,English) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", StudentID, Name,
                    Day_Of_Birth, Month_Of_Birth, Year_Of_Birth,
                    Math, Literature, Social_Science, Natural_Science, History, Geography, Civic_Education,
                    Biology, Physics, Chemistry, English)

        conn.commit()
        id_start += 1
