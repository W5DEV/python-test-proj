import modules.equipment as equipment

def starting_equipment_choice(choice_1, choice_2):
    print(f"Please choose one of either {choice_1} or {choice_2}.")
    print("> ", end="")
    choice = input()
    while choice.lower() not in [choice_1.lower(), choice_2.lower()]:
        print("Sorry, that is not a valid choice. Please try again.")
        print("> ", end="")
        choice = input()
    return choice

def select_equipment_from_category(category):
    valid_choices = []
    equipment_category = None
    print(f"Please choose one {category}:")
    if category == "Simple Melee Weapons":
        for weapon in equipment.simple_melee_weapons:
            print(weapon)
            valid_choices.append(weapon.name.lower())
        equipment_category = equipment.simple_melee_weapons
    if category == "Simple Ranged Weapons":
        for weapon in equipment.simple_ranged_weapons:
            print(weapon)
            valid_choices.append(weapon.name.lower())
        equipment_category = equipment.simple_ranged_weapons
    if category == "Simple Weapons":
        for weapon in equipment.simple_weapons:
            print(weapon)
            valid_choices.append(weapon.name.lower())
        equipment_category = equipment.simple_weapons
    if category == "Martial Melee Weapons":
        for weapon in equipment.martial_melee_weapons:
            print(weapon)
            valid_choices.append(weapon.name.lower())
        equipment_category = equipment.martial_melee_weapons
    if category == "Martial Ranged Weapons":
        for weapon in equipment.martial_ranged_weapons:
            print(weapon)
            valid_choices.append(weapon.name.lower())
        equipment_category = equipment.martial_ranged_weapons
    if category == "Martial Weapons":
        for weapon in equipment.martial_weapons:
            print(weapon)
            valid_choices.append(weapon.name.lower())
        equipment_category = equipment.martial_weapons
    if category == "Light Armor":
        for armor in equipment.light_armor:
            print(armor)
            valid_choices.append(armor.name.lower())
        equipment_category = equipment.light_armor
    if category == "Medium Armor":
        for armor in equipment.medium_armor:
            print(armor)
            valid_choices.append(armor.name.lower())
        equipment_category = equipment.medium_armor
    if category == "Heavy Armor":
        for armor in equipment.heavy_armor:
            print(armor)
            valid_choices.append(armor.name.lower())
        equipment_category = equipment.heavy_armor
    if category == "Shield":
        for shield in equipment.shields:
            print(shield)
            valid_choices.append(shield.name.lower())
        equipment_category = equipment.shields
    if category == "Instruments":
        for instrument in equipment.instruments:
            print(instrument)
            valid_choices.append(instrument.name.lower())
        equipment_category = equipment.instruments
    if category == "Packs":
        for pack in equipment.packs:
            print(pack)
            valid_choices.append(pack.name.lower())
        equipment_category = equipment.packs
    if category == "Instruments":
        for instrument in equipment.instruments:
            print(instrument)
            valid_choices.append(instrument.name.lower())
        equipment_category = equipment.instruments
    if category == "Holy Symbols":
        for symbol in equipment.holy_symbols:
            print(symbol)
            valid_choices.append(symbol.name.lower())
        equipment_category = equipment.holy_symbols
    if category == "Artisan's Tools":
        for tool in equipment.artisan_tools:
            print(tool)
            valid_choices.append(tool.name.lower())
        equipment_category = equipment.artisan_tools
    if category == "Other Tools":
        for tool in equipment.other_tools:
            print(tool)
            valid_choices.append(tool.name.lower())
        equipment_category = equipment.other_tools
    if category == "Class Equipment":
        for item in equipment.class_equipment:
            print(item)
            valid_choices.append(item.name.lower())
        equipment_category = equipment.class_equipment
    user_choice = input("> ")
    while user_choice.lower() not in valid_choices:
        print("Sorry, that is not a valid choice. Please try again.")
        user_choice = input("> ")
    for item in equipment_category:
        if user_choice.lower() == item.name.lower():
            return item
        
def starting_equipment(item):
    for equip_item in equipment.simple_weapons:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.martial_weapons:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.light_armor:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.medium_armor:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.heavy_armor:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.shields:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.packs:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.instruments:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.holy_symbols:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.artisans_tools:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.other_tools:
        if item == equip_item.name:
            return equip_item
    for equip_item in equipment.class_equipment:
        if item == equip_item.name:
            return equip_item
    return None
        