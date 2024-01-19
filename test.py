import mariadb
mydb = mariadb.connect(host = 'localhost', user = 'root', passwd = 'lolit007', database = 'test_prep')
mycr = mydb.cursor()
print(mydb)
