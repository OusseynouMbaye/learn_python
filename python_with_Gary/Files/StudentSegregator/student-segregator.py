import csv

classes = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}}
with open("students.csv", encoding="utf8") as students_file:
    csvreader = csv.reader(students_file)
    for index, name in csvreader:
        id = int(index)
        class_number = id % 5 + 1
        classes[class_number][id] = name  # on assigne pour chaque dict id et value

# for loop which iterates over classes dict items
for class_number, cohort in classes.items():
    # class number to create a classname.txt filename
    filename = f"class{class_number}.txt"
    # loop over the student names
    for name in cohort.values():
        # open class<number>.txt for appending as class_file
        with open(filename, 'a') as class_file:
            # Write the students name to the file
            class_file.write(f'{name}\n')
