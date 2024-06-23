import modules.character as character
import modules.utils as utils
import modules.equipment as equipment
import modules.races as races
import modules.archetypes as archetypes


def character_creation():
    print("Greetings traveler! Welcome to the world of D&D!")
    print("What is your character's name?")
    name = input("> ")
    print(f"Hello, {name}!")

    race = None
    print("Please choose your character's race from the following list:")
    races.display_races()
    while race == None:
        print("Which race is your character?")
        race_choice = input("> ")
        for race_option in races.get_races():
            if race_choice.lower() == race_option.lower():
                race = race_option
        if race == None:
            print("Sorry, that is not a valid race. Please try again.")
        


    archetype = None
    print("Great! Now please choose an class from the following list:")
    archetypes.display_archetypes()
    while archetype == None:
        print("Which class is your character?")
        archetype_choice = input("> ")
        for archetype_option in archetypes.get_archetypes():
            if archetype_choice.lower() == archetype_option.lower():
                archetype = archetype_option
        if archetype == None:
            print("Sorry, that is not a valid class. Please try again.")
    
    

    print(f"Awesome! Your character is called {name}, a {race} {archetype}.")

    xp = 0

    gp = utils.calculate_starting_gp(archetype)

    print(f"{name} has {gp} gold pieces.")

    print(f"Tell me about {name}'s background story.")
    bio = input("> ")

    abilities = {}

    abilities["Strength"] = utils.roll_ability()
    abilities["Dexterity"] = utils.roll_ability()
    abilities["Constitution"] = utils.roll_ability()
    abilities["Intelligence"] = utils.roll_ability()
    abilities["Wisdom"] = utils.roll_ability()
    abilities["Charisma"] = utils.roll_ability()

    print(f"Here are {name}'s abilities: ")
    for ability, value in abilities.items():
        print(f"{ability}: {value}") 

    player_equipment = []
    print("Now it is time to choose your character's equipment!")
    equipment_loop = True
    while equipment_loop:
        print(f"{name} currently has the following equipment:")
        for item in player_equipment:
            print(item.name)
        print(f"{name} has {gp} gold pieces.")
        if gp < 1:
            print(f"{name} does not have enough gold pieces to buy more equipment.")
            equipment_loop = False
            break
        print("Would you like to buy additional equipment? (yes/no)")
        buy_equipment = input("> ")
        if buy_equipment.lower() == "no":
            equipment_loop = False
            break
        print("Please choose equipment from the following list:")
        for equipment_type in equipment.equipment_types:
            print(equipment_type)
        equipment_choice = input("> ")
        if equipment_choice == "cancel":
            break
        equipment_types_lower = [equipment.lower() for equipment in equipment.equipment_types]
        while equipment_choice.lower() not in equipment_types_lower:
            print("Sorry, that is not a valid equipment type. Please try again.")
            equipment_choice = input("> ")
        if equipment_choice.lower() == "simple weapons":
            print("Please choose a weapon from the following list:")
            for weapon in equipment.simple_weapons:
                print(weapon.name)
            weapon_choice = input("> ")
            if weapon_choice == "cancel":
                    break
            simple_weapons_lower = [weapon.name.lower() for weapon in equipment.simple_weapons]
            while weapon_choice not in simple_weapons_lower:
                print("Sorry, that is not a valid weapon. Please try again.")
                weapon_choice = input("> ")
                if weapon_choice == "cancel":
                    break
            for weapon in equipment.simple_weapons:
                if weapon_choice.lower() == weapon.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {weapon.name} costs {weapon.cost} gold pieces.")
                    if gp < weapon.cost:
                        print(f"{name} does not have enough gold pieces to buy the {weapon.name}.")
                        break
                    else:
                        player_equipment.append(weapon)
                        gp -= weapon.cost
                        print(f"{name} now has {gp} gold pieces and a new {weapon.name}.")
        elif equipment_choice.lower() == "martial weapons":
            print("Please choose a weapon from the following list:")
            for weapon in equipment.martial_weapons:
                print(weapon.name)
            weapon_choice = input("> ")
            if weapon_choice == "cancel":
                    break
            martial_weapons_lower = [weapon.name.lower() for weapon in equipment.martial_weapons]
            while weapon_choice not in martial_weapons_lower:
                print("Sorry, that is not a valid weapon. Please try again.")
                weapon_choice = input("> ")
                if weapon_choice == "cancel":
                    break
            for weapon in equipment.martial_weapons:
                if weapon_choice.lower() == weapon.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {weapon.name} costs {weapon.cost} gold pieces.")
                    if gp < weapon.cost:
                        print(f"{name} does not have enough gold pieces to buy the {weapon.name}.")
                        break
                    else:
                        player_equipment.append(weapon)
                        gp -= weapon.cost
                        print(f"{name} now has {gp} gold pieces and a new {weapon.name}.")
        elif equipment_choice.lower() == "light armor":
            print("Please choose armor from the following list:")
            for armor in equipment.light_armor:
                print(armor.name)
            armor_choice = input("> ")
            if armor_choice == "cancel":
                    break
            light_armor_lower = [armor.name.lower() for armor in equipment.light_armor]
            while armor_choice not in light_armor_lower:
                print("Sorry, that is not valid armor. Please try again.")
                armor_choice = input("> ")
                if armor_choice == "cancel":
                        break
            for armor in equipment.light_armor:
                if armor_choice.lower() == armor.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {armor.name} costs {armor.cost} gold pieces.")
                    if gp < armor.cost:
                        print(f"{name} does not have enough gold pieces to buy the {armor.name}.")
                        break
                    else:
                        player_equipment.append(armor)
                        gp -= armor.cost
                        print(f"{name} now has {gp} gold pieces and new {armor.name}.")
        elif equipment_choice.lower() == "medium armor":
            print("Please choose armor from the following list:")
            for armor in equipment.medium_armor:
                print(armor.name)
            armor_choice = input("> ")
            if armor_choice == "cancel":
                    break
            medium_armor_lower = [armor.name.lower() for armor in equipment.medium_armor]
            while armor_choice not in medium_armor_lower:
                print("Sorry, that is not valid armor. Please try again.")
                armor_choice = input("> ")
                if armor_choice == "cancel":
                        break
            for armor in equipment.medium_armor:
                if armor_choice.lower() == armor.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {armor.name} costs {armor.cost} gold pieces.")
                    if gp < armor.cost:
                        print(f"{name} does not have enough gold pieces to buy the {armor.name}.")
                        break
                    else:
                        player_equipment.append(armor)
                        gp -= armor.cost
                        print(f"{name} now has {gp} gold pieces and new {armor.name}.")
        elif equipment_choice.lower() == "heavy armor":
            print(f"Please choose armor from the following list:")
            for armor in equipment.heavy_armor:
                print(armor.name)
            armor_choice = input("> ")
            if armor_choice == "cancel":
                    break
            heavy_armor_lower = [armor.name.lower() for armor in equipment.heavy_armor]
            while armor_choice not in heavy_armor_lower:
                print("Sorry, that is not valid armor. Please try again.")
                armor_choice = input("> ")
                if armor_choice == "cancel":
                        break
            for armor in equipment.heavy_armor:
                if armor_choice.lower() == armor.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {armor.name} costs {armor.cost} gold pieces.")
                    if gp < armor.cost:
                        print(f"{name} does not have enough gold pieces to buy the {armor.name}.")
                        break
                    else:
                        player_equipment.append(armor)
                        gp -= armor.cost
                        print(f"{name} now has {gp} gold pieces and new {armor.name}.")
        elif equipment_choice.lower() == "shield":
            print(f"The {equipment.shield.name} costs {equipment.shield.cost} gold pieces.")
            print(f"Please confirm {name} would like a shield: (yes/no)")
            shield_choice = input("> ")
            while shield_choice.lower() not in ["yes", "no"]:
                print("Sorry, that is not a valid choice. Please try again.")
                print(f"The {equipment.shield.name} costs {equipment.shield.cost} gold pieces.")
                print(f"Please confirm {name} would like a shield: (yes/no)")
                shield_choice = input("> ")
            if shield_choice == "no":
                break
            elif shield_choice == "yes":
                print(f"{name} has {gp} gold pieces.")
                print(f"The {equipment.shield.name} costs {equipment.shield.cost} gold pieces.")
                if gp < equipment.shield.cost:
                    print(f"{name} does not have enough gold pieces to buy the {equipment.shield.name}.")
                    break
                else:
                    player_equipment.append(equipment.shield)
                    gp -= equipment.shield.cost
                    print(f"{name} now has {gp} gold pieces and a new {equipment.shield.name}.")

    player = character.Character(name, race, archetype, bio, player_equipment, abilities, xp, gp)

    print(player.greet())
    print(player.get_info())
    print(player.get_bio())
    print(f"{name} has the following equipment items:")
    for item in player.get_equipment():
        print(item.name)
    print(f"{name} has the following abilities:")
    for ability, value in player.get_abilities().items():
        print(f"{ability}: {value}")
    print(f"{name} has {player.get_gp()} gold pieces.")
    print(player.get_xp())
    print(player.xp_needed_for_next_level())