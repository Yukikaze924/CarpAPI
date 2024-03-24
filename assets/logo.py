from models.model import Logo
from utils.spliter import split_string
from rich.console import Console


def print_logo(type: Logo):

   console = Console()

   if type == Logo.Default:
      print(get_logo())
      return
   
   elif type == Logo.Ukraine:
      parts = split_string(get_logo(), 2)
      console.print(f"[blue]{parts[0]}[/blue][#FFD700]{parts[1]}[/#FFD700]")
      return
   
   elif type == Logo.Russia:
      parts = split_string(get_logo(), 3)
      console.print(f"[white]{parts[0]}[/white][blue]{parts[1]}[/blue][red]{parts[2]}[/red]")
   
   elif type == Logo.Rainbow:
      parts = split_string(get_logo(), 7)
      console.print(f"[red]{parts[0]}[/red]"
              f"[#FFA500]{parts[1]}[/#FFA500]"
              f"[#FFD700]{parts[2]}[/#FFD700]"
              f"[green]{parts[3]}[/green]"
              f"[cyan]{parts[4]}[/cyan]"
              f"[blue]{parts[5]}[/blue]"
              f"[purple]{parts[6]}[/purple]")
      return

def get_logo() -> str:
    return """                                                                       
    ,o888888o.             .8.          8 888888888o.   8 888888888o   
   8888     `88.          .888.         8 8888    `88.  8 8888    `88. 
,8 8888       `8.        :88888.        8 8888     `88  8 8888     `88 
88 8888                 . `88888.       8 8888     ,88  8 8888     ,88 
88 8888                .8. `88888.      8 8888.   ,88'  8 8888.   ,88' 
88 8888               .8`8. `88888.     8 888888888P'   8 888888888P'  
88 8888              .8' `8. `88888.    8 8888`8b       8 8888         
`8 8888       .8'   .8'   `8. `88888.   8 8888 `8b.     8 8888         
   8888     ,88'   .888888888. `88888.  8 8888   `8b.   8 8888         
    `8888888P'    .8'       `8. `88888. 8 8888     `88. 8 8888         
"""