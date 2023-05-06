from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import hashlib
import secrets
from Crypto.Cipher import AES
import os

app = Flask(__name__)
app.secret_key = "mysecretkey"


@app.route("/")
def landing():
    return render_template("landing.html")


# privatekey = os.urandom(32)
# # Signup function


# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     msg = None
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         if username and password:
#             cipher = AES.new(privatekey, AES.MODE_EAX)

#             ciphertext, tag = cipher.encrypt_and_digest(password.encode('utf-8'))

#             # Get the nonce and update the cipher object
#             nonce = cipher.nonce
#             cipher = AES.new(privatekey, AES.MODE_EAX, nonce=nonce)
#             password_hashed = ciphertext.hex()
#             conn = sqlite3.connect("signup.db")
#             c = conn.cursor()
#             conn.execute('''CREATE TABLE IF NOT EXISTS personsdata
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   username TEXT NOT NULL,
#                   password TEXT NOT NULL,
#                   privatekey TEXT NOT NULL);''')
#             conn.execute("INSERT INTO personsdata (username, password, privatekey) VALUES (?, ?, ?)",
#                          (username, password_hashed, privatekey.hex()))
#             conn.commit()
#             conn.close()
#             decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
            

#             msg = "You have successfully signed up! Your private key is: {}".format(bytes.fromhex(privatekey.hex()))
#         else:
#             msg = "Please enter both username and password"
#     return render_template("signup.html", msg=msg)


# Signup function
@app.route("/signup", methods=["GET", "POST"])
def signup():
    msg = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            privatekey = os.urandom(32)
            conn = sqlite3.connect("signup.db")
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS personsdata
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL,
                  privatekey TEXT NOT NULL);''')
            c.execute("INSERT INTO personsdata (username, password, privatekey) VALUES (?, ?, ?)",
                      (username, password, privatekey.hex()))
            conn.commit()
            conn.close()
            msg = "You have successfully signed up!"
        else:
            msg = "Please enter both username and password"
    return render_template("signup.html", msg=msg)



# Login function
# Login function

# Login function
# Login function
# Login function
@app.route("/login", methods=["GET", "POST"])
def login():
    msg = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            conn = sqlite3.connect("signup.db")
            c = conn.cursor()
            c.execute("SELECT * FROM personsdata WHERE username = ? AND password = ?", (username, password))
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

    #         r = c.fetchone()
    #         conn.close()
    #         if r is not None:
    #             # retrieve the private key from the database
    #             privatekey = bytes.fromhex(r[3])
    #             # decrypt the password using the private key
    #             nonce = bytes.fromhex(r[4])
    #             ciphertext = bytes.fromhex(r[2])
    #             tag = bytes.fromhex(r[5])
            
    #             cipher = AES.new(privatekey, AES.MODE_EAX, nonce=nonce)
    #             plaintext = cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')
    #             if plaintext == password:
    #                 session["loggedin"] = True
    #                 session["username"] = username
    #                 return redirect(url_for("dashboard"))
    #             else:
    #                 msg = "Invalid password"
    #         else:
    #             msg = "Invalid username"
    #     else:
    #         msg = "Please enter both username and password"
    # return render_template("login.html", msg=msg)







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
        c.execute("SELECT privatekey FROM personsdata WHERE username = ?",
                  (session["username"],))
        privatekey = c.fetchone()[0]
        conn.close()
        return render_template("dashboard.html", username=session["username"], privatekey=privatekey)
    else:
        return redirect(url_for("login"))

# @app.route('/fill_details', methods=['GET', 'POST'])
# def fill_details():
#     if request.method == 'POST':
#         conn = sqlite3.connect('signup.db')
#         conn.execute('''CREATE TABLE IF NOT EXISTS user_details
#                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                          name TEXT NOT NULL,
#                          email TEXT NOT NULL,
#                          phone INTEGER NOT NULL,
#                          age INTEGER NOT NULL,

#                          monthlyexpense INTEGER NOT NULL);''')
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         age = request.form['age']

#         monthlyexpense = request.form['monthlyexpense']
#         conn.execute("INSERT INTO user_details (name, email, phone, age, salary, monthlyexpense) VALUES (?, ?, ?, ?, ?, ?)", (name, email, phone, age, monthlyexpense))
#         conn.commit()
#         conn.close()
#         return redirect('/dashboard')
#     return render_template('fill_details.html')


# @app.route('/fill_details', methods=['GET', 'POST'])
# def fill_details():
#     if request.method == 'POST':
#         conn = sqlite3.connect('signup.db')
#         conn.execute('''CREATE TABLE IF NOT EXISTS user_details
#                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                          name TEXT NOT NULL,
#                          email TEXT NOT NULL,
#                          phone INTEGER NOT NULL,
#                          age INTEGER NOT NULL,
#                          monthlyexpense INTEGER NOT NULL,
#                          retirementvalue INTEGER NOT NULL);''')
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         age = request.form['age']
#         monthlyexpense = request.form['monthlyexpense']
#         retirementvalue = int(monthlyexpense) * 12 * 25
#         conn.execute("INSERT INTO user_details (name, email, phone, age, monthlyexpense, retirementvalue) VALUES (?, ?, ?, ?, ?, ?)",
#                      (name, email, phone, age, monthlyexpense, retirementvalue))
#         conn.commit()
#         conn.close()
#         return redirect('/retirement/{}'.format(retirementvalue))
#     return render_template('fill_details.html')




#today''ssss 




# Fill details function
@app.route("/filldetails", methods=["GET", "POST"])
def filldetails():
    msg = None
    conn = sqlite3.connect("signup.db")
    c = conn.cursor()
    c.execute("SELECT privatekey FROM personsdata WHERE username = ?", (session["username"],))
    r = c.fetchone()
    if r:
        privatekey = bytes.fromhex(r[0])
    else:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        age = request.form["age"]
        monthlyexpense = request.form["monthlyexpense"]
        retirementvalue = int(monthlyexpense) * 12 * 25
        
        if name and email and phone and age and monthlyexpense and retirementvalue:
            # Initialize the cipher object with the private key and generate a nonce
            cipher = AES.new(privatekey, AES.MODE_EAX)
            nonce = cipher.nonce

            # Encrypt data using the cipher object
            email_ciphertext, email_tag = cipher.encrypt_and_digest(email.encode('utf-8'))
            phone_ciphertext, phone_tag = cipher.encrypt_and_digest(phone.encode('utf-8'))
            monthlyexpense_ciphertext, monthlyexpense_tag = cipher.encrypt_and_digest(monthlyexpense.encode('utf-8'))
            retirementvalue_ciphertext, retirementvalue_tag = cipher.encrypt_and_digest(str(retirementvalue).encode('utf-8'))

            # Convert ciphertext and tag to hexadecimal strings
            email_hashed = email_ciphertext.hex()
            phone_hashed = phone_ciphertext.hex()
            monthlyexpense_hashed = monthlyexpense_ciphertext.hex()
            retirementvalue_hashed = retirementvalue_ciphertext.hex()

            # Store encrypted data in the database
            c.execute('''CREATE TABLE IF NOT EXISTS user_details
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          email TEXT NOT NULL,
                          phone TEXT NOT NULL,
                          age TEXT NOT NULL,
                          monthlyexpense TEXT NOT NULL,
                          retirementvalue TEXT NOT NULL);''')
            c.execute("INSERT INTO user_details (name, email, phone, age, monthlyexpense, retirementvalue) VALUES (?, ?, ?, ?, ?, ?)",
                      (name, email_hashed, phone_hashed, age, monthlyexpense_hashed, retirementvalue_hashed))
            conn.commit()
            conn.close()
            msg = "Details added successfully!"
        else:
            msg = "Please fill all the fields"
    return render_template("filldetails.html", msg=msg)






@app.route('/retirement/<int:retirementvalue>')
def retirement(retirementvalue):
    return render_template('retirement.html', retirementvalue=retirementvalue)


@app.route('/asset_allocation')
def asset_allocation():
    return render_template(url_for('asset_allocation.html'))


if __name__ == "__main__":
    app.run(debug=True)
