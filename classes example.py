#Classes
# A program matic object containing data and methods
#i.e variable and functions

#basic form
"""
class Classname:

    attribute = "some data"

    def methodename(input):
        <code for method goes here>
        return value
"""

class Dog:
    breed = "fox"
    weight = 35
    energy = "Medium"

    def communicate(self):
        return "woof"



goldie = Dog()

print(goldie.breed)
print(goldie.communicate())