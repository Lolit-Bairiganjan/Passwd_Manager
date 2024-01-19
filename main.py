import mariadb
mydb = mariadb.connect(host = 'localhost', user = 'root', passwd = 'lolit007', database = 'passwd_manager')
mycr = mydb.cursor()


##Constants
global value


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
        if len(password) <= 8:
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
    mycr.execute(f'INSERT INTO PROFILE VALUES ({uid},{email_id},{password})')
    print("\n~Profile succesfully created~")


#function for accessing the various roots associated with existing user
def existing_user():
    existing_user_input = input("\nAccess all username/passwords?(1), Add a website username/pasword?(2), Access particular website password?(3):\n--------------------------------------------------------------------------------------------------------------\n>")
    if existing_user_input == '1':
        access_all()

#function to Add New Website Passwords
def add_new():
    value = mycr.execute("INSERT INTO [TABLE] VALUES()")


#function to access a particular password
def access_particular():
    value = mycr.execute(f"SELECT * FROM [TABLE] WHERE [CONDITION]")


#function to access all username/password of websites
def access_all():  
    value = mycr.execute(f'SELECT * FROM PROFILE')
    for i in value:
        for j in i:
            print(j,end='')




try:
    mycr.execute("SELECT * FROM LIBRARY")
    #Function Calls
    if begin == '1':
        new_user()
    elif begin == '2':
        existing_user()
    else:
        pass

    
except mariadb.Error as e:
    print(f"Error: {e}")
