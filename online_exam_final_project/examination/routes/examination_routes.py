from flask import Blueprint,render_template
from controllers.examination_controller import ExaminationController

examination_routes = Blueprint('examination_routes', __name__)
controller = ExaminationController()

# Examination routes
@examination_routes.route("/examination/<int:exam_id>", methods=["GET"])
def view_examination(exam_id):
    # Call the controller function to get the examination details
    examination = controller.get_examination(exam_id)
    print("\n,\n", examination)
    # Check if there is an error in the examination data
    if examination.get("error") is not None:
        return render_template("view_examination.html", error=examination.get("error"))
        
    # Render the examination details if no error exists
    return render_template("view_examination.html", examination=[examination],error=None)



@examination_routes.route("/examination", methods=["GET"])
def get_all_examinations():
    examinations = controller.get_all_examinations()
    
    # Check for error in the returned data
    if isinstance(examinations, dict) and examinations.get("error"):
        return render_template("view_all_examinations.html", error=examinations.get("error"))
    
    # Pass the examinations list to the template
    return render_template("view_all_examinations.html", examinations=examinations)




examination_routes.route("/examination", methods=["POST"])(controller.create_examination)
examination_routes.route("/examination/<int:exam_id>", methods=["PUT"])(controller.update_examination)
examination_routes.route("/examination/<int:exam_id>", methods=["DELETE"])(controller.delete_examination)



@examination_routes.route("/student_portal")
def student_portal():
    return render_template('student_portal.html')



@examination_routes.route("/admin_portal")
def admin_portal():
    return render_template('admin_portal.html')



# UserResponse routes
examination_routes.route("/user_response/<int:response_id>", methods=["GET"])(controller.get_user_response)
examination_routes.route("/user_response", methods=["POST"])(controller.create_user_response)
examination_routes.route("/user_response/<int:response_id>", methods=["PUT"])(controller.update_user_response)
examination_routes.route("/user_response/<int:response_id>", methods=["DELETE"])(controller.delete_user_response)
