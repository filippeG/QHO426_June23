def display_progress(value):
    if value == 0:
        status = "initiated"
    elif 0 < value < 100:
        status = "initiated"
    elif value == 100:
        status = "completed"
    else:
        raise ValueError("Invalid value: progress valueshould be between 0 and 100")

        f"Operation: {operation} [{status}]."
    print(message)


display_progress("File Upload", 0)
display_progress("Data Processing", 50)
display_progress("Task Completed", 100)
