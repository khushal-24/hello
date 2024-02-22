import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="system@123",
    database="db1"
)
mycursor=mydb.cursor()


mycursor.execute ("CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255)) ")

sql= "INSERT INTO Customers (name,address) VALUES (%s, %s)"
val=("John","Highway 21")
mycursor.execute(sql,val)

mydb.commit()

'''sql= "INSERT INTO Customers (name,address) VALUES (%s,%s)"
val= [
    ('Peter','Lowstreet 4'),
    ('Amy','Apple st 652'),
    ('Hannah','Mountain 21'),
    ('Michael','Valley 345'),
    ('Sandy','Ocean blvd 2'),
    ('Betty','Green Grass 1'),
    ('Richard','Sky st 331'),
    ('Susan','One way 98')
]
mycursor.executemany(sql,val)
mydb.commit()

mycursor.execute("SELECT * FROM Customers ")
myresult= mycursor.fetchall()'''