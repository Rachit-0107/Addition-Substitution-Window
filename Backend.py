import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root', #your username
    password='', #your password
    database='ADD_SUB_Window'
)

cursor=db.cursor()

def addition(studid,courseid):
    cursor.execute("CALL ADDITION(%s,%s)",(studid,courseid))
    temp=cursor.fetchall()
    print(temp[0][0])

def substitution(studid,courseidold,courseidnew):
    cursor.execute("CALL SUBSTITUTION(%s,%s,%s)",(studid,courseidold,courseidnew))
    temp=cursor.fetchall()
    print(temp[0][0])

choice=0
while(choice!=3):
    
    print("\nEnter your choice:")
    print("1. Add Course")
    print("2. Substitute Course")
    print("3. Exit\n")
    choice=int(input())
    if(choice==1):
        print("\nEnter student id:")
        studid=int(input())
        print("Enter course id:")
        courseid=int(input())
        addition(studid,courseid)
        print("\n")
        
    elif(choice==2):
        print("\nEnter student id:")
        studid=int(input())
        print("Enter course id old:")
        courseidold=int(input())
        print("Enter course id new:")
        courseidnew=int(input())
        substitution(studid,courseidold,courseidnew)
    else:
        print("\nExiting")
        exit()
