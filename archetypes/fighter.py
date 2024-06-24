import modules.equipment as equipment

displayed_fighter_skills = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
fighter_skills = ["acrobatics", "animal handling", "athletics", "history", "insight", "intimidation", "perception", "survival"]

class Fighter:
    
    def __init__(self):
        name = "Fighter"
        description = "A master of martial combat, skilled with a variety of weapons and armor"
        hit_die = "1d10 for first level, then 1d10 (or 6, whichever is higher) per level after 1 + your Constitution modifier."
        primary_ability = "Strength or Dexterity"
        saving_throw_proficiencies = "Strength, Constitution"
        armor_proficiencies = "All Armor, Shields"
        weapon_proficiencies = "All Simple Weapons and Martial Weapons"
        tool_proficiencies = "None"
        skill_proficiencies = []
        potential_starting_equipment = ["Chain Mail or Leather Armor, Longbow, and 20 Arrows", "Any Martial Weapon and a Shield or Two Martial Weapons", "Light Crossbow and 20 Bolts or Two Handaxes", "Dungeoneer's Pack or Explorer's Pack"]
        special_abilities = []
        self.name = name
        self.description = description
        self.hit_die = hit_die
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = skill_proficiencies
        self.potential_starting_equipment = potential_starting_equipment
        self.starting_equipment = []
        self.special_abilities = special_abilities

    def get_info(self):
        print(f"The {self.name}: {self.description}")
        print(f"Hit Die: {self.hit_die}")
        print(f"Primary Ability: {self.primary_ability}")
        print(f"Saving Throw Proficiencies: {self.saving_throw_proficiencies}")
        print(f"Armor Proficiencies: {self.armor_proficiencies}")
        print(f"Weapon Proficiencies: {self.weapon_proficiencies}")
        print(f"Tool Proficiencies: {self.tool_proficiencies}")
        print(f"Skill Proficiencies: {self.displayed_skill_proficiencies}")
        print(f"Starting Equipment: {self.potential_starting_equipment}")
        print(f"Special Abilities: {self.special_abilities}")
        return self
    
    def update_special_abilities(self, level):
        if level >= 1:
            self.special_abilities.append("Fighting Style")
            self.special_abilities.append("Second Wind")
        if level >= 2:
            self.special_abilities.append("Action Surge (1 use)")
        if level >= 3:
            self.special_abilities.append("Martial Archetype")
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Extra Attack (1)")
        if level >= 6:
            self.special_abilities.append("Ability Score Improvement 6th Level")
        if level >= 7:
            self.special_abilities.append("Martial Archetype Feature")
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.special_abilities.append("Indomitable (1 use)")
        if level >= 10:
            self.special_abilities.append("Martial Archetype Feature")
        if level >= 11:
            self.special_abilities.append("Extra Attack (2)")
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.special_abilities.append("Indomitable (2 uses)")
        if level >= 14:
            self.special_abilities.append("Ability Score Improvement 14th Level")
        if level >= 15:
            self.special_abilities.append("Martial Archetype Feature")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.special_abilities.append("Action Surge (2 uses)")
            self.special_abilities.append("Indomitable (3 uses)")
        if level >= 18:
            self.special_abilities.append("Martial Archetype Feature")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Extra Attack (3)")

def define_fighter():
    fighter = Fighter()
    print("You have chosen the Fighter class.")
    print(fighter.bio)

    # Skill Proficiencies
    print("Choose two skills from the following list:")
    for skill in displayed_fighter_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in fighter_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    fighter.skill_proficiencies.append(skill_choice1)

    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in fighter_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    fighter.skill_proficiencies.append(skill_choice2)

    print("You have chosen the following skills:")
    for skill in fighter.skill_proficiencies:
        print(skill)

    # Starting Equipment
    equipment_choice1 = ""
    equipment_choice2 = ""
    equipment_choice3 = ""
    equipment_choice4 = ""
    print("Choose your starting equipment:")
    for option in fighter.potential_starting_equipment:
        print(option)

    print("Please enter your choice of 'Chain Mail' or 'Leather Armor, Longbow, and 20 Arrows':")
    equipment_choice1 = input("> ")
    while equipment_choice1.lower() not in ["chain mail", "leather armor, longbow, and 20 arrows"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice1 = input("> ")
    if equipment_choice1.lower() == "chain mail":
        fighter.starting_equipment.append(equipment.chain_mail_heavy_armor)
    else:
        fighter.starting_equipment.append(equipment.leather_light_armor)
        fighter.starting_equipment.append(equipment.longbow)
        # Need to add 20 arrows here.

    print("Please enter your choice of 'Any Martial Weapon and a Shield' or 'Two Martial Weapons':")
    equipment_choice2 = input("> ")
    while equipment_choice2.lower() not in ["any martial weapon and a shield", "two martial weapons"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice2 = input("> ")
    if equipment_choice2.lower() == "any martial weapon and a shield":
        for weapon in equipment.martial_weapons:
            print(weapon.name)
        print("Please enter your choice of martial weapon:")
        weapon_choice = input("> ")
        while weapon_choice.lower() not in [weapon.name.lower() for weapon in equipment.martial_weapons]:
            print("That is not a valid choice. Please choose from the list.")
            weapon_choice = input("> ")
        for weapon in equipment.martial_weapons:
            if weapon_choice.lower() == weapon.name.lower():
                fighter.starting_equipment.append(weapon)
                break
        fighter.starting_equipment.append(equipment.shield)

    else:
        for weapon in equipment.martial_weapons:
            print(weapon.name)
        print("Please enter your choice of first martial weapon:")
        weapon_choice1 = input("> ")
        while weapon_choice1.lower() not in [weapon.name.lower() for weapon in equipment.martial_weapons]:
            print("That is not a valid choice. Please choose from the list.")
            weapon_choice1 = input("> ")
        for weapon in equipment.martial_weapons:
            if weapon_choice1.lower() == weapon.name.lower():
                fighter.starting_equipment.append(weapon)
                break

        print("Please enter your choice of second martial weapon:")
        weapon_choice2 = input("> ")
        while weapon_choice2.lower() not in [weapon.name.lower() for weapon in equipment.martial_weapons]:
            print("That is not a valid choice. Please choose from the list.")
            weapon_choice2 = input("> ")
        for weapon in equipment.martial_weapons:
            if weapon_choice2.lower() == weapon.name.lower():
                fighter.starting_equipment.append(weapon)
                break

    print("Please enter your choice of 'Light Crossbow and 20 Bolts' or 'Two Handaxes':")
    equipment_choice3 = input("> ")
    while equipment_choice3.lower() not in ["light crossbow and 20 bolts", "two handaxes"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice3 = input("> ")
    if equipment_choice3.lower() == "light crossbow and 20 bolts":
        fighter.starting_equipment.append(equipment.light_crossbow)
        # Need to add 20 bolts here.
    else:
        fighter.starting_equipment.append(equipment.hand_axe)
        fighter.starting_equipment.append(equipment.hand_axe)
    
    print("Please enter your choice of 'Dungeoneer's Pack' or 'Explorer's Pack':")
    equipment_choice4 = input("> ")
    while equipment_choice4.lower() not in ["dungeoneer's pack", "explorer's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice4 = input("> ")
    if equipment_choice4.lower() == "dungeoneer's pack":
        fighter.starting_equipment.append(equipment.dungeoneers_pack)
    else:
        fighter.starting_equipment.append(equipment.explorers_pack)

    print(f"You have chosen the following starting equipment:")
    for item in fighter.starting_equipment:
        print(item.name)

    return fighter