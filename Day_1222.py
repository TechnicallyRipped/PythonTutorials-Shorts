

from dataclasses import dataclass

@dataclass
class YouTuber:
    name : str
    videos : int = 0
    subs : int = 0

    def intro(self):
        print(f'Welcome to {self.name}!')

x = YouTuber('TechnicallyRipped')

x.intro()
print(x.subs)
