from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def landing():
	return render_template("landing.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
	msg = None
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		if username and password:
			conn = sqlite3.connect("signup.db")
			c = conn.cursor()
			c.execute("INSERT INTO person (username, password) VALUES (?, ?)", (username, password))
			conn.commit()
			conn.close()
			msg = "You have successfully signed up!"
		else:
			msg = "Please enter both username and password"
	return render_template("signup.html", msg=msg)

@app.route("/login", methods=["GET", "POST"])
def login():
	msg = None
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		if username and password:
			conn = sqlite3.connect("signup.db")
			c = conn.cursor()
			c.execute("SELECT * FROM person WHERE username = ? AND password = ?", (username, password))
			r = c.fetchone()
			conn.close()
			if r:
				session["loggedin"] = True
				session["username"] = username
				return redirect(url_for("dashboard"))
			else:
				msg = "Invalid username or password"
		else:
			msg = "Please enter both username and password"
	return render_template("login.html", msg=msg)
@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("username", None)
    return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
	if "loggedin" in session:
		return render_template("dashboard.html", username=session["username"])
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