from flask import Blueprint, render_template, request, redirect, url_for, session

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return render_template("index.html", user=session["user"])

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:
            session["user"] = email
            return redirect(url_for("auth.home"))

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("auth.login"))

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            session["user"] = email
            return redirect(url_for("auth.home"))
            
    return render_template("register.html")
