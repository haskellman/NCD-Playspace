class Game:
    def __init__(self, name: str, record: int, link: str, tag: list[str] = None):
        self.name = name
        self.record = record
        self.link = link
        self.tag = tag
        pass

    def __str__(self):
        return f"Game({self.name}, {self.record}, {self.link}, {self.type})"