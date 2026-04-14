


from rich.console import Console
from time import sleep

console = Console()

with console.status("Loading data..."):
    sleep(10)

console.print("Done!")