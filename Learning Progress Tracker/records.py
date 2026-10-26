import csv
def add_records():
    date = input("Date:")
    topic = input("Topic:")
    while True:
        try:
            duration = float(input("Duration(hours):"))
            if duration <= 0:
                print("Duration must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid duration. Please enter a number.")


    resource = input("Resource:")

    record = {
        "Date":date,
        "Topic":topic,
        "Duration":duration,
        "Resource":resource
    }
    with open("learning_records.csv", "a", newline = "", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames = ["Date","Topic","Duration","Resource"]
            )
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(record)


def view_records():
    try:
        print("=== Learning Records ===\n")
        with open("learning_records.csv", "r",newline = "", encoding = "utf-8") as file:
            reader = csv.DictReader(file)

            for record in reader:
                print(
                    f"{record['Date']} | {record['Topic']} | {record['Duration']}(h) | {record['Resource']}"
                )
    except FileNotFoundError:
        print("File Not Found")

def longest_time_record():
    try:
        with open("learning_records.csv", "r",newline = "", encoding = "utf-8") as file:
            reader = csv.DictReader(file)
        
            longest_record = max(
                                reader,
                                key=lambda record: float(record["Duration"]),
                                default=None
                                )

        if longest_record is not None:
            print(
            f"Longest study session:\n"
            f"{longest_record['Topic']} - {longest_record['Duration']} hours"
            )

    except FileNotFoundError:
            print("File Not Found")

def total_time_record():
    try:
        with open("learning_records.csv", "r",newline = "", encoding = "utf-8") as file:
            reader = csv.DictReader(file)

            total_time = 0
        
            for record in reader:
                total_time += float(record["Duration"])
            print(f"Total study time: {total_time} hours")
    except FileNotFoundError:
            print("File Not Found")

def sort_record():
    try:
        with open("learning_records.csv", "r",newline = "", encoding = "utf-8") as file:
            reader = csv.DictReader(file)

            sorted_records = sorted(
                reader,
                key=lambda record: float(record["Duration"]),
                reverse=True
                )
            i = 1   
            for record in sorted_records:
                print(f"{i}. {record['Topic']}--{record['Duration']}(h)")
                i += 1
    except FileNotFoundError:
            print("File Not Found")            
            