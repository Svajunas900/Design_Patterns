#  Create class DBSingleton - with singleton implementation of connecting to the sqlite db
import sqlite3

# Main purpose of this pattern in this class to reduce connections and instead create only one that is shared among all users
class SQLiteConnection:
    # Declare shared state
    _instance = None

    # Create a cursor which will execute queries
    def cursor(cls):
        cls._instance = cls._instance.cursor()
        return cls._instance
    
    # Check if Database instance exists if exits return it if not create and connect to tutorial.db
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = sqlite3.connect("tutorial.db")
        return cls._instance
    

