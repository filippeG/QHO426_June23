"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should display the title 'Hotel Reviews'.
    The welcome message should contain asterisks before and after the title.
    The number of asterisks should be equivalent to the number of characters in the title.
    There should be a space between the asterisks and the title i.e. a space before and after the title

    :return: Does not return anything.
    """
    # TODO:

def display_welcome_message(title):
#Calculate number of asrerisks needed
    num_asterisks = len(title)
#Welcome message
welcome_message = f"* {title} *"
#Line of asterisks
asterisks_line = "*" * (num_asterisks + 4)
#Display the welcome message
print(asterisks_line)
print(welcome_message)
print(asterisks_line)

display_welcome_message("Hotel Reviews")


#Task 2: Display an error message.
"""
    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter 'msg' passed to this function

    :param msg: a string containing an error message
    :return: does not return anything
"""
    # TODO: Your code here

def display_error_message(msg):
    print(f"Error! {msg}.")


    Task 3: Display a message to indicate the progress of an operation.

    The function should display a message in the following format:
    'Operation: {operation} [{status}].'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'initiated' if the value of the parameter 'value' is 0
    {status} is 'in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'completed' if the value of the parameter 'value' is 100

    :param operation: a string indicating the operation being started
    :param value: an integer indicating the amount of progress made
    :return: does not return anything

    # TODO: Your code here

def display_progress(value):
    if value == 0:
        status = "initiated"
    elif 0 < value < 100:
        status = "initiated"
    elif value == 100:
        status = "completed"
    else:
        raise ValueError("Invalid value: progress valueshould be between 0 and 100")

    message = f"Operation: {operation} [{status}]."
    print(message)

display_progress("File Upload", 0)
display_progress("Data Processing", 50)
display_progress("Task Completed", 100)



def main_menu():
"""
Task 4: Display the main menu and read the user response.

    The following options should be displayed:

    '[1] Process Data', '[2] Visualise Data', '[3] Export Data' and '[4] Exit'

In each of the above cases, the users response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.

    If the user enters a invalid option then a suitable error should be displayed and the user
    prompted to try again.

    :return: an integer for a valid selection
"""

    # TODO: Your code here

def display_menu():
    print("Main Menu:")
    print("[1] Process Data")
    print("[2] Visualise Data")
    print("[3] Export Data")
    print("[4] Exit ")


def get_user_choise():
    while True:
        try:
            choice = int(input("Please enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid option. Please enter a number between 1 and 4. ")
        except ValueError:
            print("Invalid input. Please enter a valid number. ")


def get_user_choice():

    if 'name' == "main":

        while True:
            display_menu()
            user_choice = get_user_choice()

            if user_choice == 1:
                print("You selected 'Process Data'")
            elif user_choice == 2:
                print("You selected 'Visualise Data'")
            elif user_choice == 3:
                print("You selected 'Export Data'")
            elif user_choice == 4:
                print("Exiting the program. Goodbye!")



   """ Task 5: Display a sub menu of options and read the users response.

    If no value or a zero is supplied for the parameter 'variant' then a suitable error should be displayed
    and the value 0 should be returned.

    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:

    [1] Reviews for Hotel, [2] Reviews for Dates, [3] Reviews for Nationality,
    [4] Reviews Summary

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Positive/Negative Pie Chart', '[2] Reviews Per Nationality Chart', '[3] Animated Summary'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    #[1] All Reviews', '[2] Reviews for Specific Hotel'

    In each of the above cases, the users response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Reviews for Hotel', 2 for 'Reviews for Dates' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: 0 if invalid selection otherwise an integer for a valid selection
"""
    # TODO: Your code here

def display_sub_menu(variant):
    if variant == 0:
        print("Error: Invalid variant value. Please provide a non-vero value. ")
        return 0
    elif variant == 1:
        print("[1] Reviews for Hotel")
        print("[2] Reviews for Dates")
        print("[3] Reviews for Nacionality" )
        print("[4] Reviews Summary")
    elif variant == 2:
        print("[1] Positive/Negative Pie Chart")
        print("[2] Reviews per Nationality Chart")
        print("[3] Animated Summary")
    elif variant == 3:
        print("[1] All Reviews")
        print("[2] Reviews for Specific Hotel")
    else:
        print("Error: Invalid variant value. Please choose a valid variant.")
        return 0

    while True:
        try:
            user_input = int(input("Enter your selection: "))
            if 1 <= user_input <= 4:
                return user_input
            else:
                print("Error: Invalid option. Please select a valid option. ")
        except ValueError:
            print("Error: Invalid input Please enter A valid integer.")

select_option = display_sub_menu(1)
print("Selected option: ", select_option)




def total_reviews(num_reviews):

  """"  Task 6: Display the total number of reviews in the data set.
    
    The function should display a message in the following format:

    "There are {num_reviews} reviews in the data set."

    Where {num_reviews} is the value of the parameter passed to this function
    
    :param num_reviews: the total number of reviews in the data set
    :return: Does not return anything
"""
    # TODO: Your code here

def display_num_reviews(num_reviews):
    print("There are {} reviews in the data set.". format(num_reviews))


    Task 7: Read in and return the name of a hotel.

    The function should ask the user to enter a hotel name e.g. Hotel Arena
    The function should then read in and return the users response as a string.

    :return: the name of a hotel

    # TODO: Your code here

def get_hotel_name():
    hotel_name = input("Please enter the name of a hotel: ")
    return hotel_name
#testing the function
hotel_name = get_hotel_name()
print("Hotel name entered: " , hotel_name)



  """  Task 8: Read in and return a list of review dates.

    The function should ask the user to enter some review dates
    This should be entered in the format mm/dd/yyyy (same as that in the file)
    where dd is two-digit day, 
    mm is two digit month and 
    yyyy is a four digit year 
    e.g.01/22/2020
    The function should return a list containing the specified review dates.

    :return: a list of review dates
"""
    # TODO: Your code here

def get_review_dates():
    reviews_dates = []
    while True:
        date_input = input("Enter a review date (mm/dd/yyyy) or 'done' to finish: ")

        if date_input.lower() == 'done':
            break

        try:
            month, day,year = map(int, date_input.split("/"))
            if len(str(year)) != 4 or not (1 <= month <= 12) or not (1 <= 31):
                raise ValueError
            reviews_dates.append(date_input)
        except ValueError:
            print("Invalid date format. Please use the format mm/dd/yyyy.")
    return reviews_dates
review_dates_list = get_review_dates()
print("Review dates entered:", review_dates_list)


"""
    Task 9: Display a review. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the review will be displayed.

    The parameter review is a list of values 
    e.g. ["08/03/2017", "Hotel Arena", "Russia", "I am so angry...", "Only the park...", 2.9,	7, "[' Leisure trip ', ' Couple ', ' Duplex Double Room ', ' Stayed 6 nights ']", "0 days"]
    [Note: in the above example, the ... is an ellipsis and is only included here as the text is long]

    The parameter cols is a list of column indexes e.g. [0,3,5]
    
    The function should display a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the sample review above the following should be displayed:
    ["Hotel Arena", "I am so angry..."]

    E.g. if cols is [0,1,5] then for the sample review above the following should be displayed:
    ["08/03/2017", "Hotel Arena", 2.9]

    E.g. if cols is an empty list or None then all the values will be displayed
    ["08/03/2017", "Hotel Arena", "Russia", "I am so angry...", "Only the park...", 2.9,	7, "[' Leisure trip ', ' Couple ', ' Duplex Double Room ', ' Stayed 6 nights ']", "0 days"]

    :param review: A list of data values for a review
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
"""
    # TODO: Your code here

def display_review(reviews, cols=None):
    if cols is None:
        display_list = review
    else:
        display_list = [review[i] for i in cols]

    print(display_list)

review = ["08/03/2017", "Hotel Arena", "Russia", "I am so angry ...", "Only the Park...", 2.9, 7, "[Leisure trip" , "couple", "Duplex Double Room", "Stayed 6 nights" , "0 days"]

display_review(review, [1, 3])
output:("Hotel Arena", 'I am so angry...')
display_review(review , (0, 1, 5))
display_review(review)




  """  Task 10: Display each review in the specified list of reviews.
    
    This function will display more than one review.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a review will be displayed.

    The function should have two parameters as follows:

    reviews     which is a list of reviews where each reviews itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each review in reviews and display the relevant review data.

    Each review should be displayed as a list of values 
    e.g. ["08/03/2017", "Hotel Arena", "Russia", "I am so angry...", "Only the park...", 2.9,	7, "[' Leisure trip ', ' Couple ', ' Duplex Double Room ', ' Stayed 6 nights ']", "0 days"]
    
    Only the columns whose indexes are included in cols should be displayed for each review.

    If cols is an empty list or None then all values for the review should be displayed.

    :param reviews: A list of reviews
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
"""
    # TODO: Your code here

def display_reviews(reviews, cols = None):
    for review in reviews:
        if cols is None or not cols:
            print(review)
        else:
            selected_data = [review[i] for i in cols if i < len(review)]
            print(selected_data)

# testing
if 'Name' == "main":
    sample_reviews = ["08/03/2017", "Hotel Arena", "Russia", "I am angry ... ", "Only the park ..." , 2.9, 7, "['Leisure trip', 'Couple', 'Duplex Double Room','Stayed 6 nights'] ", "0 days"], "07/30/2017", "Hilton Moscow", "Russia", "Very comfortable", "The bed was...", 10.0, 10, "[' Leisure trip', 'Solo traveler', 'King Hilton Guestroom', 'Stayed 2 nights']", "0 days]"

#Display all columns for each review
print("Displaying all colums: ")
display_reviews(sample_reviews)

#Display specific colums (e.g., column index 0, 1, and 4) for each review
print("\nDisplaying specific colums: ")
display_reviews(sample_reviews, cols=[0, 1, 4])