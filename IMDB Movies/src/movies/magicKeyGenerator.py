# Implementation of builder pattern for generating a magic key object with 3 categories
# If more categories are needed in the future, just change 'numberofcategoriesAllowed'
# for changing the algorithm when using more categories just change the return statement of getMagicKey()

class MagicKeyGenerator():
    def __init__(self):
        self.categories = []
        self.count = 1
        self.numberofcategoriesAllowed = 3
    
    def addCategory(self, category):
        if self.count > self.numberofcategoriesAllowed:
            raise Exception("Cannot add more than 3 categories")
        else:
            self.count += 1
            self.categories.append(category)
            return self
            
    def getMagicKey(self):
        if self.categories.__len__() != self.numberofcategoriesAllowed:
            raise Exception("Magic key must have 3 categories")
        else:
            return (self.categories[0]*self.categories[1]*self.categories[2]%5)+1

    def getCategories(self):
        return self.categories

""" x = MagicKeyGenerator()
x.addCategory(3).addCategory(9).addCategory(7)
print(x.getMagicKey()) """


