class User:
    def __init__(self, name: str, email: str, password: str, birthdate: str = None, gender: str = None, points: int = 0):
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate
        self.gender = gender
        self.points = points
        pass

    def __str__(self):
        return f"User({self.name}, {self.email}, {self.password}, {self.birthdate}, {self.gender}, {self.points})"