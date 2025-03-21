class Add:
    def init(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b  # Works for both numbers and strings

# Example usage
if name == "main":
    print(Add(5, 3).calculate())  # Output: 8
    print(Add("abs", "ent").calculate())  # Output: "absent"