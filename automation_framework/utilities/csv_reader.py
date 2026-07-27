import csv


def read_csv(file_path):

    data = []

    with open(file_path, newline="", encoding="utf-8") as file:

        reader = csv.reader(file)
        next(reader)


        for row in reader:
            data.append(tuple(row))


    return data