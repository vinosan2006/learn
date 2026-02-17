from flask import Blueprint, render_template, session, redirect, url_for
from app.models.course_model import Course

course_bp = Blueprint("course", __name__)

@course_bp.route("/courses")
def courses():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    course = Course("Web Development")
    return render_template("courses.html", course=course)
