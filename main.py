# PERSONAL EXERCISE 1
# PROGRAM TO TRACK MOVIES AND SERIES:
#   
#   
#   
import setup
from IO_methods import input_new_series, input_update_series, menu_builder, clean_screen
import database

while True:
    clean_screen()
    selected_option = menu_builder("NOW, WHAT YOU WANNA DO?",
                                    ["Add new series",
                                    "Delete series",
                                    "Edit tracked series",
                                    "View tracked series",
                                    "Show statistics"],
                                    "Move around with <DOWN ARROW>, <UP ARROW>, confirm with <ENTER>",
                                    return_value=True, default_options=["Exit"])

    match selected_option:
        case "Add new series":
            new_item_data = input_new_series()
            database.add_series(*new_item_data)
        case "Delete series":
            selected_series = menu_builder("Which series you want to delete?",
                                            database.get_series_items_names(),
                                            "Move around with <DOWN ARROW>, <UP ARROW>, confirm with <ENTER>",
                                            return_value=True, default_options=["Exit"])
            database.delete_series(selected_series)
        case "Edit tracked series":
            update_item_data = input_update_series()
            database.update_series(*update_item_data)
        case "View tracked series":
            pass
        case "Show Statistics":
            pass
        case "Exit":
            exit()
