import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1', # localhost
         port=3306,
         database='flight_game2',
         user='username',
         password='password',
         autocommit=True,
        # tarvitaan uudelle 9.0 versiolle ajurista:
         collation='utf8mb4_general_ci'
         )
