from user_controller import appfrom flask import request, render_template, flash, redirectfrom constants import ADMINSimport requestsimport json# Controller for student enrollment@app.route("/<user_id>/student/enrollments", methods=["GET"])def student_enrollment(user_id):    """Controller Function for handling student enrollment"""    # Hitting API to get enrollments data    response = requests.get(f"http://127.0.0.1:5001/api/enrollments/student/{user_id}")    data = {"user_id": user_id}    info = response.json()    # If success then getting course name for the corresponding course id    if response.status_code == 200:        # Rendering template for student's enrollment        return render_template("student_enrollment.html", data=data, enrollments=info["data"],                               admin=False, page_title="Student's Enrollments")# Controller for adding enrollment@app.route('/<user_id>/add_enrollment', methods=["GET", "POST"])def add_enrollment(user_id):    """Controller Function for handling add enrollment functionality"""    # Getting User's name    data = {"user_id": user_id}    req = requests.get(f"http://127.0.0.1:5001/api/get_user_name/{user_id}")    user_name = ""    if req.status_code == 200:        user_name = req.json()["data"]["name"]    # Getting Unenrolled courses for showing as options    data1 = json.dumps({"user_id": user_id, "enrollment_type": "unenrolled"})    headers = {"Content-Type": "application/json"}    # Hitting API for getting unenrolled courses    req2 = requests.post("http://127.0.0.1:5001/api/courses/student", data=data1, headers=headers)    courses = []    if req2.status_code == 200:        courses = req2.json()["data"]    # If request is POST    if request.method == "POST":        course_id = int(request.form["course_name"])        marks = int(request.form["marks"])        term = request.form["term"]        year = int(request.form["year"])        study_hour = int(request.form["study_hour"])        # Preparing data as json for hitting API for adding enrollment        data2 = json.dumps({"course_id": course_id, "user_id": int(user_id), "marks": marks, "term": term,                            "year": year, "study_hours": study_hour})        headers = {"Content-Type": "application/json"}        req3 = requests.post("http://127.0.0.1:5001/api/enrollments", data=data2, headers=headers)        msg = req3.json()["message"]        flash(msg)        # If success then reverting to student's enrollment page        if req3.status_code == 201:            return redirect(f"/{user_id}/student/enrollments")        # If failure, then returning to add enrollment form with appropriate message        return render_template("add_enrollment.html", data=data, admin=False, page_title="Add Enrollment",                               user_name=user_name, courses=courses)    # rendering template upon GET request    data = {"user_id": user_id}    return render_template("add_enrollment.html", data=data, admin=False, page_title="Add Enrollment",                           user_name=user_name, courses=courses)# Controller for deleting enrollment@app.route("/<int:user_id>/delete_enrollment/<int:enroll_id>", methods=["GET"])def delete_enrollment(user_id, enroll_id):    """Controller Function for handling delete enrollment functionality"""    # Hitting API for deleting enrollment data    req = requests.delete(f"http://127.0.0.1:5001/api/enrollments/{enroll_id}")    msg = req.json()["message"]    flash(msg)    if user_id not in ADMINS:        # Reverting to student enrollments again        return redirect(f"/{user_id}/student/enrollments")    else:        return redirect(f"/{user_id}/enrollments/admin")# Controller for getting all enrollments@app.route("/<user_id>/enrollments/admin", methods=["GET"])def admin_enrollments(user_id):    """Controller Function for getting all enrollments data"""    # hitting API to get data    req = requests.get("http://127.0.0.1:5001/api/enrollments/admin")    data = {"user_id": user_id}    # If response is success then rendering page with data    if req.status_code == 200:        info = req.json()["data"]        return render_template("all_enrollments.html", data=data, enrollments=info, admin=True,                               page_title="All Enrollments")    return req.status_code