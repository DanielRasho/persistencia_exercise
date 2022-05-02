from readchar import readkey, key
import os
import database

def menu_builder(header: str, options: list, footer: str, return_value = False, default_options = []):
    # Builds an interface where user can choose beetween given options.

    cursor_position = 0
    options += default_options

    while True:
        # Print Menu
        clean_screen()
        print(f"{header}\n")
        for index, option in enumerate(options):
            if index == cursor_position:
                print(f"\t>> {option}")
            else:
                print(f"\t   {option}")
        print(f"\n{footer}")

        # Modify cursor postion
        new_cursor_position = readkey()
        if new_cursor_position == key.UP:         # UP ARROW
            cursor_position -= 1
            cursor_position %= len(options)
        elif new_cursor_position == key.DOWN:     # DOWN ARROW
            cursor_position += 1
            cursor_position %= len(options)
        elif new_cursor_position == key.ENTER:   # ENTER KEY
            if return_value is True: return options[cursor_position]
            else: return cursor_position

def numeric_slider(header: str, footer: str, start = 0, step = 1, just_positive_values = True):
    # Builds an interface where user can move to write a numeric value

    cursor_position = 0
    options = [start]
    while True:
        # Print Menu
        clean_screen()
        print(f"{header}\n")
        print(f"<< {options[abs(cursor_position)]} >>")
        print(f"\n{footer}")

        # Modify cursor postion
        new_cursor_position = readkey()
        if new_cursor_position == key.LEFT:         # LEFT ARROW
            cursor_position -= 1
        elif new_cursor_position == key.RIGHT:     # RIGHT ARROW
            cursor_position += 1
        elif new_cursor_position == key.ENTER:   # ENTER KEY
            print(options)
            return options[abs(cursor_position)]
        
        if just_positive_values == True:
            if cursor_position >= len(options):
                options.append(options[-1] + step)
            elif (cursor_position * step) < start:
                cursor_position = 0
        else:
            if abs(cursor_position) >= len(options):
                options.append(options[-1] - step)
            elif (cursor_position * step)  > start:
                cursor_position = 0

def clean_screen():
    # Cleans terminal screen  
    if os.name == "posix":  # If program is executed in Linux or Mac
        os.system("clear")
    else:
        os.system("cls")

def input_new_series():
    # Just a shortcut to ask user for data for a new item.
    while True:
        name = input("Enter your series name: ")
        if database.is_series_saved(name) == False:
            state = menu_builder("What is the current state of the series?",
                            ["Finished",
                            "Watching",
                            "Watch later",
                            "Stop watching it"],
                            "Move around with <DOWN ARROW>, <UP ARROW>, confirm with <ENTER>",
                            return_value=True)
            episode_duration = numeric_slider("What is the average episode duration (minutes)?",
                            "Move around with <RIGHT ARROW>, <LEFT ARROW>, confirm with <ENTER>",
                            start=10, step=10)
            watched_episodes = numeric_slider("How many episodes have you watched?",
                            "Move around with <RIGHT ARROW>, <LEFT ARROW>, confirm with <ENTER>",
                            start=1, step=1)
            platform = menu_builder("Where are you watching it?",
                            database.get_platforms(),
                            "Move around with <DOWN ARROW>, <UP ARROW>, confirm with <ENTER>",
                            return_value=True, default_options=["Add New"])
            if platform == "Add New":
                platform = input("Write the new platform: ")

            return [name, state, episode_duration, watched_episodes, platform]
        else:
            print("That series is already on the list.\nPress <ENTER> to try again...")
            input()

def input_update_series():
    # Just a shortcut to ask user for data to update an existent item.
    series_to_edit = menu_builder("What series you wanna edit?",
                    database.get_series_items_names(),
                    "Move around with <DOWN ARROW>, <UP ARROW>, confirm with <ENTER>",
                    return_value=True)
    field_to_edit = menu_builder("What field you wanna edit?",
                    list(database.MOVIES_FIELDS.keys())[:-1],
                    "Move around with <DOWN ARROW>, <UP ARROW>, confirm with <ENTER>",
                    return_value=True)

    field_type = database.MOVIES_FIELDS[field_to_edit]

    if field_type is str:
        new_value = input(f"Enter your new value for {field_to_edit}: ")
    elif field_type is int:
        new_value = numeric_slider(f"Enter your new value for {field_to_edit}: ",
                        "Move around with <RIGHT ARROW>, <LEFT ARROW>, confirm with <ENTER>",
                        start=1, step=1)
    return [series_to_edit, field_to_edit, new_value]
