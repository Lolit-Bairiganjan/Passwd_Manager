from argon2 import PasswordHasher
import mariadb
mydb = mariadb.connect(host = 'localhost', user = 'root', passwd = 'lolit007', database = 'test_prep')
mycr = mydb.cursor()
##Taking input for NEW/EXISTING USER
begin = input(">New User?(1) or Existing User?(2):\n-----------------------------------\n>")

##Function Definitions

#function to take user's words for creating profile
def new_user():
    print("~Welcome New User~\n>This is a passwd manager app.\n>Here you can store all your passwords securely into a vault and access them whenever you need.")
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
        if len(password) <= 8:
            print("Password must be atleast 8 characters long. Try again!")
        elif password.isalnum() == False:
            print("Password must contain both letters and numbers. Try again!")
        else:
            print("Password Accepted")

#function to create a username/password
def create_user_passwd():
    global uid
    global email_id
    global password
    uid = input("Enter username: ")
    email_id = input("Enter your email_id: ")
    password = input("Enter a password: ")
    passwd_input()
    
    confirm_password = input("Confirm your password.")
    if password != confirm_password:
        passwd_input()
    else:
        profile_created()


#function finally creates a proifle after user input is done 
def profile_created():


#Function Calls
new_user()



try:
    mycr.execute("SELECT * FROM LIBRARY")
    
except mariadb.Error as e:
    print(f"Error: {e}")
