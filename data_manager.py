from family import Family,Person
import csv

families = {}
persons = {}

with open("muestra06.csv", 'r', encoding="latin-1") as file:
    reader = csv.reader(file, delimiter="\t")
    for line in reader:
        if len(line) != 27:
            print("uuuf")
            break
        elif len(line) == 27:
            print("cool")
        

