

from rich.table import Table
from rich.console import Console

console = Console()
table = Table(header_style="white on green")

table.add_column("Name",style="white on red")
table.add_column("Score",style="white on blue")

table.add_row("Mike", "90")
table.add_row("Patrick", "95",style='bold')
table.add_row("Chris", "88",style='italic')

console.print(table)








# table.add_column("Name", style="black on red")
# table.add_column("Score", style="white on blue")

# table.add_row("Mike", "90")
# table.add_row("Patrick", "95", style='bold')
# table.add_row("Chris", "88", style='italic')

# console.print(table)