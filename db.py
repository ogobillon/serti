import mysql.connector

def db_get(host1,user1,passw, db):
    mydb = mysql.connector.connect(
        host=host1,
        user=user1,
        password=passw,
        database=db
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM servicios")


    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return myresult







# db_get("localhost","root","1942""ogobillon$serti_db")

    # mydb = mysql.connector.connect(
    #   host="localhost",
    #   user="root",
    #   password="1942",
    #   database="ogobillon$serti_db"
    # )
    #
    # mycursor = mydb.cursor()
    #
    # mycursor.execute("SELECT * FROM servicios")
    #
    # myresult = mycursor.fetchall()
    #
    # mycursor.close()
    # mydb.close()