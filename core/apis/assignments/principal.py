from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.principals import Principal
from core.models.students import Student
from core.models.teachers import Teacher  # Assuming you have a Teacher model
from .schema import AssignmentSchema, TeacherSchema  # Assuming you have schemas for Assignment and Teacher
from core.models.users import User
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_submitted_assignments(p):
    """List all submitted and graded assignments"""
    # List all submitted and graded assignments
    principal_assignments = Assignment.query.filter(Assignment.state.in_(['SUBMITTED', 'GRADED'])).all()

    return APIResponse.respond(data=AssignmentSchema().dump(principal_assignments, many=True))


@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """List all the teachers"""
    teachers = Teacher.query.all()
    teachers_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)


# @principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
# @decorators.accept_payload
# @decorators.authenticate_principal
# def grade_assignment(p, incoming_payload):
#     """Grade or re-grade an assignment"""
#     assignment_id = incoming_payload.get('assignment_id')
#     grade = incoming_payload.get('grade')

#     if not assignment_id or not grade:
#         return APIResponse.respond(message="Assignment ID and grade are required.", status=400)

#     assignment = Assignment.query.get(assignment_id)
#     if not assignment:
#         return APIResponse.respond(message="Assignment not found.", status=404)

#     assignment.grade = grade
#     db.session.commit()

#     graded_assignment_dump = AssignmentSchema().dump(assignment)
#     return APIResponse.respond(data=graded_assignment_dump)
