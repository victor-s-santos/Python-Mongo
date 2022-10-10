import pymongo

class PymongoConnection:
    def __init__(self) -> None:
        pass

    def create_connection(self):
        """Create the mongodb connection."""
        return pymongo.MongoClient("mongodb://localhost:27017/")


    def create_db(self):
        """Create the first_database database if is does not exist."""
        return self.create_connection(["first_database"])



