import os
from flask import Flask, render_template, request, redirect,flash,make_response,session, abort, url_for
from forms import signupForm,loginForm,ChangePasswordForm


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "freshield@123")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = signupForm()
    if form.validate_on_submit():
            flash("Signed up successfully!", "success")
            return redirect(url_for("home"))
    return render_template("signup.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        email = form.email.data
        pw = form.password.data
        if email == "sanjeevnayak8260@gmail.com" and pw == "123456":
            flash("Logged in successfully !!!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html", title="Login", form=form)

       

    return render_template("login.html",title = "Login",form=form)

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=False)

