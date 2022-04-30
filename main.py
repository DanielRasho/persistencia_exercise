# PERSONAL EXERCISE 1
# PROGRAM TO TRACK MOVIES AND SERIES:
#   
#   
#   
from IO_methods import menu_builder, clean_screen

while True:
    selected_option = menu_builder("NOW, WHAT YOU WANNA DO?",
                                    ["Add new series",
                                    "Edit tracked series",
                                    "View tracked series",
                                    "Show statistics"],
                                    "Move around with <DOWN ARROW>, <UP ARROW>, confirm with <ENTER>",
                                    return_value=True, default_options=["Exit"])

    match selected_option:
        case "Add new series":
            pass
        case "Edit tracked series":
            pass
        case "View tracked series":
            pass
        case "Show Statistics":
            pass
        case "Exit":
            exit()
