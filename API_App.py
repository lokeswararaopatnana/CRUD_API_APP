import json
from flask import Flask,jsonify
from EmployeeDB import DBdetails

app = Flask(__name__)
db = DBdetails()

@app.route("/")
def welcome():
    return "Welcome to Employee details Application...!"

@app.route("/employee/<eid>/<ename>/<desg>/<did>/<dname>/<award>/<salary>/<skills>",methods=['POST'])
def create_employee(eid,ename,desg,did,dname,award,salary,skills):
    db.insert_employee(eid,ename,desg,did,dname,award,salary,skills)
    data = {
        "eid":eid,
        "ename":ename,
        "desg":desg,
        "did":did,
        "dname":dname,
        "award":award,
        "salary":salary
    }
    return {"data":data,"status":"Success!","message":"Employee Created Successfully!"}

@app.route("/employees",methods = ['GET'])
def show_employees():
    res = db.fetch_all_employees()
    return res

@app.route("/employee/<eid>",methods = ['GET'])
def show_one_employee(eid):
    data = db.fetch_one_employee(eid)
    if data:
        return jsonify(data)
    else:
        data = {
            "data":"data not found!",
            "status":"Status Error!"
        }
        return jsonify(data)


@app.route("/employee/<EmployeeId>",methods = ['DELETE'])
def delete_employee(EmployeeId):
    data = db.delete_employee(EmployeeId)
    if data:
        data = {
            "status":"Error!",
            "message":"No EmployeeId in data!"
        }
        return data
    else:
        data = {
            "data":"data deleted successfully!",
            "status":"success!"
        }
        return data

@app.route("/employee/<EmployeeId>/<newName>/<newDesg>/<newDid>/<newDname>/<newAwards>/<newSalary>/<newSkills>",methods = ['PUT'])
def update_employee(EmployeeId,newName,newDesg,newDid,newDname,newAwards,newSalary,newSkills):
    data = db.update_employee(EmployeeId,newName,newDesg,newDid,newDname,newAwards,newSalary,newSkills)
    if data:
        return jsonify(data)
    else:
        data = {
            "status":"Success!",
            "message":"Employee Updated Sucessfully!"
        }
    return data


@app.route("/employees/<did>",methods = ['GET'])
def show_one_departmentname(did):
    data = db.fetch_departmentname(did)
    if data:
        return jsonify(data)
    else:
        data = {
            "data":"data not found please enter correct departmentname!",
            "status":"Error!"
        }
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)