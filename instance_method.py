# Instance method

class User:
    def __init__(self, name):
        self.name = name 

    def greet(self):
        return f"Hi, {self.name}"


# class method 

class User:
    count = 0 

    def __init__(self, name):
        self.name = name 
        User.count += 1 

    @classmethod 
    def from_string(cls, s):
        name = s.split(',')[0]
        return cls(name)

u = User.from_string('Anna,25')


# static method 

class User:
    @staticmethod
    def is_valid_name(name):
        return len(name) > 1 and name.isalpha()

User.is_valid_name('Anna')


