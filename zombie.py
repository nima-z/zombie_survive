
# Enemies Dict
zombie_rat = {"name": "Zombie_rat", "hp": 5, "damage": 2}
zombie_student = {"name": "Zombie_student", "hp": 10, "damage": 5}
normal_zombie = {"name": "Normal_zombie", "hp": 10, "damage": 10}
zombie_nurse = {"name": "Zombie_nurse", "hp": 15, "damage": 10}
zombie_nerd = {"name": "Zombie_nerd", "hp": 15, "damage": 10}
zombie_homeless = {"name": "Zombie_homeless", "hp": 15, "damage": 15}
zombie_runner = {"name": "Zombie_runner", "hp": 20, "damage": 15}
zombie_buyer = {"name": "zombie_buyer", "hp": 20, "damage": 10}
zombie_actress = {"name": "Zombie_actress", "hp": 20, "damage": 15}
zombie_dancer = {"name": "Zombie_dancer", "hp": 25, "damage": 15}
zombie_azi = {"name": "Zombie_azi", "hp": 25, "damage": 20}
zombie_priest = {"name": "Zombie_priest", "hp": 25, "damage": 15}
zombie_worker = {"name": "Zombie_Worker", "hp": 30, "damage": 20}
zombie_prisoner = {"name": "Zombie_prisoner", "hp": 35, "damage": 25}
zombie_dog = {"name": "Zombie_dog", "hp": 40, "damage": 30}
# Places Dict
hospital = {
    "name": "Hospital",
    "item": "nothing",
    "weapon": "steel_pipe",
    "danger": zombie_nurse,
}
police_station = {
    "name": "Police_Station",
    "item": "a battery",
    "weapon": "rifle",
    "danger": zombie_prisoner,
}
gas_station = {
    "name": "Gas_Station",
    "item": "some gas",
    "weapon": "nothing",
    "danger": zombie_worker,
}
park = {
    "name": "Park",
    "item": "nothing",
    "weapon": "stone",
    "danger": zombie_runner,
}
school = {
    "name": "School",
    "item": "nothing",
    "weapon": "baseball_bat",
    "danger": zombie_student,
}
library = {
    "name": "Library",
    "item": "nothing",
    "weapon": "nothing",
    "danger": zombie_nerd,
}
super_market = {
    "name": "Super_Market",
    "item": "some water",
    "weapon": "bottle",
    "danger": zombie_buyer,
}
church = {
    "name": "Church",
    "item": "nothing",
    "weapon": "nothing",
    "danger": zombie_priest,
}
theater = {
    "name": "Theater",
    "item": "a wire",
    "weapon": "nothing",
    "danger": zombie_actress,
}
garage = {
    "name": "Garage",
    "item": "a tire",
    "weapon": "nothing",
    "danger": zombie_rat,
}
home = {
    "name": "Home",
    "item": "nothing",
    "weapon": "spoon",
    "danger": "no_one",
}
metro_station = {
    "name": "Metro_Station",
    "item": "nothing",
    "weapon": "knife",
    "danger": zombie_homeless,
}
azi_house = {
    "name": "Azi_House",
    "item": "some oil",
    "weapon": "nothing",
    "danger": zombie_azi,
}
pet_shop = {
    "name": "Pet_Shop",
    "item": "nothing",
    "weapon": "nothing",
    "danger": zombie_dog,
}
club = {
    "name": "Club",
    "item": "nothing",
    "weapon": "pistole",
    "danger": zombie_dancer,
}
coffee_house = {
    "name": "Coffee_House",
    "item": "nothing",
    "weapon": "bottle",
    "danger": normal_zombie,
}
# City Map
citydict = [
    [hospital, police_station, gas_station, park],
    [school, library, super_market, church],
    [theater, garage, home, metro_station],
    [azi_house, pet_shop, club, coffee_house],
]
# Weapons
weapons = {
    "nothing": 0,
    "spoon": 2,
    "stone": 5,
    "bottle": 7,
    "baseball_bat": 10,
    "steel_pipe": 13,
    "knife": 15,
    "pistole": 20,
    "rifle": 30,
}
# Starting Location : Home
x = 2
y = 2
locationdict = citydict[x][y]
player = {"hp": 100}
player_items = []
# Introduction
print("This is a survival game and you only need to type 'yes' or 'no'.")
next_line = input("type any character:  ")
print(
    "You have to leave the city, because of zombies. you have a car but it is broken."
)
next_line = input("type any character:  ")
print("You need 6 items to fix your car, but those are in 6 different places.")
print("Remember, your car is at your place, collect them and return home.")
next_line = input("type any character:  ")
print("you can find weapons and use them to kill zombies.")
next_line = input("type any character to start the game:  ")
# Game play
while player["hp"] > 0:
    # Determin new location
    locationdict = citydict[x][y]
    # win and endgame code
    if (len(player_items) == 6) and (locationdict["name"] == "Home"):
        print("==========================")
        print(
            "You have all 6 items and you are at Home, now you can fix your car and run"
        )
        print("You Won The Game, CONGRATS")
        break
    # print current status
    print(
        "You are in '%s'. There is '%s' as a weapon and '%s' as an item."
        % (locationdict["name"], locationdict["weapon"], locationdict["item"])
    )
    # select weapon
    if locationdict["weapon"] != "nothing":
        take_weapon = input(
            "Do you want to pick up '%s' with [power: %s] ? "
            % (locationdict["weapon"], weapons[locationdict["weapon"]])
        )
        if take_weapon.lower() == "yes":
            player["weapon"] = locationdict["weapon"]
            print(
                "Now, You have '%s' with [power: %s]"
                % (locationdict["weapon"], weapons[locationdict["weapon"]])
            )
            locationdict["weapon"] = "nothing"
    # Fight and pick item
    if locationdict["danger"] != "no_one":
        print("But you need to fight before taking any item.")
        print("your enemy's stat is : ", locationdict["danger"])
        fight_danger = input("Do you want to fight?")
        if fight_danger.lower() == "yes":
            while (locationdict["danger"])["hp"] > 0:
                if player["hp"] <= 0:  # game over checker (2nd while)
                    print("unfortunatly you died")
                    print("Game Over")
                    break
                (locationdict["danger"])["hp"] -= weapons[player["weapon"]]
                if (locationdict["danger"])["hp"] <= 0:
                    if locationdict["item"] != "nothing":
                        player.get("items", 0) + 1
                        player_items.append(locationdict["item"])
                    print("you killed a '%s', and after this fight, your stat is :"% ((locationdict["danger"])["name"]))
                    print(player, "/// your items are : ", player_items)
                    locationdict["item"] = "nothing"
                    locationdict["danger"] = "no_one"
                    break
                else:
                    player["hp"] -= (locationdict["danger"])["damage"]
    # Move
    move = input("which way?")
    if move == "left":
        y -= 1
        if y == -1:
            print("There is a wall because you are at the most left in the map")
            y = 0
            continue
    elif move == "right":
        y += 1
        if y == 4:
            print("There is a wall because you are at the most right in the map")
            y = 3
            continue
    elif move == "up":
        x -= 1
        if x == -1:
            print("There is a wall because you are at the most up in the map")
            x = 0
            continue
    elif move == "down":
        x += 1
        if x == 4:
            print("There is a wall because you are at the most down in the map")
            x = 3
            continue
    else:
        print("Please Type Again")