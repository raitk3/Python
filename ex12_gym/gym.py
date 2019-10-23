"""Gym."""


class Trainers:
    """Member."""

    def __init__(self, stamina: int, color: str):
        """Init."""
        self.stamina = stamina
        self.color = color

    def __repr__(self):
        """Repr."""
        return f"Trainers: [{self.stamina}, {self.color}]"


class Member:
    """Member."""

    def __init__(self, name: str, age: int, trainers: Trainers):
        """Init."""
        self.name = name
        self.age = age
        self.trainers = trainers
        self.member_gyms = []

    def __repr__(self):
        """Repr."""
        return f"{self.name}, {self.age}: {self.trainers}"

    def get_gyms(self) -> list:
        """Return list of member object gyms."""
        return self.member_gyms


class Gym:
    """Gym."""

    def __init__(self, name: str, max_members_number: int):
        """Init."""
        self.name = name
        self.max_members = max_members_number
        self.members = []

    def can_add_member(self, member: Member):
        """Check if member can be added."""
        return member.trainers.stamina >= 0 and member.trainers.color

    def add_member(self, member: Member):
        """Add a member to the members."""
        if member not in self.members and isinstance(member, Member) and self.can_add_member(member):
            if len(self.members) == self.max_members:
                min_stamina = -1
                for current_member in self.members:
                    if min_stamina == -1 or current_member.trainers.stamina < min_stamina:
                        min_stamina = current_member.trainers.stamina
                for _ in range(len(self.members)):
                    for current_member in self.members:
                        if current_member.trainers.stamina == min_stamina:
                            self.members.remove(current_member)
            self.members.append(member)
            return member

    def remove_member(self, member: Member):
        """Remove member."""
        if member in self.members:
            self.members.remove(member)

    def get_total_stamina(self) -> int:
        """Get total stamina of every trainer."""
        total_stamina = 0
        for member in self.members:
            total_stamina += member.trainers.stamina
        return total_stamina

    def get_members_number(self) -> int:
        """Get amount of members."""
        return len(self.members)

    def get_all_members(self) -> list:
        """Get all members."""
        return self.members

    def get_average_age(self) -> float:
        """Calculate average age of members."""
        if len(self.members) > 0:
            members_ages = []
            for member in self.members:
                members_ages.append(member.age)
            return sum(members_ages) / len(members_ages)

    def __repr__(self):
        """Repr."""
        return f"Gym {self.name} : {len(self.members)} member(s)"


class City:
    """Town."""

    def __init__(self, max_gym_number: int):
        """A maximum amount of gyms in city."""
        self.max_gym_number = max_gym_number
        self.gyms = []

    def can_build_gym(self) -> bool:
        """Can build a gym."""
        return len(self.gyms) < self.max_gym_number

    def build_gym(self, gym: Gym):
        """Build a gym."""
        if self.can_build_gym():
            self.gyms.append(gym)
            return gym

    def destroy_gym(self):
        """Destroy smallest gym."""
        if len(self.gyms) > 0:
            minimum_members = -1
            for gym in self.gyms:
                if minimum_members == -1 or gym.members < minimum_members:
                    minimum_members = gym.members
            for gym in self.gyms:
                if gym.members == minimum_members:
                    self.gyms.remove(gym)

    def get_max_members_gym(self) -> list:
        """Return gym with most members."""
        if len(self.gyms) > 0:
            max_members = 0
            max_gym = []
            for gym in self.gyms:
                if len(gym.members) > max_members:
                    max_gym = list()
                    max_gym.append(gym)
                    max_members = len(gym.members)
                elif len(gym.members) == max_members:
                    max_gym.append(gym)
            return max_gym

    def get_max_stamina_gyms(self) -> list:
        """Return gym with highest stamina."""
        if len(self.gyms) > 0:
            max_stamina = 0
            max_gym = []
            for gym in self.gyms:
                temp_stamina = 0
                for member in gym.members:
                    temp_stamina += member.trainers.stamina
                if temp_stamina > max_stamina:
                    max_stamina = temp_stamina
                    max_gym = [gym]
                elif temp_stamina == max_stamina:
                    max_gym.append(gym)
            return max_gym

    def get_max_average_ages(self) -> list:
        """Return gym with highest avg ages."""
        highest_avg = 0
        highest_gym = []
        for gym in self.gyms:
            temp_age = 0
            for member in gym.members:
                temp_age += member.age
            temp_avg = temp_age / len(gym.members)
            if temp_avg > highest_avg:
                highest_avg = temp_avg
                highest_gym = [gym]
            elif temp_avg == highest_avg:
                highest_gym.append(gym)
        return highest_gym

    def get_min_average_ages(self) -> list:
        """Return gym with lowest avg ages."""
        minimum_avg = -1
        minimum_gym = []
        for gym in self.gyms:
            temp_age = 0
            for member in gym.members:
                temp_age += member.age
            temp_avg = temp_age / len(gym.members)
            if temp_avg < minimum_avg or minimum_avg == -1:
                minimum_avg = temp_avg
                minimum_gym = [gym]
            elif temp_avg == minimum_avg:
                minimum_gym.append(gym)
        return minimum_gym

    def get_gyms_by_trainers_color(self, color: str) -> list:
        """Get gyms by trainers color."""
        gyms = {}
        for gym in self.gyms:
            match_count = 0
            for member in gym.members:
                if member.trainers.color == color:
                    match_count += 1
            if match_count > 0:
                gyms[gym] = match_count
        gyms_list = sorted(gyms.items(), key=lambda x: x[1], reverse=True)
        gyms_final = []
        for el in gyms_list:
            gyms_final. append(el[0])
        return gyms_final

    def get_gyms_by_name(self, name: str) -> list:
        """Get gyms by trainers color."""
        gyms = {}
        for gym in self.gyms:
            match_count = 0
            for member in gym.members:
                if member.name == name:
                    match_count += 1
            if match_count > 0:
                gyms[gym] = match_count
        gyms_list = sorted(gyms.items(), key=lambda x: x[1], reverse=True)
        gyms_final = []
        for el in gyms_list:
            gyms_final. append(el[0])
        return gyms_final

    def get_all_gyms(self) -> list:
        """Return all the gyms."""
        return self.gyms


if __name__ == "__main__":
    city1 = City(100)
    gym = Gym("TTÜ Sport", 50)
    city1.build_gym(gym)

    trainers1 = Trainers(50, "blue")
    trainers2 = Trainers(50, "grey")

    member = Member("Ago Luberg", 35, trainers1)
    member2 = Member("Ahti Lohk", 35, trainers2)

    gym.add_member(member)
    gym.add_member(member2)

    print(gym.get_members_number())  # 2

    print(gym.get_all_members())  # [Ago Luberg, 35: Trainers: [50, blue], Ahti Lohk, 35: Trainers: [50, grey]]

    gym.add_member(member)  # Trying to add Ago again
    print(gym.get_members_number())  # 2 //We can't...

    for i in range(48):
        gym.add_member(Member("Tudeng Tudeng", 20, Trainers(49, "blue")))

    print(gym.get_members_number())  # 50

    trainers3 = Trainers(60, "blue")
    member_new = Member("Megane", 19, trainers3)
    gym.add_member(member_new)

    print(
        gym.get_members_number())  # 3 -> Ago, Ahti and Megan, all others were removed because of the lowest trainers' stamina

    city2 = City(10)
    city2.build_gym(Gym("MyFitness", 100))
    city2.destroy_gym()

    for i in range(9):
        city2.build_gym(Gym("Super Gym", 10))

    print(city2.can_build_gym())  # False -> Cannot build gym, city is full of them

    #######################################################################################

    city3 = City(100)

    gym4 = Gym("Sparta", 50)
    gym5 = Gym("People Fitness", 30)
    gym6 = Gym("Gym Eesti", 100)

    city3.build_gym(gym4)
    city3.build_gym(gym5)
    city3.build_gym(gym6)

    gym4.add_member(Member("Bob", 18, Trainers(50, "black")))
    gym4.add_member(Member("Emma", 20, Trainers(70, "red")))
    gym4.add_member(Member("Ken", 25, Trainers(40, "grey")))

    gym5.add_member(Member("Merili", 18, Trainers(100, "pink")))
    gym5.add_member(Member("Richard", 20, Trainers(70, "green")))

    gym6.add_member(Member("Bella", 40, Trainers(15, "green")))
    gym6.add_member(Member("Bob", 50, Trainers(70, "green")))
    gym6.add_member(Member("Sandra", 25, Trainers(30, "pink")))
    gym6.add_member(Member("Bob", 35, Trainers(50, "black")))

    city3.get_max_members_gym()  # [Gym Gym Eesti : 4 member(s)]
    city3.get_max_stamina_gyms()  # [Gym People Fitness : 2 member(s)]
    city3.get_max_average_ages()  # [Gym Gym Eesti : 4 member(s)] => average age 37,5
    city3.get_min_average_ages()  # [Gym People Fitness : 2 member(s)] => average age 19
    print(city3.get_gyms_by_trainers_color(
        "green"))  # [Gym Gym Eesti : 4 member(s), Gym People Fitness : 2 member(s)] => Gym Eesti has 2 members with green trainers, People Fitness has 1.
    print(city3.get_gyms_by_name(
        "Bob"))  # [Gym Gym Eesti : 4 member(s), Gym Sparta : 3 member(s)] => Gym Eesti has 2 members with name Bob, Sparta has 1.
