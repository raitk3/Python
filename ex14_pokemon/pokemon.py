"""EX14."""
import requests
import random
url = "https://pokeapi.co/api/v2/pokemon/"


class CannotAddPokemonException(Exception):
    """Custom exception."""

    pass


class NoAvailablePokemonsInWorldException(Exception):
    """Custom exception."""

    pass


class Person:
    """Simple Person class."""

    def __init__(self, name, age):
        """
        Person constructor.

        :param name: Name of the Person.
        :param age:  Age of the Person.
        """
        self.name = name
        self.age = age
        self.pokemon = None

    def add_pokemon(self, pokemon):
        """
        Add pokemon to Person.

        :param pokemon: Pokemon to add.
        :return:
        """
        if self.pokemon is None and isinstance(pokemon, Pokemon) and pokemon.person is None:
            self.pokemon = pokemon
            pokemon.person = self
        elif self.pokemon:
            raise CannotAddPokemonException("Person already has a pokemon!")
        elif not isinstance(pokemon, Pokemon):
            raise CannotAddPokemonException("Must be instance of Pokemon!")
        else:
            raise CannotAddPokemonException

    def get_pokemon(self):
        """
        Get Person's Pokemon.

        :return: Pokemon or None.
        """
        return self.pokemon

    def remove_pokemon(self):
        """Remove Person's Pokemon."""
        self.pokemon.person = None
        self.pokemon = None

    def __repr__(self):
        """
        Representation of object.

        :return: Person's name, Person's age, Pokemon: Person's pokemon.
        """
        return f"({self.name}, {self.age}, Pokemon: {self.pokemon}."


class Data:
    """Class for getting data from API."""

    @staticmethod
    def get_all_pokemons_data(endpoint):
        """
        Make request to API.

        :param endpoint: Address where to make the GET request.
        :return: Response data.
        """
        return requests.get(endpoint).json()

    @staticmethod
    def get_additional_data(endpoint):
        """
        Make request to API to get additional data for each Pokemon.

        :param number_of_pokemons: Number of pokemons to take.
        :return: Response data.
        """
        return requests.get(endpoint).json()


class Pokemon:
    """Class for Pokemon."""

    def __init__(self, name, experience, attack, defence, types):
        """
        Class constructor.

        :param name: Pokemon's name.
        :param experience: Pokemon's experience
        :param attack: Pokemon's attack level
        :param defence: Pokemon's defence level.
        :param types: Pokemon's types.
        """
        self.types = types
        self.defence = defence
        self.name = name
        self.experience = experience
        self.attack = attack
        self.person = None

    def get_power(self):
        """
        Calculate power of Pokemon.

        :return: Power.
        """
        return (self.experience / self.attack + self.defence) * len(self.name)

    def __str__(self):
        """
        String representation of object.

        :return: Pokemon's name, experience: Pokemon's experience,
        att: Pokemon's attack level, def: Pokemon's defence level, types: Pokemon's types.
        """
        return f"({self.name}, experience: {self.experience}," \
            f" att: {self.attack}, def: {self.defence}, types: {self.types}"

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name
        """
        return self.name


class World:
    """World class."""

    def __init__(self, name):
        """
        Class constructor.

        :param name:
        """
        self.name = name
        self.pokemons = []
        self.people = []
        self.available_pokemons = []

    def add_pokemons(self, number_of_pokemons):
        """Add Pokemons to world, GET data from the API."""
        all_pokemons = Data.get_additional_data(url)
        for i in range(number_of_pokemons):
            new_url = all_pokemons["results"][i]["url"]
            poke = Data.get_additional_data(new_url)
            name = all_pokemons["results"][i]["name"].upper()
            attack = poke["stats"][4]["base_stat"]
            defence = poke["stats"][3]["base_stat"]
            experience = poke["base_experience"]
            types = [type["type"]["name"] for type in poke["types"]]
            pokemon = Pokemon(name, experience, attack, defence, types)
            if pokemon not in self.pokemons:
                self.pokemons.append(pokemon)
                self.available_pokemons.append(pokemon)
        print(self.pokemons)

    def get_pokemons_by_type(self):
        """
        Get Pokemons by type.

        :return: Dict of Pokemons, grouped by types.
        """
        types = {}
        for poke in self.pokemons:
            for type in poke.types:
                if type not in types:
                    types[type] = [poke]
                else:
                    types[type].append(poke)
        return types

    def hike(self, person: Person):
        """
        Person goes to a hike to find a Pokemon.

        :param person: Person who goes to hike.
        """
        if len(self.available_pokemons) == 0:
            raise NoAvailablePokemonsInWorldException("Could not find any pokemons.")
        else:
            pokemon = random.choice(self.available_pokemons)
            person.add_pokemon(pokemon)
            self.remove_available_pokemon(pokemon)

    def remove_available_pokemon(self, pokemon: Pokemon):
        """
        Remove Pokemon from available Pokemons, which means that the Pokemon got a owner.

        :param pokemon: Pokemon to be removed.
        """
        if pokemon in self.available_pokemons:
            self.available_pokemons.remove(pokemon)

    def remove_pokemon_from_world(self, pokemon: Pokemon):
        """
        Remove Pokemon from the world, which means that the Pokemon died.

        :param pokemon: Pokemon to be removed.
        """
        if pokemon.person:
            pokemon.person.remove_pokemon()
            pokemon.person = None
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
        if pokemon in self.available_pokemons:
            self.available_pokemons.remove(pokemon)

    def fight(self, person1: Person, person2: Person):
        """
        Two people fight with their Pokemons.

        :param person1:
        :param person2:
        :return: Pokemon which wins.
        """
        if person1.pokemon.get_power() > person2.pokemon.get_power():
            loser_pokemon = str(person2.pokemon)
            self.remove_pokemon_from_world(person2.pokemon)
            return f"There was a battle between {person1.pokemon} and {loser_pokemon} and the winner was {person1}"
        elif person1.pokemon.get_power() < person2.pokemon.get_power():
            loser_pokemon = str(person1.pokemon)
            self.remove_pokemon_from_world(person1.pokemon)
            return f"There was a battle between {loser_pokemon} and {person2.pokemon} and the winner was {person2}"

    def group_pokemons(self):
        """
        Group Pokemons by given format.

        :return: Dictionary of grouped Pokemons.
        """
        d = {}
        dict_of_groups = {"EARTH": ["poison", "grass", "bug", "ground", "rock"],
                          "FIRE": ["fire", "electric"],
                          "WATER": ["water", "ice"],
                          "AIR": ["flying", "fairy", "ghost"],
                          "OTHER": ["normal", "fighting", "psychic", "steel"]}
        for pokemon in self.pokemons:
            for group in dict_of_groups:
                if pokemon.types[0] in dict_of_groups[group]:
                    if group not in d:
                        d[group] = [pokemon]
                    else:
                        d[group].append(pokemon)
        return d

    def sort_by_type_experience(self):
        """
        Sort Pokemons by type adn experience. The first Pokemons should be Fire type and experience level of under 100.

        :return: List of sorted Pokemons.
        """
        types_order = ["poison", "grass", "bug", "ground", "rock", "fire", "electric", "water",
                       "ice", "flying", "fairy", "ghost", "normal", "fighting", "psychic", "steel"]
        sort_list_1 = []
        sort_list_2 = []
        for pokemon in self.pokemons:
            sortable_element = (pokemon, pokemon.types[0], pokemon.experience)
            if sortable_element[1] == "fire" and sortable_element[2] < 100:
                sort_list_1.append(sortable_element)
            elif (sortable_element[1] == "fire" and sortable_element[2] >= 100) or sortable_element[1] != "fire":
                sortable_element = (pokemon, types_order.index(pokemon.types[0]), pokemon.experience)
                sort_list_2.append(sortable_element)
        sorted_list_1 = sorted(sort_list_1, key=lambda x: (-x[2]))
        sorted_list_2 = sorted(sort_list_2, key=lambda x: (x[1], -x[2]))
        print(sorted_list_1, sorted_list_2)
        sorted_list = sorted_list_1 + sorted_list_2
        return [x[0] for x in sorted_list]

    def get_most_experienced_pokemon(self):
        """Get the Pokemon which has the maximum experience level."""
        return [pokemon for pokemon in self.pokemons if pokemon.experience
                == max(pokemon.experience for pokemon in self.pokemons)]

    def get_min_experience_pokemon(self):
        """Get the Pokemon which has the minimum experience level."""
        return [pokemon for pokemon in self.pokemons if pokemon.experience
                == min(pokemon.experience for pokemon in self.pokemons)]


class Main:
    """Main function."""

    if __name__ == '__main__':
        world = World("Poke land")
        world.add_pokemons(128)
        print(len(world.pokemons))  # -> 128
        print(len(world.get_pokemons_by_type().keys()))  # -> 16
        ago = Person("Ago", 10)
        peeter = Person("Peeter", 11)
        print(len(world.available_pokemons))  # -> 128
        world.hike(ago)
        world.hike(peeter)
        print(len(world.available_pokemons))  # -> 126
        print(world.get_most_experienced_pokemon())  # -> [CHANSEY]
        print(world.get_min_experience_pokemon())  # -> [CATERPIE, WEEDLE]
        print(world.fight(ago, peeter))  # String that says who battled with who and who won.
        print(world.sort_by_type_experience())
