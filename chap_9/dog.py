class Dog():
    """A Simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simnulate a dog sitting in response to a commade"""
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
