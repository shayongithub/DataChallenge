import csv
import glob
import json
import os
import shutil
import time

import loguru
import pandas as pd
import pymongo
import pyodbc
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def clean(path):
    file = open(path, encoding='utf-8', mode="r")

    # Read first student
    datas = file.read().split("\n")

    # Removing the header and the empty element at the end of the list
    datas.pop(0)
    datas.pop(len(datas) - 1)

    with open("filtered.csv", encoding="utf8", mode="w", newline='') as file_csv:
        header = ["tên", "dd", "mm", "yy", "toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học",
                  "vật lí", "hóa học", "tiếng anh"]
        writer = csv.writer(file_csv)
        writer.writerow(header)

    for i in datas:
        # make data becomes a list
        i = i.split(",")
        for a in range(len(i)):
            i[a] = i[a].replace("\n", "")
            i[a] = i[a].replace("\t", "")
            i[a] = i[a].replace("\r", "")
        for a in range(len(i)):
            i[a] = i[a].strip()
        unemtyLine = []
        for a in range(len(i)):
            if i[a] != "":
                unemtyLine.append(i[a])
        i = unemtyLine

        name = i[0]
        dob = i[1]
        scores = i[2]
        name = name.lower()
        scores = scores.lower()
        name = name.lower()
        scores = scores.lower()
        # 		# split
        dob_list = dob.split("/")
        dd = int(dob_list[0])
        mm = int(dob_list[1])
        yy = int(dob_list[2])

        scores = scores.replace(":", "")

        scores = scores.replace("khxh ", "khxh   ")
        scores = scores.replace("khtn ", "khtn   ")

        scores_list = scores.split("   ")
        i = [name, str(dd), str(mm), str(yy)]

        for subject in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học",
                        "tiếng anh"]:

            if subject in scores_list:
                subject_name_position = scores_list.index(subject)
                subject_score_position = subject_name_position + 1
                subject_score = scores_list[subject_score_position]
                i.append(str(subject_score))
            else:
                i.append("-1")

        # 	# write data to test.txt
        with open("filtered.csv", "a", encoding='utf-8', newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(i)


def create_server_connection(server_name):
    try:
        conn = pyodbc.connect(
            'Driver={driver};'
            'Server={server};'
            'Trusted_Connection=yes;'.format(driver='{ODBC Driver 17 for SQL Server}', server=server_name))
    except ValueError as err:
        loguru.logger.warning(f'Error: {err}')
    return conn


def create_db_connection(server_name, db_name):
    try:
        conn = pyodbc.connect(
            'Driver={driver};'
            'Server={server};'
            'Database={db_name};'
            'Trusted_Connection=yes;'.format(driver='{ODBC Driver 17 for SQL Server}', server=server_name,
                                             db_name=db_name))
    except ValueError as err:
        loguru.logger.warning(f'Error: {err}')

    return conn


def import2sql(csvPath):
    # Windows Authentication
    server_name = 'DESKTOP-RCI0U7A\SQLEXPRESS'
    conn = create_server_connection(server_name)
    conn.autocommit = True

    # Access to SQL to create database
    cur = conn.cursor()
    db_name = 'KithiTHPTQG'

    cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    cur.execute(f'CREATE DATABASE {db_name}')
    cur.close()

    # Access to the database you have just created
    conn_db = create_db_connection(server_name, db_name)
    cur_db = conn_db.cursor()

    create_table_querry = "CREATE TABLE Diemthi(StudentID int,Name nvarchar(50),Day_Of_Birth int,Month_Of_Birth int,Year_Of_Birth int,Math float,Literature float,Social_Science float,Natural_Science float,History float,Geography float,Civic_Education float,Biology float,Physics float,Chemistry float,English float)"

    cur_db.execute('DROP TABLE IF EXISTS diemthi')
    cur_db.execute(create_table_querry)

    id_start = 2071000
    with open(csvPath, encoding='utf-8') as csv_file:
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

            cur_db.execute("INSERT INTO diemthi(StudentID, Name, Day_Of_Birth,  Month_Of_Birth, Year_Of_Birth,"
                           "Math, Literature, Social_Science, Natural_Science, History, Geography, Civic_Education, "
                           "Biology, Physics, Chemistry,English) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", StudentID,
                           Name,
                           Day_Of_Birth, Month_Of_Birth, Year_Of_Birth,
                           Math, Literature, Social_Science, Natural_Science, History, Geography, Civic_Education,
                           Biology, Physics, Chemistry, English)

            conn_db.commit()
            id_start += 1
    loguru.logger.info('Import successfully. Check your SQLServer !')

def import2mongoDB(csvPath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['diemthi']  # Replace mongo db name
    collection_name = 'finalAssignment'  # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, csvPath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

    loguru.logger.info('Import successfully. Check your MongoDB !')


class Watcher:
    DIRECTORY_TO_WATCH = "F:\Python\Data1\Assignment 1\diemthi\csv"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return None
        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            loguru.logger.info("Received csv - %s." % event.src_path)
            time.sleep(2)
            # The path to start looking for usedcsv file
            path = 'F:/Python/Data1/Assignment 1/diemthi/csv'
            all_files = glob.glob(os.path.join(path, 'diemthi*.csv'))

            # return a generator object
            all_lines = (pd.read_csv(link) for link in all_files)
            # read into DataFrame

            found_csv_df = pd.concat(all_lines, ignore_index=True)

            # Read the existed csv file
            loguru.logger.info('Concating the received file to existed file')
            time.sleep(2)
            merge_df = pd.read_csv('csv/merged.csv')
            loguru.logger.info('Rows before concating: ' + str(merge_df.shape[0]))
            time.sleep(2)
            # take the number to rename later
            start_num_rows = merge_df.shape[0] + 1
            end_num_rows = found_csv_df.shape[0] + start_num_rows
            # concat the existed file to curent file
            merge_df = pd.concat([merge_df, found_csv_df], ignore_index=True)

            loguru.logger.info('Rows after concating: ' + str(merge_df.shape[0]))
            time.sleep(2)
            path_to_export_merged_csv = r'merged.csv'  # relative path in current directory
            merge_df.to_csv(path_to_export_merged_csv, index=False)

            # Move used-usedcsv to another file
            loguru.logger.info('Change the name for ease in managing')
            orginal = r'csv'
            loguru.logger.info('Original: ' + event.src_path)
            target = r'usedcsv'

            os.chdir(r"csv")

            new_name = 'diemthi_' + str(start_num_rows) + '-' + str(end_num_rows) + '.csv'
            os.rename('diemthi.csv', new_name)
            time.sleep(2)
            loguru.logger.info('Changed name to ' + new_name + ' successfully')

            # Transfering files

            loguru.logger.info('Start transferring to "usedcsv" file')

            os.chdir(r"F:/Python/Data1/Assignment 1/diemthi")

            time.sleep(1)
            if os.path.exists(target + '/' + new_name):
                os.remove(target + '/' + new_name)
                shutil.move(orginal + '/' + new_name, target)
            else:
                shutil.move(orginal + '/' + new_name, target)

            time.sleep(1)
            loguru.logger.info('Transfered successfully')

            time.sleep(2)
            clean(path_to_export_merged_csv)  # export a filtered csv in current directory
            loguru.logger.info('Filtered columns successfully')
            filter_df = pd.read_csv('filtered.csv')
            print(filter_df)
            time.sleep(4)
            # Push data to SQL and MongoDB
            loguru.logger.info('Push data to mongoDB and SQL server')

            path_to_filtered_csv = r'filtered.csv'
            import2sql(path_to_filtered_csv)
            time.sleep(2)
            import2mongoDB(path_to_filtered_csv)
            loguru.logger.info('Finished !')

if __name__ == '__main__':
    print('Watchdog is starting . . . ')

    w = Watcher()
    w.run()
