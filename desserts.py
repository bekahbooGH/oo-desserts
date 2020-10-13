class Cupcake:
    """A cupcake."""

    # Class attribute
    cache = {}

    # INSTANCE METHOD::
    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        self.cache[name] = self

    def add_stock(self, amount):
        self.qty = (
            self.qty + amount
        )  # NOTE: self.amount? Nope, it's just amount since we didn't create an instance for it in the __init__
        # return self.qty

    def sell(self, amount):
        if self.qty == 0 and amount > self.qty:
            print("Sorry, these cupcakes are sold out")

        elif self.qty < amount:
            self.qty = 0

        else:
            self.qty = self.qty - amount
            # return self.qty  #Checks that it works

    # STATIC METHOD:
    @staticmethod
    def scale_recipe(ingredients, amount):
        # ingredients = [(ingredient_name , ingredient_qty), ()]
        final_list = []
        for ingr in ingredients:
            multiplied_amount = amount * ingr[1]
            final_list.append((ingr[0], multiplied_amount))
        # print(final_list)
        return final_list

    # Function call:
    # Cupcake.scale_recipe([('flour', 1), ('sugar', 3)], 10)
    # output --> [('flour', 10), ('sugar', 30)]

    # CLASS METHODS:
    @classmethod
    def get(cls, name):
        if name not in cls.cache:
            print("Sorry, that cupcake doesn't exist")

        else:
            return cls.cache[name]

    def __repr__(self):
        """Human-readable printout for debugging."""
        # test_cupcake.name = "testing 123"
        # test_cupcake.qty = 0
        # test_cupcake.flavor = "vanilla"
        # test_price = 1.00

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


if __name__ == "__main__":
    import doctest

    result = doctest.testfile(
        "doctests.py", report=False, optionflags=(doctest.REPORT_ONLY_FIRST_FAILURE)
    )
    doctest.master.summarize(1)
    if result.failed == 0:
        print("ALL TESTS PASSED")
