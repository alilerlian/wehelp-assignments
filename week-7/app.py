from flask import Flask, request, render_template, redirect, session, json
import mysql.connector
app = Flask(__name__)  # 建立Application

mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='12345678',
    database='WEEK7_database'
)

mycursor = mydb.cursor()
app.secret_key = "Alice"  # 設定session密鑰 密鑰可以為任何字串


@app.route("/")  # 首頁
def index():
    return render_template("homepage.html")


@app.route("/signup", methods=["POST"])  # 註冊帳號密碼
def singup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    checkMember = "SELECT username FROM members WHERE username COLLATE utf8mb4_0900_as_cs =%s"
    # select 區分大小寫
    userUsername = (username,)
    mycursor.execute(checkMember, userUsername)
    check = mycursor.fetchall() == [userUsername]

    insertMember = "INSERT INTO members (name, username,password) VALUES (%s, %s, %s)"
    memberData = (name, username, password)

    if check == False:
        mycursor.execute(insertMember, memberData)
        mydb.commit()
        return redirect("/")  # 註冊成功後跳回首頁
    else:
        return redirect("/error?message=帳號已經被註冊")  # 註冊失敗顯示錯誤訊息


@app.route("/signin", methods=["POST"])  # 登入驗證功能
def singin():
    username = request.form["username"]
    password = request.form["password"]
    selectUser = "SELECT username,password FROM members WHERE username COLLATE utf8mb4_0900_as_cs =%s AND password COLLATE utf8mb4_0900_as_cs =%s"
    User = (username, password)
    mycursor.execute(selectUser, User)
    selectResult = mycursor.fetchall()

    accountSituation = selectResult == [User]
    session["accountSituation"] = accountSituation  # session["欄位名稱"]=資料 儲存帳號狀態

    if accountSituation == True:
        selectName = "SELECT name FROM members WHERE username COLLATE utf8mb4_0900_as_cs =%s"
        username = (username,)
        mycursor.execute(selectName, username)
        name = mycursor.fetchall()  # 取得名字 儲存名字
        session["name"] = name
        return redirect("/member")
    elif accountSituation == False and (len(username) != 0 and len(password) != 0):
        return redirect("/error?message=帳號密碼錯誤")
    elif len(username) == 0 or len(password) == 0:
        return redirect("/error?message=請輸入帳號密碼")


@app.route("/member")  # 登入成功頁面
def member():
    accountSituation = session["accountSituation"]  # 取得 資料=session["欄位名稱"]
    name = session["name"]  # 取得儲存的名字

    if accountSituation == True:
        return render_template("member.html", name=name[0][0])
    else:
        return redirect("/")  # 非登入狀態跳回首頁


@app.route("/error")  # 失敗頁面
def error():
    message = request.args.get("message", "")
    return render_template("error.html", message=message)


@app.route("/signout")  # 登出功能
def signout():
    session["accountSituation"] = False
    session["passwordSituation"] = False
    return redirect("/")


@app.route("/api/members")  # 註冊帳號密碼
def getMember():
    getMember = "SELECT id,name,username FROM members WHERE username COLLATE utf8mb4_0900_as_cs =%s"
    username = request.args.get("username")
    userUsername = (username,)
    mycursor.execute(getMember, userUsername)
    userData = mycursor.fetchall()
    check = userData == []

    Data = {}

    if check == True:
        Data["data"] = None
        return json.dumps(Data)
    else:
        member = {"id": userData[0][0], "name": userData[0]
                  [1], "username": userData[0][2]}
        Data["data"] = member
        return json.dumps(Data)


app.run(port=3000)
