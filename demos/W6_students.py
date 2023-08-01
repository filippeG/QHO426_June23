import csv
def reading():
    with open("files/students.csv") as studs:
        csv_reader = csv.reader(studs)
        next(csv_reader) #skipp the header
        for row in csv_reader:
            print(f"{row[0]} recived {row[2]} marks for Exam 1 and {row[3]} for Exam 2")

def writing():
    with open("files/students.csv", "a") as studs:
        csv_writer = csv.writer(studs)
        while True:
            name = input("Enter Name: ")
            id = input("Enter ID: ")
            e1 = int(input("Enter Exam 1 Score: "))
            e2 = int(input("Enter Exam 2 Score: "))
            csv_writer.writerow([name, id, e1, e2])
            if input("Do you want to stop [y/n]").lower() == "y":
               break

writing()
