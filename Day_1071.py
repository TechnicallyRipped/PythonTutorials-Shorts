

from rich.console import Console
from rich.table import Table

console = Console()
table = Table()

table.add_column("Name")
table.add_column("Age")
table.add_row('Joe','20')
table.add_row('Chris','30')
table.add_row('Mike','35')

console.print(table)