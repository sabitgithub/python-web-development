import mysql.connector
# pip install mysql-connect-python

class Database:
    
    def createDatabase(self,db):
        self.con=mysql.connector.connect(host="localhost",username="root",password="")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE database IF NOT EXISTS "+db)
        self.con.commit()
    
    
    def __init__(self,dbase) -> None:
        self.createDatabase(dbase)
        self.con=mysql.connector.connect(host="localhost",username="root",password="",database=dbase)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS employee(\
            emp_id INTEGER PRIMARY KEY AUTO_INCREMENT,\
            emp_name varchar(50),\
            email VARCHAR(50),\
            emp_salary INTEGER)")
        self.con.commit()
        
    def insertData(self):
        print("Add new Data")
        print("="*50)
        name=input("Name        : ")    
        email=input("Email      : ")    
        salary=input("Salary    : ")
        
        self.cur.execute("INSERT INTO employee (emp_name,email,emp_salary) VALUES (%s,%s,%s)",(name,email,salary))
        self.con.commit()
        
    def showData(self):
        print("Show Data")
        print("="*50)
        self.cur.execute("SELECT * FROM employee")
        print('\n\n %-5s %20s %-20s %-10s' %("Employee ID","Employee Nane","Email Address","Salary"))
        print("="*80)
        
        employess=self.cur.fetchall()
        
        for data in employess:
            print('%-5s %-20s %-20s %-10s' %(data[0],data[1],data[2],data[3]))
        
        print(f'Total Numbers of Records {len(employess)}')    
            
        

db=Database('bitmdb')
db.insertData()
db.showData()
            
        
        