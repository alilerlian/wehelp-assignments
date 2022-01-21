from flask import Flask  # 載入Flask
from flask import request  # 載入request物件
from flask import render_template  # 載入render_template 函式
from flask import redirect  # 載入redirect函式
from flask import session  # 載入session
app = Flask(__name__)  # 建立Application

app.secret_key = "Alice"  # 設定session密鑰 密鑰可以為任何字串


@app.route("/")  # 首頁
def index():
    return render_template("homepage.html")


@app.route("/signin", methods=["POST"])  # 登入驗證功能
def singin():
    accountList = {'account': 'test', 'password': 'test'}
    account = request.form["account"]
    password = request.form["password"]
    
    accountSituation = account == accountList["account"] and password == accountList["password"]
    session["accountSituation"] = accountSituation # session["欄位名稱"]=資料 儲存帳號狀態

    if accountSituation == True: 
        return redirect("/member")
    elif len(account) != 0 or len(password) != 0:
        if account != accountList["account"] or password != accountList["password"]:
            return redirect("/error?message=帳號密碼錯誤")
    elif len(account) == 0 and len(password) == 0:
        return redirect("/error?message=請輸入帳號密碼")
    # return "登入驗證"


@app.route("/member")  # 登入成功頁面
def member():
    accountSituation = session["accountSituation"]  # 取得 資料=session["欄位名稱"]
    if accountSituation == True:
        return render_template("member.html")
    else:
        return redirect("/")  # 非登入狀態跳回首頁
    # return "登入成功"


@app.route("/error")  # 失敗頁面
def error():
    message = request.args.get("message", "")
    return render_template("error.html", message=message)
    # return "登入失敗"


@app.route("/signout")  # 登出功能
def signout():
    session["accountSituation"] = False
    session["passwordSituation"] = False
    return redirect("/")
    # return "登出"


app.run(port=3000)
