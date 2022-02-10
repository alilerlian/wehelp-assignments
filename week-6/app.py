from flask import Flask, request, render_template, redirect, session
import mysql.connector
app = Flask(__name__)  # 建立Application

mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='12345678',
    database='WEEK6_database'
)

mycursor = mydb.cursor()
app.secret_key = "Alice"  # 設定session密鑰 密鑰可以為任何字串


@app.route("/")  # 首頁
def index():
    return render_template("homepage.html")


@app.route("/signup", methods=["POST"])  # 註冊帳號密碼
def singup():
    mycursor.execute("SELECT username FROM members")
    memberUsername = mycursor.fetchall()

    insertMember = "INSERT INTO members (name, username,password) VALUES (%s, %s, %s)"
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    memberData = (name, username, password)

    if (username,) in memberUsername:
        return redirect("/error?message=帳號已經被註冊")  # 註冊失敗顯示錯誤訊息
    else:
        mycursor.execute(insertMember, memberData)
        mydb.commit()
        return redirect("/")  # 註冊成功後跳回首頁


@app.route("/signin", methods=["POST"])  # 登入驗證功能
def singin():
    mycursor.execute("SELECT username,password FROM members")
    memberData = mycursor.fetchall()

    username = request.form["username"]
    password = request.form["password"]

    accountSituation = (username, password) in memberData
    session["accountSituation"] = accountSituation  # session["欄位名稱"]=資料 儲存帳號狀態

    if accountSituation == True:
        mycursor.execute("SELECT username,name FROM members")
        memberName = dict(mycursor.fetchall())  # 取得名字 儲存名字
        name = memberName[username]
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
        return render_template("member.html", name=name)
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


app.run(port=3000)
