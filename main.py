import pymongo

class PymongoConnection:
    def __init__(self) -> None:
        pass

    def my_client(self):
        """Create the mongodb connection."""
        return pymongo.MongoClient("mongodb://localhost:27017/")


    def create_db(self):
        """Create the first_database database if is does not exist."""
        return self.my_client()["first_database"]

    
    def check_database_names(self):
        """Return a list of the name of databases."""
        return self.my_client().list_database_names()

