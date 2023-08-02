"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 11: Import required modules and create an empty list named 'reviews_data'.
# This will be used to store the data read from the source data file.
#TODO: Your code here

import csv

from TEST import display_error_message

reviews_data = []


    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here

import tui
tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should represent a review in the list 'reviews_data'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many reviews have
    # been loaded and that the data loading operation has completed.
    
    # TODO: Your code here

import tui

def load_data(file_path):
    try:
        tui.display_message("Data loading has started. ")
        reviews_data = []
        with open(file_path, 'r') as file:
            for line in file:
                reviews_data.append(line.strip())
        tui.display_message(f"{len(reviews_data)} reviews have been loaded. ")
        tui.display_message("Data loading operation has completed. ")
        return reviews_data
    except FileExistsError:
        tui.display_message("Error: File not found. ")
        return[]
    except Exception as e:
        tui.display_message(f"Error: {str(e)}")
        return[]

file_path = 'reviews.txt'
reviews_data = load_data(file_path)


        # Task 14: Using the appropriate function in the module 'tui', display the main menu
        # Assign the value returned from calling the function to a suitable local variable
        # TODO: Your code here

import curses

def display_main_menu():
    #TODO: Implement your main menu here
    #You can use curse functions to draw text, boxes, buttons, etc.

def main():
#Initialize curses
   stdscr = curses.initscr()
   curses.curs_set(0)

   try:
       main_menu_result = display_main_menu()

   finally:
       curses.endwin()

if 'name' == "main":
    main()


        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve reviews by hotel name then
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the review and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve reviews by review dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve the reviews
        #       - Use the appropriate function in the module 'tui' to display the retrieved reviews.
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group reviews by nationality then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the reviews
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - If required, you may add a suitable function to the module 'tui' to display the groupings
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the reviews then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the reviews.
        #       - Add a suitable function to the module 'tui' to display the summary
        #       - Use your function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here

import tui
import process


def process_data():
    if tui.user_selected_processing_data():
        tui.display_message("Data processing operation has started. ")

        processing_option = tui.display_processing_menu()

        if processing_option == "retrieve_reviews_by_hotel":
            tui.display_message("Review retrieval process has started. ")

            reviews = process.retrieve_reviews_by_hotel_name()
            tui.display_reviews(reviews)

            tui.display_message("Review retrieval process has completed. ")

        elif processing_option == "Review retrieval process has completed. "

            tui.display_message("Reviews retrieval process has started. ")

            reviews = process.retrieve_reviews_by_dates()
            tui.display_reviews(reviews)

            tui.display_message("Reviews retrieval process has completed. ")

        elif processing_option == "group_reviews_by_nationality":
            tui.display_message("Grouping process has started. ")

            groupings = process.group_reviews_by_nationality()
            tui.display_groupings(groupings)

            tui.display_message("Grouping process has completed. ")

        elif processing_option == "summarize_reviews ":
            tui.display_message("Summary process has started. ")

            summary = process.summarize_reviews()
            tui.display_summary(summary)

            tui.display_message("Summary process has completed. ")

        else:
            tui.display_message("Invalid option selected. ")

    else:
        tui.display_message("Data processing ws not selected. ")


        """#Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual' to display the visual
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed."""

import json
from tui import get_export_options, indicate_export_started, indicate_export_completed

class Review:
    def __init__(self, title, rating, content, country):
        self.title = title
        self.rating = rating
        self.content = content
        self.country = country

    def to_dict(self):
        return{
        "title": self.title,
        "rating": self.rating,
        "content": self.content,
        "country": self.country
        }
class ReviewExporter:
    def __init__(self, reviews):
        self.reviews = reviews

    def export_all_reviews(self):
        data = [review.to_dict() for review in self.reviews]
        self._export_to_json(data)

    def export_reviews_by_country(self, country):
        filtered_reviews = [review.to_dict() for review in self.reviews if review.coutry == country]
        self._export_to_json(filtered_reviews)

    def _export_to_json(self, data):
        with open("reviews_export.json", "w") as file:
             json.dump(data, file, indent=2)

if __name__ == "__main__":

#reviews_data as a list of Reviews objects
    reviews_data = [
        Review("Great Product", 5, "This product exceeded my expectations!", "USA"),
        Review("Not Recommend", 1, "I had a terrible experience with this product.", "UK"),
        Review("Awesome!", 4, "This product is fantastic!", "USA"),
#more reviews
         ]
    export_options = get_export_options()

    if export_options:
        review_exporter = ReviewExporter(reviews_data)

        if export_options == "all":
            indicate_export_started()
            review_exporter.export_all_reviews()
            indicate_export_completed()

        elif export_options == "by_country":
            selected_country = input("Enter the country for which you want to export review: ")
            indicate_export_started()
            review_exporter.export_reviews_by_country(selected_country)
            indicate_export_completed()
        else:
            print("Invalid export option selected. ")


       """ # Task 25: Check if the user selected the option for exporting reviews.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve what reviews are to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the reviews (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the reviews, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the reviews (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here"""

def reviews_to_export():
    pass

class ReviewExporter:
    def __init__(self, export_option):
        self.export_option = export_option

    def export_review(self):
        self._start_export()
        reviews_to_export() == self._get_reviews_to_export()
        self._write_reviews_to_json(reviews_to_export)
        self._end_export()

    def _start_export(self):
        pass

    def _get_reviews_to_export(self):
        if self.export_option == 'all':
            pass

        elif self.export_option == 'specific':
            pass

    def _write_reviews_to_json(self, reviews):
        with open('reviews_export.json_file', 'w') as json_file:
            import json
            json.dump(reviews, json_file, indent=4)

    def _end_export(self):
        pass


def main():
    export_options = 'all'

    if export_options:
        review_exporter = ReviewExporter(export_options)
        review_exporter.export_review()


if __name__ != "__main__":
    pass


        """ # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here """

while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")

    user_input = input("Select an option (1, 2, or 3): ")

    if user_input == '3':
        print("Existing the program.")
        break

    if user_input == '1':
        print("You selected Option 1. ")

    elif user_input == '2':
        print("You selected Option 2.")

    else:
        print("Invalid option. Please choose a valid option (1, 2, or 3). ")


      """  # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here"""


def function_option_1():
    pass


def main(stdscr, function_option_1= None, function_option_2= None, function_option_3= None ):
    valid_options = ['1', '2', '3']

    stdscr.clear()
    stdscr.addstr("Select an option: \n")
    stdscr.addstr("1. Option 1\n")
    stdscr.addstr("2. Option 2\n")
    stdscr.addstr("3. Option 3\n")
    stdscr.refresh()

    user_input = stdscr.getch()
    selected_option = chr(user_input)

    if selected_option in valid_options:
        if selected_option == "1":
            function_option_1()
        elif selected_option == "2":
            function_option_2()
        else:
            function_option_3()
    else:
        display_error_message("Invalid option selected!", stdscr)

