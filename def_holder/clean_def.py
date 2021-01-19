import csv
import os

file = open(r"../usedcsv/diemthi.csv", encoding='utf-8', mode="r")

# Read first student
datas = file.read().split("\n")

#Removing the header and the empty element at the end of the list
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

    print('Len: '+str(len(i)))
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
