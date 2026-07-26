import csv


def read_csv(file_path):

    data = []

    with open(file_path, newline="") as csv_file:

        reader = csv.DictReader(csv_file)

        for row in reader:
            data.append((row["username"], row["password"]))

    return data