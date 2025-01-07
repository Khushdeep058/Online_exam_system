from flask import Blueprint,request
from controller.eval_controller import EvaluationController


eval_routes = Blueprint('eval_routes', __name__)
controller = EvaluationController()


#route to get evaluation by evaluation_id
@eval_routes.route("/evaluation/<int:evaluation_id>",methods=["GET"])
def get_eval(evaluation_id):
    return controller.get_eval(evaluation_id)

#route to create a new evaluation
@eval_routes.route("/evaluation", methods=["POST"])
def create_eval():
    evaluation_data=request.json
    return controller.create_eval(evaluation_data)

#route to update the evaluation by evaluation_id
@eval_routes.route("/evaluations/<int:evaluation_id>", methods=["PUT"])
def update_evaluation(evaluation_id):
    update_data = request.json
    return controller.update_evaluation(evaluation_id, update_data)


#route to delete the evaluation by evaluation_id
@eval_routes.route("/evaluations/<int:evaluation_id>", methods=["DELETE"])
def delete_evaluation(evaluation_id):
    return controller.delete_evaluation(evaluation_id)





