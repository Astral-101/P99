class IceCream(object):
    def __init__(self, flavor, popularity):
        self.flavor = flavor
        self.popularity = popularity

    def iceCreamDetails(self):
        return print("The ice cream is " + strawberry.flavor)

    def popularityDetails(self):
        return print("The ice cream's popularity is " + strawberry.popularity)


strawberry = IceCream("Strawberry", "100")

print(strawberry.iceCreamDetails())
print(strawberry.popularityDetails())