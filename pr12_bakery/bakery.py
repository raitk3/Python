"""PR12."""


class Baker:
    """Baker."""

    def __init__(self, name: str, experience_level: int, money: int):
        """Define Baker."""
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __repr__(self) -> str:
        """
        Product object representation in object format.

        :return: string
        """
        return f"Baker: {self.name}({self.experience_level})"


class Pastry:
    """Pastry."""

    def __init__(self, name: str, complexity_level: int):
        """Define pastry."""
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self) -> str:
        """
        Product object representation in object format.

        :return: string
        """
        return self.name


class Bakery:
    """Bakery."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Define Bakery."""
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.bakers = []
        self.recipes = {}

    def add_baker(self, baker: Baker) -> Baker:
        """Add new baker."""
        if isinstance(baker, Baker) and baker.experience_level >= self.min_experience_level:
            self.bakers.append(baker)
            return baker

    def remove_baker(self, baker: Baker):
        """Remove baker if (s)he exists."""
        if baker in self.bakers:
            self.bakers.remove(baker)

    def add_recipe(self, name: str):
        """Add new recipe."""
        if self.budget - len(name) >= 0 and len(self.bakers) > 0 and name not in self.recipes.keys():
            min_baker = min(baker.experience_level for baker in self.bakers)
            complexity_level = abs(len(name) * len(self.bakers) - min_baker)
            self.budget -= len(name)
            self.recipes[name] = complexity_level

    def make_order(self, name: str) -> Pastry:
        """Make order."""
        pass

    def get_recipes(self) -> dict:
        """Get recipes."""
        return self.recipes

    def get_pastries(self) -> list:
        """Get pastries."""
        pass

    def get_bakers(self) -> list:
        """Get bakers."""
        pass

    def __repr__(self) -> str:
        """
        Product object representation in object format.

        :return: string
        """
        return f"Bakery {self.name}: {len(self.bakers)} baker(s)"


if __name__ == '__main__':

    bakery1 = Bakery("Pagariposid", 10, 100)
    print(bakery1)  # Bakery Pagariposid: 0 baker(s)

    bakery1.add_baker(Baker("Ago", 9, 0))
    bakery1.add_baker(Baker("Teet", 10, 0))
    bakery1.remove_baker(Baker("Teet", 10, 0))
    print(bakery1.bakers)
    print(bakery1)  # Bakery Pagariposid: 0 baker(s) => Baker Ago was not added because of low experience level (Sorry Ago)

    print(bakery1.make_order("cake"))  # None => No such recipe nor baker in bakery
    print(bakery1.remove_baker(Baker("Teet", 2, 22)))
    ########################################################################

    polly = Baker("Polly", 10, 5)
    sam = Baker("Sam", 11, 0)
    emma = Baker("Emma", 12, 6)

    bakery1.add_baker(polly)
    bakery1.add_baker(sam)
    bakery1.add_baker(emma)

    # Trying to make order when no recipes are in bakery

    print(bakery1.make_order("cake"))  # None

    bakery1.add_recipe("cake")
    print(bakery1.budget)  # 96 (100 - len('cake') = 96 => price for recipe)
    print(bakery1.get_recipes())  # {'cake': 2}

    print(bakery1.make_order("cake"))  # cake
    print(
        bakery1.get_bakers())  # [Baker: Polly(14), Baker: Emma(12), Baker: Sam(11)] =>
    # Polly was chosen to be the baker because 'cake' complexity and Polly experience lever were the closest
    # Polly experience level was increased by len('cake') => 10 + 4 = 14

    print(bakery1.budget)  # 104 (used to be 96: 96 + len('cake') * 2 = 104)
    print(polly.money)  # 13 (5 she had + len('cake') * 2 = 13)

    print(bakery1.get_pastries())  # [cake] ("NB! cake is instance of class Pastry, not a string)

    ########################################################################

    bakery2 = Bakery("Pihlaka", 11, 100)

    john = Baker("John", 11, 5)
    megane = Baker("Megane", 17, 4)
    kate = Baker("Megane", 18, 8)

    bakery2.add_baker(john)
    bakery2.add_baker(megane)
    bakery2.add_baker(kate)

    bakery2.add_recipe("muffin")
    bakery2.add_recipe("cupcake")
    bakery2.add_recipe("biscuits")

    print(bakery2.get_recipes())  # {'muffin': 7, 'cupcake': 10, 'biscuits': 13}

    print(
        bakery2.get_bakers())  # [Baker: Megane(18), Baker: Megane(17), Baker: John(11)]
    bakery2.make_order("biscuits")
    print(
        bakery2.get_bakers())  # [Baker: Megane(25), Baker: Megane(18), Baker: John(11)]
    # Magane was chosen to be the baker as the most closest experience (which is also greater than complexity) was 17.
