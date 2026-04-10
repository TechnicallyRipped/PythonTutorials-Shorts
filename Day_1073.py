



from rich.prompt import Prompt

name = Prompt.ask("Enter your name",
                  default='Mike',
                  choices=['Mike','Joe'])

print(name)








