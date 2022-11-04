import flask
import sqlite3

app = flask.Flask(__name__)


def dict_factory(cursor, row):
    dict = {}
    for idx, col in enumerate(cursor.description):
        dict[col[0]] = row[idx]
    return dict



@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/login", methods = ["POST"])
def search():
    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()
    conn.row_factory = dict_factory

    try:
        account = flask.request.form["account"]
        password = flask.request.form["password"]
    except:
        return flask.render_template("loggedin.html",message = "missing argument")
    cursor.execute(f"SELECT * FROM ACCOUNT WHERE ACCOUNT = '{account}' AND PASSWORD = '{password}'")
    
    data = cursor.fetchall()
    if len(data) == 0:
        return flask.render_template("loggedin.html", message = "login failed")
    
    return flask.render_template("loggedin.html",message = f"login as {data[0][1]} | password : {data[0][2]}")
    
    




if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)