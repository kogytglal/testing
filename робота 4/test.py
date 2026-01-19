a = input("Enter a number: ")
assert a.isdigit(), "You must enter a number!"
print(f"Entered number: {a}")

class Figure:
    def __init__(self, type, length):
        assert length > 0, "Length must be greater than 0!"
        assert type in ["square", "rectangle", "triangle"], "Allowed figures: square, rectangle, triangle"
        self.type = type
        self.length = length

f3 = Figure("square", 1)
print(f"Figure created: {f3.type}, length {f3.length}")

class Name:
    def __init__(self, name, hobby):
        if name not in ["Taras", "Anonymous"]:
            raise ValueError("Allowed names: Taras, Anonymous")
        if not hobby:
            raise ValueError("Hobby must not be empty")
        self.name = name
        self.hobby = hobby

n2 = Name("Taras", "reading")
print(f"Name created: {n2.name}, hobby: {n2.hobby}")
