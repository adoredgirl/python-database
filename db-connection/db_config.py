import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
                                            user = 'root',
                                            password = 'Mariyashaikh@12345',
                                            host = 'localhost',
                                            database = 'pdbc'
                                        )
        
        return connection
            
    except Exception:
        print("some problem occured")
        return None