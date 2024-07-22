import mysql.connector
mysw = mysql.connector.connect (host='localhost',username='root',password='1234',database='project_1')
print(mysw)

myca=mysw.cursor()

#cre=myca.execute("create table Admin_1(no int primary key auto_increment,Python varchar(50),Mysql varchar(50),Html varchar(50))")
#db=myca.execute("create table user(no int primary key auto_increment,category varchar(15),score int)")
'''
ins1="INSERT INTO admin(Python,Mysql,Html) VALUES (%s,%s,%s)"
mysw.close()
'''
class Quiz():
    def __init__(self):
        self.admin="Quiz"
        print("   ------------------------------------------")
        print("       <<<<<<<< Welcome To Quiz >>>>>>        ")
        print("   ------------------------------------------")
        print("___________--__Admin__--____________","_____________--__User__--___________")
        print("   ____________(10)_____________","       ______________(11)_____________")
        print("Are you admin or user")
               
    def Admin(self):
        print("Admin")
        print("Add New Questions")
            
        ins="INSERT INTO admin_1(Python,Mysql,Html) VALUES (%s,%s,%s)"
        val=[
               ("What will be the output of the following code snippet?:\n print(2**3 + (5 + 6)**(1 + 1))",
                "To see the list of options provided by MYSQL which of the following command is used?",
                "How many sizes of headers are available in HTML by default?"),
                ("What will be the datatype of the var in the below code snippet?:\n var = 10 \n print(type(var))\n var = 'Hello'\n print(type(var))",
                "What do you mean by HOST in MYSQL?",
                "What is the smallest header in HTML by default?"),
                ("How is a code block indicated in Python?",
                "Is a semicolon necessary after every query?",
                "What are the types of lists available in HTML?"),
                ("What will be the output of the following code snippet?:\n a = [1, 2, 3] \n a = tuple(a)\na[0] = 2 \n print(a)",
                "To know your MYSQL version and current date which of the following command you should use?",
                "How to create an ordered list in HTML?")
            ]
        try:
            myca.executemany(ins,val)
            mysw.commit()   
            print(myca.rowcount,"!1_row inserted")
        except:
            mysw.rollback()
              
        
    def User(self):
        print("       -----------------------------")
        print("            <<<<<Category>>>>>>")
        print("       -----------------------------")
        print("")
        print("--__Python__--","--__Mysql__--","--__HTML__--")
        print("_____(1)___________ (2)___________(3)_________")
        
        print("select a number to choose your category:")
p=Quiz()
A=int(input("choose a number to go your option:"))
if A==10:
    p.Admin()
if A==11:    
    p.User()
    n=int(input("enter a category:"))
    if n==1:
        print("__Python__")
        try:
            myca.execute("SELECT Python FROM admin_1")
            questions = myca.fetchall()
            options=(("A.129","B.8","C.121","D.None of the above"),
                    ("A.str and int","B.int and int","C.str and str","D.int and str"),
                    ("A.Brackets","B.Indentation","C.Key","D.None of the above"),
                    ("A.32","B.16","C.128","D.No fixed length is specified"))
                    
            answers=("A","D","B","D")
            users=[]
            score=0
            question_num=0
            for q in questions:
                print("")
                print(q[0])
                for o in options[question_num]:
                    print(o)
    
                user=input("enter(A,B,C,D):").upper()
                users.append(user)
                if user==answers[question_num]:
                    score += 1
                    print("correct!")
                else:
                    print("incorrect!")
                    print(f"{answers[question_num]}is the correct answer")
                question_num += 1
            print("__________")

            print(" RESULTS    ")

            print("__________")

            score=int(score/len(questions) * 100)
            print(f"your score is : {score}%")
            myca.commit()
        except:
            mysw.rollback()
    elif n==2:
        print("__Mysql__")
        try:
            myca.execute("SELECT Mysql FROM admin_1")
            questions = myca.fetchall()
            options=(("A.HELP","B.–HELP","C.--HELP","D.ELP-"),
                    ("A.HOST is the user name","B.HOST is the representation of where the MYSQL server is running","C.HOST is the administration’s machine name"),
                    ("A.TRUE","B.FALSE"),
                    ("A.VERSION.CURRENT_DATE();","B.SELECT VERSION,CURRENT_DATE();","C.SELECT VERSION(), CURRENT_DATE;","D.SELECT VERSON(),CURRENT_DATE();"))

            answers=("B","C","B","A")
            users=[]
            score=0
            question_num=0

            for q in questions:
                print("")
                print(q[0])
                for o in options[question_num]:
                    print(o)
            
                user=input("enter(A,B,C,D): ").upper()
                users.append(user)
                if user==answers[question_num]:
                    score += 1
                    print("correct!")
                else:
                    print("incorrect!")
                    print(f"{answers[question_num]}is the correct answer")
                question_num += 1    
            print("__________")

            print(" RESULTS    ")

            print("__________") 

            score=int(score/len(questions) * 100)
            print(f"your score is : {score}%")
            myca.commit()
        except:
            mysw.rollback()
    elif n==3:
        print("__HTML__")
        try:
            myca.execute("SELECT Html FROM admin_1")
            questions = myca.fetchall()
            options=(("A.5","B.4","C.1","D.6"),
                    ("A.h1","B.h2","C.h4","D.h6"),
                    ("A.Ordered,Unordered list","B.Bullet,numbered list","C.Named,Unnamed list","D.None of the above"),
                    ("A.<ul>","B.<ol>","C.<href>","D.<b>"))
        
            answers=("D","D","A","B")
            users=[]
            score=0
            question_num=0
        
            for q in questions:
                print("")
                print(q[0])
                for o in options[question_num]:
                    print(o)
                user=input("enter(A,B,C,D): ").upper()
                users.append(user)
                if user==answers[question_num]:
                    score +=1
                    print("Correct!")
                else:
                    print("Incorrect!")
                    print(f"{answers[question_num]}is the correct answer")
                question_num += 1
            print("______________________")
            print("       Results       ")
            print("______________________")
        
            score=int(score/len(questions)*100)
            print(f"your score is :{score}%")
  
            myca.commit()
        except:
            mysw.rollback()
        finally:
            mysw.close()

        


