#############
# Basic SOS Send System
# Author: Zherish Galvin Mayordo
#
# How to use:
# 1. Import comms in your main program
# 2. Initialize the Comms class with id and location
# 3. Use send_sos() to send SOS to the base
# 4. Use is_clear() to check if the base has responded to the SOS message
#
# Note: SOS will not be turned off even if Python program is offline
# Note: This is made to allow consistent inputs in the database
#############

import mysql.connector


class Comms:
    def __init__(self, id, location):
        self.__dbname = "sql6497641"
        self.__dbuser = "sql6497641"
        self.__dbpass = "9c7ymcwsIl"
        self.__dbhost = "sql6.freemysqlhosting.net"
        self.__tbname = "emergency"

        self.__id = id  # primary key id
        self.__location = location

        # connects the python to a remote database
        self.__connect(self.__dbhost, self.__dbuser, self.__dbpass, self.__dbname)

        # introduce self to database
        self.__introduce()

    def __del__(self):
        self.close_conn()

    def close_conn(self):
        self.cursor.close()
        self.mydb.close()

    def __introduce(self):
        # introduce self to database
        try:
            query = f"""INSERT INTO {self.__tbname} (id, location, sos) VALUES ('{self.__id}', '{self.__location}', false) ON DUPLICATE KEY UPDATE location='{self.__location}';"""
            self.cursor.execute(query)
            self.mydb.commit()

        except mysql.connector.Error as err:
            print("\nError: " + err.msg)

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

    def send_sos(self):
        # reconnect
        self.__reconnect()

        # send SOS to the base
        query = f"""UPDATE {self.__tbname} SET sos=true WHERE id='{self.__id}';"""
        self.cursor.execute(query)
        self.mydb.commit()
        print(f"SOS at {self.__location} has been sent.")

    def is_clear(self):
        # reconnect
        self.__reconnect()

        # check if SOS has responded
        query = f"""SELECT * FROM {self.__tbname} WHERE id='{self.__id}';"""
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        if row[3] == 0:
            # Node is clear
            return True
        else:
            # Node is not clear
            return False
