import mysql.connector as connector

class DBdetails:
    def __init__(self):
        self.con = connector.connect(host = 'localhost',user = 'root',password = '123456',database = 'employees')
        query = "create table if not exists employeedata(EmployeeId int primary key,EmployeeName varchar(100),Designation varchar(150),DepartmentId varchar(15),DepartmentName varchar(150),Awards varchar(10),Salary varchar(20),Skills varchar(200))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Table is Created Successfully!")
    
    def insert_employee(self,eid,ename,desg,did,dname,awards,salary,skills):
        query = "insert into employeedata(EmployeeId,EmployeeName,Designation,DepartmentId,DepartmentName,Awards,Salary,Skills) values({},'{}','{}','{}','{}','{}','{}','{}')".format(eid,ename,desg,did,dname,awards,salary,skills)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Employee Created in Database!")

    def fetch_all_employees(self):
        query = "select * from employeedata"
        cur = self.con.cursor()
        cur.execute(query)
        res = []
        for row in cur:
            res.append(row)
            print(row)
            print("Employee Id:",row[0])
            print("Employee Name:",row[1])
            print("Designation:",row[2])
            print("Department Id:",row[3])
            print("Department Name:",row[4])
            print("Awards:",row[5])
            print("Salary:",row[6])
            print("Skills:",round[7])
            print()
            print()
        return res

    def fetch_one_employee(self,eid):
        query = "select * from employeedata where EmployeeId = {}".format(eid)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
            return row
        return False
    
    def delete_employee(self,EmployeeId):
        query = "delete from employeedata where EmployeeId = {}".format(EmployeeId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Record Deleted!")

    def update_employee(self,EmployeeId,newName,newDesg,newDid,newDname,newAwards,newSalary,newSkills):
        query = "update employeedata set EmployeeName = '{}',Designation ='{}',DepartmentId = '{}',DepartmentName = '{}',Awards = '{}',Salary = '{}',Skills = '{}' where EmployeeId = {}".format(newName,newDesg,newDid,newDname,newAwards,newSalary,newSkills,EmployeeId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Employee is Updated!")

    def fetch_departmentname(self,dname):
        query = "select * from employeedata where DepartmentName='{}' ".format(dname)
        c = self.con.cursor()
        c.execute(query)
        for row in c:
            print(row)
            return row
        return False