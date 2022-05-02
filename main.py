# PERSONAL EXERCISE 1
# PROGRAM TO TRACK MOVIES AND SERIES:
#   
#   
#   
import setup
from IO_methods import input_new_series, input_update_series, menu_builder, clean_screen
import database
from statistics_functions import Most_Watched_Series, Most_Common_Streaming_Plat, Finished_Series_Counter

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

    if selected_option == "Add new series": 
            new_item_data = input_new_series()
            database.add_series(*new_item_data)
    if selected_option == "Delete series":
            selected_series = menu_builder("Which series you want to delete?",
                                            database.get_series_items_names(),
                                            "Move around with <DOWN ARROW>, <UP ARROW>, confirm with <ENTER>",
                                            return_value=True, default_options=["Exit"])
            database.delete_series(selected_series)
    if selected_option == "Edit tracked series":
            update_item_data = input_update_series()
            database.edit_series(*update_item_data)
    if selected_option == "View tracked series":
        database.print_series()
    if selected_option == "Show statistics":
        Most_Watched_Series()
        Most_Common_Streaming_Plat()
        Finished_Series_Counter()
    if selected_option == "Exit":
            exit()