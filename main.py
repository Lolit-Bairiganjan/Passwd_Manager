import mariadb
mydb = mariadb.connect(host = 'localhost', user = 'root', passwd = 'lolit007', database = 'test_prep')
mycr = mydb.cursor()
try:
    mycr.execute("SELECT * FROM LIBRARY")
    x = mycr.fetchall()
    print(x, 'Mariadb prints values in the form of list of tuples!')
except mariadb.Error as e:
    print(f"Error: {e}")
