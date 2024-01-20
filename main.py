##Imports
import mariadb
from prettytable import PrettyTable


##Python Mariadb connection
mydb = mariadb.connect(host = 'localhost', user = 'root', passwd = 'lolit007', database = 'passwd_manager')
mycr = mydb.cursor()


##Constants
profile_column = ['UNAME','EMAIL','PASSWD']
passwds_column = ['WNAME','WLINK','WPASSWD','UNAME','WID']


##Taking input for NEW/EXISTING USER
begin = input(">New User?(1) or Existing User?(2):\n-----------------------------------\n>")


##Function Definitions

#function to take user's words for creating profile
def new_user():
    print("\n~Welcome New User~\n>This is a passwd manager app.\n>Here you can store all your passwords securely into a vault and access them whenever you need.")
    loop = 't'
    while loop == "t":
        new_user_input = input("\nCreate username/passwd now(1) or create later(2):\n-------------------------------------------------\n>")
        if new_user_input == '1':
            create_user_passwd()
            loop = 'f'
        elif new_user_input == '2':
            break
        else:
            print("Wrong input. Try Again!!")


#function takes the input of password in right way
def passwd_input():
    loop = 't'
    while loop == 't':
        if len(password) < 8:
            print("\n+------------------------------------------------------+\n|Password must be atleast 8 characters long. Try again!|\n+------------------------------------------------------+")
            new_user()
        elif password.isalnum() == False:
            print("Password must contain both letters and numbers. Try again!")
            new_user()
        else:
            print("Password Accepted")
            loop = 'f'


#function to create a username/password
def create_user_passwd():
    global uid
    global email_id
    global password
    uid = input("\n>Enter username:\n----------------\n>")
    email_id = input("\n>Enter your email_id:\n---------------------\n>")
    password = input("\n>Enter a password:\n------------------\n>")
    passwd_input()
    
    confirm_password = input("Confirm your password:\n----------------------\n")
    if password != confirm_password:
        passwd_input()
    else:
        profile_created()


#function finally creates a proifle after user input is done 
def profile_created():
    mycr.execute(f"INSERT INTO PROFILE VALUES('{uid}','{email_id}','{password}');")
    print("\n~Profile succesfully created~")


#Setup password for existing user
def passwd_validation():
    global uid
    global password
    uid = input("\nEnter your existing username:\n-----------------------------\n>")
    password = input("\nEnter your existing password:\n-----------------------------\n>")
    mycr.execute(f"SELECT UNAME,PASSWD FROM PROFILE WHERE UNAME='{uid}'")
    value = mycr.fetchone()
    try:
        if value[1] == password:
            existing_user()
        else:
            print("\n~Wrong password. Try Again!~")
            passwd_validation()   
    except TypeError:
        print("+-----------------------+\n|Enter a valid username!|\n+-----------------------+")

#function for accessing the various roots associated with existing user
def existing_user():
    existing_user_input = input("\nAccess all username/passwords?(1), Add a website username/pasword?(2), Access particular website password?(3):\n--------------------------------------------------------------------------------------------------------------\n>")
    if existing_user_input == '1':
        access_all()
    elif 3:
        w_input = input("\nEnter website name:\n-------------------\n>").upper()
        access_particular(w_input)

#function to Add New Website Passwords
def add_new():
    value = mycr.execute("INSERT INTO [TABLE] VALUES()")


#function to access a particular password
def access_particular(wname):
    mycr.execute(f"SELECT * FROM PASSWDS WHERE (UNAME='{uid}'&& WNAME='{wname}')")
    value = mycr.fetchall()
    myTable = PrettyTable(passwds_column)
    for i in value:
        myTable.add_row(i)
    print(myTable)

#function to access all username/password of websites and print them beautifully
def access_all():  
    mycr.execute(f"SELECT * FROM PASSWDS WHERE UNAME='{uid}'")
    value = mycr.fetchall()
    for i in value:
        for j in i:
            title = passwds_column[i.index(j)-1]
            multiplier = (len(title)*'-')+'-'
            print(f"{multiplier}\n"+title+':')
            print(j)
        multiplier = (len(j)*'-')
        print(multiplier)



try:
    #Function Calls
    if begin == '1':
        new_user()
    elif begin == '2':
        passwd_validation()
    else:
        pass

    mydb.commit()

    
except mariadb.Error as e:
    print(f"Error: {e}")
mydb.close()