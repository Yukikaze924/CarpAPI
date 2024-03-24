import json
from fastapi import FastAPI
from rich.console import Console
from rich.markdown import Markdown

from models.model import LoginModel, UserModel
from utils.Mysql import Mysql
from utils.Logger import Log

class CarpAPI:
    def __init__(self):
        self.app = FastAPI()
        self.cursor = Mysql().getCursor()
        self.route()
    # End

    def route(self):

        @self.app.get('/')
        def get_root():
            return json.load(open("./assets/root.json", "r"))
        # End get_root()

        @self.app.post("/login/")
        def post_login(item: LoginModel):
            try:
                self.cursor.execute("SELECT * FROM users WHERE account = '" + item.account + "'")        
                results = self.cursor.fetchall()

                columns = [desc[0] for desc in self.cursor.description]
                rows = [dict(zip(columns, row)) for row in results]

                for row in rows:
                    if item.password == row['password']:
                        user = UserModel(isUserValid=True, account=row['account'], nickname=row['nickname'], password=row['password'])
                        return user
                    else:
                        raise Exception("Invalid password")
                # for row in results:
                #     if item.password == row[2]:
                #         user = UserModel(isUserValid=True, account=row[0], nickname=row[1], password=row[2])
                #         return user
                #     else:
                #         raise Exception("Invalid password")
                    
            except Exception:
                return UserModel(isUserValid=False)
        
            return UserModel(isUserValid=False)
        # End post_login()

# End

app = CarpAPI().app



if __name__ == '__main__':

    console = Console()

    with open("./assets/docs/usage.md", encoding='utf-8') as readme:
        markdown = Markdown(readme.read())
    
    console.print(markdown)

    Log.getLogger().error("[bold red blink]This is not the entry point![/]", extra={"markup": True})
# End