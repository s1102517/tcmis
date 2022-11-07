import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>袁家偉 Python+flask+Vercel網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=袁家偉>傳送使用者暱稱</a><br>"
    homepage += "<a href=/me>袁家偉介網頁</a><br>"
    homepage += "<br><a href=/read>讀取Firestore資料</a><br>"
    return homepage

@app.route("/read")
def read():
    Result = ""     
    collection_ref = db.collection("111")    
    docs = collection_ref.order_by("mail", direction=firestore.Query.DESCENDING).get()    
    for doc in docs:         
            dict = doc.to_dict()
    if cond in dict["Course"]:

        #print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
        result += dict["Leacture"] + "老師開的" + dict["Course"] + "課程,每週"
        result += dict["Time"] + "於" + dict["Room"] + "上課\n"
        print(result)

        #Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
        
    return Result

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/me")
def me():
    return render_template("aboutme.html")

#if __name__ == "__main__":
#    app.run()
