import time
import uvicorn
import argparse

from assets.logo import print_logo
from main import app
from configs import config

from rich.console import Console
from rich.table import Column, Table
from rich.progress import track
from rich.theme import Theme
from rich import print

from models.model import Logo
from utils.Audio import play_audio_from
from utils.Mysql import Mysql

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=config.BASE_URL, help="Host address")
    parser.add_argument("--port", default=config.BASE_PORT, type=int, help="Port number")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    return parser.parse_args()

if __name__ == "__main__":

    cursor = Mysql().getCursor()
    console = Console()

    # 查询数据库版本信息
    cursor.execute('SELECT VERSION()')
    # 获取查询结果
    db_version = cursor.fetchone()[0]

    # 查询数据库中所有表的数量
    cursor.execute("SHOW TABLES")
    # 获取查询结果
    tables = cursor.fetchall()

    # Print logo
    print_logo(config.LOGO)

    print("\n")

    for step in track(range(len(tables)), description=f"[bold]Connecting to[/bold] [green]{config.DB_NAME}@{config.DB_HOST}:{str(config.DB_PORT)}[/green]"):
        time.sleep(0.4)
    play_audio_from(config.LAUNCH_AUDIO)

    print("\n")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Version", style="dim", width=12)
    table.add_column("Database")
    table.add_column("Host", justify="right")
    table.add_column("Port", justify="right")
    table.add_row(db_version, config.DB_NAME, config.DB_HOST, str(config.DB_PORT))
    console.print(table)
    

    args = parse_arguments()
    if args.reload==True:
        uvicorn.run("main:app", host=args.host, port=args.port, reload=args.reload)
    # End if
    else:
        uvicorn.run(app, host=args.host, port=args.port, reload=False)
    # End else
        
# End