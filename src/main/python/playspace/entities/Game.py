from dataclasses import dataclass

@dataclass
class Game:
    name: str
    tags: list
    assesment: list = None

    def add_assesments(self, assesment):
        assesment.append(assesment)
@dataclass
class Assessments:
    rating: int
    comment: str
    date: str
