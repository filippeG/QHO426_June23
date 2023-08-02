import Matplotlib.pyplot as plt


def pie_chart_positive_negative(hotel_name, positive_reviews_count, negative_reviews_count):
    plt.figure(figsize=(8, 8))
    labels = ['Positive, Negative']
    sizes = [positive_reviews_count, negative_reviews_count]
    colors = ['#66b3ff', '#ff9999']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f"Positive vs. Negative Reviews for {hotel_name}")
    plt.axis('equal')
    plt.show


def bar_chart_reviews_by_nationality(nationalities, review_counts):
    plt.figure(figsize=(12, 6))
    plt.bar(nationalities, review_counts, color='#66b3ff')
    plt.xlabel('Nationality')
    plt.ylabel('Number of Reviews')
    plt.title('Number of Reviews per Nationality')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def animated_line_chart_over_time(time_point, positive_counts, negative_counts, average_ratings, time_points=None):
    plt.figure(figsize=(10, 6))
    plt.title('Positive, Negative Reviews, and Average Rating Over Time')
    plt.xlabel('Time')
    plt.ylabel('Count / Rating')

    for i in range(len(time_points)):
        plt.plot(time_points[:i + 1], positive_counts[:i + 1], label='Positive Reviews', color='green')
        plt.plot(time_points[:i + 1], negative_counts[:i + 1], label='Negative Reviews', color='red')
        plt.plot(time_points[:i + 1], average_ratings[:i + 1], label='Average Rating ', color='blue')

        plt.legend(loc='upper left')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(0.5)
        if i < len(time_points) - 1:
            plt.clf()

    plt.show()


# Data to visualization "example"

hotel_name = "Sample Hotel"
positive_review_count = 120
negative_reviews_count = 80

nationalities = ["USA", "UK", "CANADA", "France", "China", "Australia", "Italy", "Spain", "Japan"]
review_count = [250, 200, 180, 170, 160, 140, 130, 120, 110, 100]

time_points = ['Jan 2023', 'Feb 2023', 'Mar 2023', 'Apr 2023', 'May 2023']
positive_count = [50, 65, 80, 95, 110]
negative_counts = [20, 25, 40, 45, 60]
average_ratings = [4.2, 4.0, 3.8, 4.1, 4.3]

# generate the visualization
pie_chart_positive_negative(hotel_name, positive_review_count, negative_reviews_count)
bar_chart_reviews_by_nationality(nationalities, review_count)
animated_line_chart_over_time(time_points, positive_count, negative_counts, average_ratings)

