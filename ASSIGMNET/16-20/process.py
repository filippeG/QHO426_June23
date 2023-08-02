"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""

def get_total_reviews(reviews):
    return len(reviews)

def get_review_by_hotel(review):
    hotel_name = input("Enter the hotel name: ")
    return [review for review in review if review[1] == hotel_name]

def get_review_by_dates(reviews):
    start_data = input("Enter the start date (yyyy-mm-dd): ")
    end_date = input("Enter the end date (yyyy-mm-dd): ")
    return [review for review in reviews if start_date <= review[2] <= end_date]

def get_reviews_by_nationality(reviews):
    reviews_by_nationality = {}
    for review in reviews:
        nationality = review[3]
        if nationality in reviews_by_nationality:
            reviews_by_nationality[nationality].append(review)
        else:
            reviews_by_nationality[nationality] = [review]
    return reviews_by_nationality

def get_reviews_summary(reviews):
    from collections import defaultdict
    summary = defaultdict(lambda: {'negative': 0, 'positive': 0, 'total_ratings': 0, 'rating_sum': 0})

    for review in reviews:
        date = review[2]
        rating = float(review[4])
        if rating < 5:
            summary[date]['negative'] += 1
        else:
            summary[date]['positive'] += 1

        summary[date]['total_rating'] += 1
        summary[date]['rating_sum'] += rating

    sorted_dates = sorted(summary.keys())
    result = []
    for date in sorted_dates:
        total_neg = summary[date]['negative']
        total_pos = summary[date]['positive']
        total_ratings = summary[date]['total_rating']
        average_rating = summary[date]['rating_sum'] / total_ratings if total_ratings > 0 else 0.0
        result.append((date, total_neg, total_pos, average_rating))

    return result
