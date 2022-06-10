import mysql.connector


class Base:
    def __init__(self):
        self.__dbname = "sql6497641"
        self.__dbuser = "sql6497641"
        self.__dbpass = "9c7ymcwsIl"
        self.__dbhost = "sql6.freemysqlhosting.net"
        self.__tbname = "emergency"

        # connects the python to a remote database
        self.__connect(self.__dbhost, self.__dbuser, self.__dbpass, self.__dbname)

    def __connect(self, dbhost, dbuser, dbpass, dbname):
        try:
            self.mydb = mysql.connector.connect(
                host=dbhost,
                user=dbuser,
                password=dbpass,
                database=dbname,
            )

            self.cursor = self.mydb.cursor(buffered=True)

        except mysql.connector.Error as err:
            print("\nError: " + err.msg)

    def __reconnect(self):
        # close connections
        self.close_conn()

        # reconnect to the database
        self.__connect(self.__dbhost, self.__dbuser, self.__dbpass, self.__dbname)

    def __del__(self):
        self.close_conn()

    def close_conn(self):
        self.cursor.close()
        self.mydb.close()

    def receive_sos(self):
        # reconnect to the database
        self.__reconnect()

        mydict = {}  # where we store all the data

        # selects only those who need sos
        query = f"""SELECT * FROM {self.__tbname} WHERE sos = true;"""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        for row in rows:
            # stores the values in a dictionary with id as key and location as value
            mydict[row[1]] = row[2]

        return mydict

    def respond_sos(self, id):
        # reconnect to the database
        self.__reconnect()

        # gets the location of the id
        query = f"""SELECT location FROM {self.__tbname} WHERE id='{id}';"""
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        # responds to that sos
        query = f"""UPDATE {self.__tbname} SET sos=false WHERE id='{id}';"""
        self.cursor.execute(query)
        self.mydb.commit()

        if row != None:
            print(f"Responded to {row[0]}'s SOS.")
