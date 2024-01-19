import mariadb
mydb = mariadb.connect(host = 'localhost', user = 'root', passwd = 'lolit007', database = 'test_prep')
mycr = mydb.cursor()
#Taking input for NEW/EXISTING USER
begin = input("New User?(1) or Existing User?(2):\n----------------------------------\n>")

#Function Definitions
def new_user():
    print("~Welcome New User~")


#Function Calls
new_user()



try:
    mycr.execute("SELECT * FROM LIBRARY")
    
except mariadb.Error as e:
    print(f"Error: {e}")
