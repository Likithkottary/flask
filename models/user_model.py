import mysql.connector

class user_model:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="", database="flask_db")
            self.con.autocommit=True #will commit your query after ur execution else u need to write it separately after execution
            self.cur = self.con.cursor()
            print("Connected")
        except:
            print("Error connecting DB")

    def user_login_model(self): #GET
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()  
        if len(result) > 0: 
            print(len(result))
            return result  
        else:
            return "No Data Found"                      

    def user_add_model(self,data): #POST
        print(data)
        name = data['name']
        age = data['age']
        self.cur.execute(f"INSERT into users(name,age)VALUES('{name}','{age}')")
        return "User created"

    def user_update_model(self,data): #PUT
        name = data['name']
        age = data['age']
        self.cur.execute(f"UPDATE users set age='{age}' where name ='{name}' ")
        if self.cur.rowcount > 0 :
            return "User Updated"
        else:
            return "No user updated"
        
    def user_delete_model(self,id): #DELETE
        self.cur.execute(f"DELETE from users where id ='{id}'")
        if self.cur.rowcount > 0 :
            return "User Deleted"
        else:
            return "No user Deleted"