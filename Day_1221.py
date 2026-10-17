

from dataclasses import dataclass

@dataclass
class YouTuber:
    name : str
    videos : int
    subs : int

    def intro(self):
        print(f'Welcome to {self.name}!')

x = YouTuber('TechnicallyRipped',
             1200,
             11000)

x.intro()
