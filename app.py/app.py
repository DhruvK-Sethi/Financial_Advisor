from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import hashlib
import secrets

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def landing():
	return render_template("landing.html")


# Signup function
@app.route("/signup", methods=["GET", "POST"])
def signup():
    msg = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            privatekey = secrets.token_hex(16)
            password_hashed = hashlib.sha256(password.encode()).hexdigest()
            conn = sqlite3.connect("signup.db")
            c = conn.cursor()
            conn.execute('''CREATE TABLE IF NOT EXISTS personsdata
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL,
                  privatekey TEXT NOT NULL);''')
            conn.execute("INSERT INTO personsdata (username, password, privatekey) VALUES (?, ?, ?)", (username, password_hashed, privatekey))
            conn.commit()
            conn.close()
            msg = "You have successfully signed up! Your private key is: {}".format(privatekey)
        else:
            msg = "Please enter both username and password"
    return render_template("signup.html", msg=msg)


# Login function
@app.route("/login", methods=["GET", "POST"])
def login():
    msg = None
    if request.method == "POST":
        username = request.form.get("username")
        privatekey = request.form.get("privatekey")
        if username and privatekey:
            conn = sqlite3.connect("signup.db")
            c = conn.cursor()
            c.execute("SELECT * FROM personsdata WHERE username = ? AND privatekey = ?", (username, privatekey))
            r = c.fetchone()
            conn.close()
            if r:
                session["loggedin"] = True
                session["username"] = username
                return redirect(url_for("dashboard"))
            else:
                msg = "Invalid username or private key"
        else:
            msg = "Please enter both username and private key"
    return render_template("login.html", msg=msg)


@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("username", None)
    return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
	if "loggedin" in session:
		conn = sqlite3.connect("signup.db")
		c = conn.cursor()
		c.execute("SELECT privatekey FROM personsdata WHERE username = ?", (session["username"],))
		privatekey = c.fetchone()[0]
		conn.close()
		return render_template("dashboard.html", username=session["username"], privatekey=privatekey)
	else:
		return redirect(url_for("login"))
	
@app.route('/fill_details', methods=['GET', 'POST'])
def fill_details():
    if request.method == 'POST':
        conn = sqlite3.connect('signup.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS user_details
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL,
                         email TEXT NOT NULL,
                         phone INTEGER NOT NULL,
                         age INTEGER NOT NULL,
                         salary INTEGER NOT NULL,
                         monthlyexpend INTEGER NOT NULL);''')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        salary = request.form['salary']
        monthlyexpend = request.form['monthlyexpend']
        conn.execute("INSERT INTO user_details (name, email, phone, age, salary, monthlyexpend) VALUES (?, ?, ?, ?, ?, ?)", (name, email, phone, age, salary, monthlyexpend))
        conn.commit()
        conn.close()
        return redirect('/dashboard')
    return render_template('fill_details.html')

	




if __name__ == "__main__":
    app.run(debug=True)


	





