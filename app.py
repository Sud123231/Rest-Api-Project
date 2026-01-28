from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///api_database.sqlite3"
db=SQLAlchemy(app)
api = Api(app)

class Course(db.Model):
    __tablename__="Course"
    course_id=db.Column(db.Integer,primary_key=True)
    course_name=db.Column(db.String,nullable=False)
    course_code=db.Column(db.String,unique=True,nullable=False)
    course_description=db.Column(db.String)

class Student(db.Model):
    __tablename__ ="Student"
    student_id=db.Column(db.Integer,primary_key=True)
    roll_number=db.Column(db.String,unique=True,nullable=False)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String)

class Enrollment(db.Model):
    enrollment_id=db.Column(db.Integer,primary_key=True)
    student_id=db.Column(db.Integer,db.ForeignKey("Student.student_id"),nullable=False)
    course_id=db.Column(db.Integer,db.ForeignKey("Course.course_id"),nullable=False)


with app.app_context():
    db.create_all()
    
class course(Resource):
    def get(self,course_id):
        course=db.session.query(Course).filter_by(course_id=course_id).first()
        if course:
            return {"course_id":course.course_id,
                    "course_name":course.course_name,
                    "course_code":course.course_code,
                    "course_description":course.course_description
                    },200
        else:
            return "course not found",404
    
    def put(self,course_id):
       data=request.get_json(silent=True)
       if data is None: 
           data=[]
       required_fields={"course_name":0, "course_code":0, "course_description":0}
       missing=[f for f in required_fields if f not in data]
       if missing:
           return {"error_code":"string", "error_message":"string"},400
       course=db.session.query(Course).filter_by(course_id=course_id).first()
       if course:
           course.course_name=data['course_name']
           course.course_code=data['course_code']
           course.course_description=data['course_description']
           db.session.commit()
           course=db.session.query(Course).filter_by(course_id=course_id).first()
           return {"course_id":course.course_id,
                           "course_name":course.course_name,
                           "course_code":course.course_code,
                           "course_description":course.course_description
                        },200
       else:
           return "course not found",404
       
    def delete(self,course_id):           
          course=db.session.query(Course).filter_by(course_id=course_id).first()
          if course:
              db.session.delete(course)
              db.session.commit()
              return "Successfully Deleted",200
          else:
              return "Course not found",404  

    def post(self):
        data=request.get_json(silent=True)
        if data is None: 
           data=[]
        required_fields={"course_name":0, "course_code":0, "course_description":0}
        missing=[f for f in required_fields if f not in data]
        if missing:
           return {"error_code":"string", "error_message":"string"},400
        course=db.session.query(Course).filter_by(course_code=data['course_code']).first()
        if course:
            return "course_code already exist",409
        course=Course(course_name=data['course_name'],course_code=data['course_code'],course_description=data['course_description'])
        db.session.add(course)
        db.session.commit()
        return {"course_id":course.course_id,
                "course_name":course.course_name,
                "course_code":course.course_code,
                "course_description":course.course_description
                },201   

class student(Resource):
    def get(self,student_id):
        student=db.session.query(Student).filter_by(student_id=student_id).first()
        if student:
            return {"student_id":student.student_id,
                    "first_name":student.first_name,
                    "last_name":student.first_name,
                    "roll_number":student.roll_number
                    },200
        else:
            return "student not found",404

    def post(self):
        data=request.get_json(silent=True)
        if data is None: 
           data=[]
        required_fields={"first_name":0, "last_name":0, "roll_number":0}
        missing=[f for f in required_fields if f not in data]
        if missing:
           return {"error_code":"string", "error_message":"string"},400
        student=db.session.query(Student).filter_by(roll_number=data["roll_number"]).first()
        if student:
            return "Student already exist",409
        student=Student(first_name=data['first_name'],last_name=data['last_name'],roll_number=data['roll_number'])
        db.session.add(student)
        db.session.commit()
        return {"student_id":student.student_id,
                "first_name":student.first_name,
                "last_name":student.last_name,
                "roll_number":student.roll_number
                },201 
    

    def put(self,student_id):
       data=request.get_json(silent=True)
       if data is None: 
           data=[]
       required_fields={"first_name":0, "last_name":0, "roll_number":0}
       missing=[f for f in required_fields if f not in data]
       if missing:
           return {"error_code":"string", "error_message":"string"},400
       student=db.session.query(Student).filter_by(student_id=student_id).first()
       if student:
           student.first_name=data['first_name']
           course.last_name=data['last_name']
           course.roll_number=data['roll_number']
           db.session.commit()
           student=db.session.query(Student).filter_by(roll_number=data["roll_number"]).first()
           return {"student_id":student.student_id,
                "first_name":student.first_name,
                "last_name":student.last_name,
                "roll_number":student.roll_number
                },201
       else:
           return "Student not found",404  

    def delete(self,student_id):           
          student=db.session.query(Student).filter_by(student_id=student_id).first()
          if student:
              db.session.delete(student)
              db.session.commit()
              return "Successfully Deleted",200
          else:
              return "Student not found",404   

class enrollment(Resource):
    def get(self,student_id):
        student=db.session.query(Student).filter_by(student_id=student_id).one_or_none()
        if student is None:
            return {"error_code":"string", "error_message":"string"},400

        enrollments=db.session.query(Enrollment).filter_by(student_id=student_id).all()
        if enrollments==[]:
            return "student is not enrolled in any course",404
        result=[]
        for obj in enrollments:
            format_obj={
                "enrollment_id":obj.enrollment_id,
                "student_id":obj.student_id,
                "course_id":obj.course_id
            }  
            result.append(format_obj)
        
        return jsonify(result),201  


    def post(self,student_id):
        data=request.get_json(silent=True)
        if data is None: 
           data=[]
        required_fields={"course_id":0}
        missing=[f for f in required_fields if f not in data]
        if missing:
           return {"error_code":"string", "error_message":"string"},400
        student=db.session.query(Student).filter_by(student_id=student_id).one_or_none()
        if student is None:
            return "Student not found",404 
        enrollment=Enrollment(student_id=student_id,course_id=data["course_id"])
        db.session.add(enrollment)
        db.session.commit()
        return {"enrollment_id":enrollment.enrollment_id,
                "student_id":enrollment.student_id,
                "course_id":enrollment.course_id,
                },201   
        
    def delete(self,student_id,course_id):           
          student=db.session.query(Student).filter_by(student_id=student_id).one_or_none()
          course=db.session.query(Course).filter_by(course_id=course_id).one_or_none()
          if  student is None or course is None:
              return "Invalid Student Id or Course Id",400
          enrollment=db.session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).one_or_none()
          if enrollment is not None:
              db.session.delete(enrollment)
              db.session.commit()
              return "successfully deleted",200
          else:
              return "Enrollment for the student not found",404     
api.add_resource(course,"/api/course/<int:course_id>", "/api/course") 
api.add_resource(student, "/api/student/<int:student_id>", "/api/student") 
api.add_resource(enrollment, "/api/student/<int:student_id>/course/<int:course_id>", "/api/student/<int:student_id>/course")

if __name__=='__main__':
    app.run(debug=True)     