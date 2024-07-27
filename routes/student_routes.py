from flask import Blueprint, request, jsonify
from models.student import Student

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/students', methods=['GET'])
def get_students():
    students = Student.get_all_students()
    return jsonify(students)

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.get_student_by_id(student_id)
    if student:
        return jsonify(student)
    else:
        return jsonify({'message': 'Student not found'}), 404

@student_bp.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name and email:
        Student.add_student(name, email)
        return jsonify({'message': 'Student added successfully'})
    else:
        return jsonify({'message': 'Invalid data'}), 400

@student_bp.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name and email:
        Student.update_student(student_id, name, email)
        return jsonify({'message': 'Student updated successfully'})
    else:
        return jsonify({'message': 'Invalid data'}), 400
