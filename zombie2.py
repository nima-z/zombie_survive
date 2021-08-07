class Zombie:

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

z1 = Zombie("Zombie_rat", 5, 2)
z2 = Zombie("Zombie_student", 10, 5)
z3 = Zombie("Zombie_nurse", 10, 10)
z4 = Zombie("Zombie_nerd", 15, 10)
z5 = Zombie("Zombie_homeless", 15, 10)
z6 = Zombie("Zombie_runner", 15, 15)
z7 = Zombie("Zombie_buyer", 20, 15)
z8 = Zombie("Zombie_actress", 20, 10)
z9 = Zombie("Zombie_dancer", 25, 15)
z10 = Zombie("Zombie_priest", 25, 15)
z11 = Zombie("Zombie_worker", 25, 20)
z12 = Zombie("Zombie_prisoner", 30, 20)
z13 = Zombie("Zombie_dog", 35, 25)
z14 = Zombie("Normal_zombie", 40, 30)


class place:
    
    def __init__(self, name, item, weapon, danger):
        self.name = name
        self.item = item
        self.weapon = weapon
        self.danger = danger

p1 = place("Hospital", "nothing", "Steel pipe", z3.name)
p2 = place("Police_station", "Battery", "Rifle", z12.name)
p3 = place("Gas_station", "Some Gas", "Nothing", z11.name)
p4 = place("Park", "nothing", "Stone", z6.name)
p5 = place("Library", "nothing", "Nothing", z4.name)
p6 = place("Super_market", "Some Water", "Bottle", z7.name)
p7 = place("Church", "nothing", "Nothing", z10.name)
p8 = place("Theater", "Wire", "Nothing", z8.name)
p9 = place("Garage", "Tire", "Nothing", z1.name)
p10 = place("Home", "nothing", "Spoon", "No one")
p11 = place("Metro_station", "nothing", "Knife", z5.name)
p12 = place("Azi_house", "Some Oil", "Nothing", "No one")
p13 = place("Pet_shop", "nothing", "Nothing", z13.name)
p14 = place("Club", "nothing", "Pistole", z9.name)
p15 = place("Coffe_house", "nothing", "Nothing", z14.name)
p16 = place("School", "nothing", "Baseball Bat", z2.name)


citydict = [
    [hospital, police_station, gas_station, park],
    [school, library, super_market, church],
    [theater, garage, home, metro_station],
    [azi_house, pet_shop, club, coffee_house],