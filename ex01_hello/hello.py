"""kuskil on astendamine, seega..."""
import math
name = input("What's your name?:")
"""kaastundeng näitas, et whilega saab loopida, seega kasutan õpitut siin."""
while name == "":
        print("Name was not inserted!")
        name = input("What's your name?:")
school = input("Where do you study?:")
while school == "":
    print("School was not inserted!")
    school = input("Where do you study?:")
print(name + ", welcome to " + school + "!")
"""Kuna mul viisakusest on vajaka, küsin suht otse vist?."""
weight = input("How much do you weigh (in kilograms)?")
while weight == "":
    print("Weight was not inserted!")
    weight = input("How much do you weigh (in kilograms)?")
height = input("How tall are you (in meters)?")
while height == "":
    print("Height was not inserted!")
    height = input("How tall are you (in meters)?")
"""Kuna arvutused toimuvad arvude, mitte tekstidega..."""
weight = float(weight)
height = float(height)
"""kiired arvutused...ennäe, siin oli math-i vaja."""
index = f'{weight / math.pow(height,2)}'
"""miskipärast ümardab kenasti vaid floate, huvitav küll, miks?."""
index = float(index)
"""Ümardamine on lihtsalt mõistlik, parem lugeda ning 23.44 on parem silmale kui 23.437499999999996."""
index = round(index, 1)
if index < 18.5:
    print(str(index) + ", alakaaluline")
elif index > 25.0:
    print(str(index) + ", ülekaaluline")
else:
    print(str(index) + ", normaalkaal")
