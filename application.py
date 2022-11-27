import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, url_for
# from flask_session import session


conn = sqlite3.connect("marks",check_same_thread=False)
cur = conn.cursor()
app = Flask(__name__)
@app.route('/login')
@app.route('/login.html')
def login1():
	return render_template("login.html")

@app.route('/teacher')
@app.route('/teacher.html')
def teacher1():
	return render_template("display.html")

@app.route('/display')
@app.route('/display.html')
def display1():
	return render_template("display.html")

@app.route('/')
@app.route('/index.html')
def index1():
	return render_template("index.html")

@app.route("/", methods = ["GET","POST"])
def index():
    flag=0
    if request.method == "GET" :
        return render_template("index.html")
        print("hiii")
    else:
        print("hello")
        usn1=request.form.get("usn1")
        name1=request.form.get("name1")
        sem1=request.form.get("sem1")
        sub1=request.form.get("sub1")
        print(usn1,name1,sem1,sub1)
        cur.execute("select ia1,ia2,ia3 from marks where usn=? and sem=? and subname=?",(usn1,sem1,sub1))
        rows2=cur.fetchall()
        conn.commit()
        print(rows2[0][0])
        return render_template("display.html", usn1=usn1,name1=name1,sem1=sem1,sub1=sub1,ia1=rows2[0][0],ia2=rows2[0][1],ia3=rows2[0][2])

@app.route("/display", methods = ["GET","POST"])
def display():
        return render_template("display.html")


@app.route("/login", methods = ["GET","POST"])
def login():
    flag1=0
    if request.method == "GET" :
        return render_template("login.html")
    else :
        email=request.form.get("email")
        pwd=request.form.get("pwd")
        #print("Hllo")
	#print(email,pwd)
        if email=="isebit@gmail.com" and pwd== "ise123":
            return render_template("teacher.html")
        else:
            flag1=1
            return render_template("login.html",flag1=flag1)

@app.route("/teacher", methods = ["GET","POST"])
def teacher():
    if request.method == "GET" :
	    return render_template("teacher.html")
    else:
        #rf=request.form
        #print(rf)
        usn=request.form.get("usn")
        sem=request.form.get("selectsem")
        sub=request.form.get("selectsub")
        ia1=request.form.get("ia1")
        ia2=request.form.get("ia2")
        ia3=request.form.get("ia3")
        #seme,subb=request.data()
        param=(usn,sub,sem,ia1,ia2,ia3)
        cur.execute("insert into marks (usn,subname,sem,ia1,ia2,ia3) values(?,?,?,?,?,?)", param)
        conn.commit()
        print(usn,ia1,ia2,ia3,sem,sub)
        return render_template("teacher.html")
        

# @app.route('/get_sub/<semes>')
# def selectsem(semes):
#     ret = ''
#     print("hhlo")
#     #seme=request.form.get("selectsem")
#     cur.execute("select * from semester where sem=?",(semes))
#     rows=cur.fetchall() 
#     conn.commit()
#     print(rows)	
#     #ret += '<option value="%s">"%s"</option>'%(entry,entry)
#     #return ret
@app.route('/selectsem', methods=['GET'])
def selectsem():
    ret = ''
    print('hello')
    seme=request.args.get('semes')
    print(seme)
    cur.execute("select * from semester where sem=?",(seme))
    rows=cur.fetchall()
    conn.commit()
    print(rows)
    for entry in rows[0]:
         ret += '<option value=%s>%s</option>'%(entry,entry)
    print(ret)
    ret='<select name="selectsem" class="orderby" id="selectsem">'+ret+'</select>'
    return ret

@app.route('/sem1', methods=['GET'])
def sem1():
    ret1 = ''
    #print('hello')
    seme1=request.args.get('semes1')
    #print(seme)
    cur.execute("select * from semester where sem=?",(seme1))
    rows1=cur.fetchall()
    conn.commit()
    print(rows1)
    for entry1 in rows1[0]:
         ret1 += '<option value=%s>%s</option>'%(entry1,entry1)
    print(ret1)
    ret1='<select name="sem1" class="orderby" id="sem1">'+ret1+'</select>'
    return ret1

if __name__ == '__main__' :
    app.run(debug=True)
