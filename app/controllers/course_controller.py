from flask import Blueprint, render_template, session, redirect, url_for, abort, request
from app.models.course_model import CourseFactory
from prometheus_client import Counter

ENROLLMENT_COUNTS = Counter('enrollment_counts_total', 'Total Course Enrollments')

course_bp = Blueprint("course", __name__)

# Using the GoF Factory Pattern to instantiate polymorphic Course objects
courses_data = [
    CourseFactory.create_course(
        "Programming", 1, "Python", 
        "Learn Python basics such as variables, loops, functions and mini projects.", 
        "Beginner", "6 Weeks"
    ),
    CourseFactory.create_course(
        "Data Science", 2, "Machine Learning", 
        "Learn regression, classification, datasets and build ML projects.", 
        "Intermediate", "8 Weeks"
    ),
    CourseFactory.create_course(
        "Web Development", 3, "Web Development", 
        "Learn HTML, CSS, Flask and create complete websites.", 
        "Beginner", "5 Weeks"
    )
]

@course_bp.route("/courses")
def courses():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    q = request.args.get("q", "").lower()
    if q:
        filtered_courses = [course for course in courses_data if q in course.title.lower() or q in course.description.lower()]
    else:
        filtered_courses = courses_data

    return render_template("courses.html", courses=filtered_courses)


@course_bp.route("/course/<int:course_id>")
def course_detail(course_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))

    selected_course = next(
        (course for course in courses_data if course.id == course_id),
        None
    )

    if selected_course is None:
        abort(404)

    enrolled = session.get("enrolled", [])
    return render_template("course_detail.html", course=selected_course, enrolled=enrolled)
@course_bp.route("/enroll/<int:course_id>", methods=["POST"])
def enroll(course_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    enrolled = session.get("enrolled", [])
    if course_id not in enrolled:
        enrolled.append(course_id)
        session["enrolled"] = enrolled
        session.modified = True
        ENROLLMENT_COUNTS.inc()
        
    return redirect(url_for("course.enrolled"))

@course_bp.route("/enrolled")
def enrolled():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    enrolled_ids = session.get("enrolled", [])
    enrolled_list = [c for c in courses_data if c.id in enrolled_ids]
    return render_template("enrolled.html", courses=enrolled_list)

@course_bp.route("/jobs")
def jobs():
    if "user" not in session:
        return redirect(url_for("auth.login"))
        
    job_list = [
        {"title": "Junior Web Developer", "desc": "Entry-level position focusing on building basic static websites.", "tags": ["HTML", "CSS", "JS"]},
        {"title": "Frontend Developer", "desc": "Focus on creating responsive and interactive user interfaces.", "tags": ["React", "Vue", "Tailwind"]},
        {"title": "Full Stack Developer", "desc": "Manage both frontend and backend architectures.", "tags": ["Python", "Flask", "React", "NodeJS"]}
    ]
    return render_template("jobs.html", jobs=job_list)

@course_bp.route("/assessment")
def assessment():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return render_template("assessment.html")