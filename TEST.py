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


process_data()