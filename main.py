import json
from fastapi import FastAPI

from models.model import LoginModel, UserModel
from utils.Mysql import Mysql

class CarpAPI():
    def __init__(self):
        self.app = FastAPI()
        self.cursor = Mysql().getCursor()
        self.route()

    def route(self):
        @self.app.post("/login/")
        def post_login(item: LoginModel):
            try:
                self.cursor.execute("SELECT * FROM users WHERE account = '" + item.account + "'")
                results = self.cursor.fetchall()
                for row in results:
                    if item.password == row[2]:
                        user = UserModel(isUserValid=True, account=row[0], nickname=row[1], password=row[2])
                        return user
                    else:
                        raise Exception("Invalid password")
            except Exception:
                return UserModel(isUserValid=False)
        
            return UserModel(isUserValid=False)
    
        @self.app.get('/')
        def get_root():
            return json.load(open("./assets/root.json", "r"))

carp_api = CarpAPI()
app = carp_api.app


# app = FastAPI()
# cursor = Mysql().getCursor()

# @app.get('/')
# def get_root():
#     return None

# @app.post("/login/")
# def post_login(item: LoginModel):
#     try:
#         cursor.execute("SELECT * FROM users WHERE account = '" + item.account + "'")
#         results = cursor.fetchall()
#         for row in results:
#             user = UserModel(isUserValid=True, account=row[0], nickname=row[1], password=row[2])
#             return user
    
#     except Exception:
#         print("SQLException " + Exception.args[0])
#         return UserModel(isUserValid=False)
    
#     return UserModel(isUserValid=False)