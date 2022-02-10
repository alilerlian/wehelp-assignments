from turtle import clear
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='12345678',
    database='WEEK6_database'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE WEEK6_database")

# 創建表格
# mycursor.execute(
#     "CREATE TABLE members (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)")

# 顯示資料庫中的表
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# 插入資料
# insertMember = "INSERT INTO members (name, username,password) VALUES (%s, %s, %s)"
# memberData = ("AAA", "AAA", "aaa")
# mycursor.execute(insertMember, memberData)
# mydb.commit()

# 印出表中所有資料
# mycursor.execute("SELECT * FROM members")
# member = mycursor.fetchall()
# for x in member:
#     print(x)

# 傳回受到前一個陳述式所影響的資料列數
# print(mycursor.rowcount, "record inserted.")


# mycursor.execute("SELECT username,password FROM members")
# memberUsername = mycursor.fetchall()

# print(memberUsername)

# mycursor.execute("SELECT username FROM members")
# memberUsername = mycursor.fetchall()

# username = 'BBB'

# if (username,) in memberUsername:
#     print(memberUsername)

# mycursor.execute("SELECT username,password FROM members")
# memberData = mycursor.fetchall()
# if ('BBB', 'bbb') in memberData:
#     print(memberData)

mycursor.execute("SELECT id,username FROM members")
memberID = mycursor.fetchall()
print(memberID[0])
print(memberID[0][0])
member = "BBB"
memberID = dict(memberID)
print(memberID)
for id in memberID.keys():
    if memberID[id] == member:
        print(id)
