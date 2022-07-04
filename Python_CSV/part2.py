import csv

with open("melts_output.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    title = next(reader)[1]
    print(title)

    found_section = False
    header = None
    alloy_index = None
    alloy_sum = 0.0

    for row in reader:
        if not found_section:
            if len(row) > 0:
                if row[0] == "Phase":
                    header = next(reader)
                    alloy_index = header.index("alloy")
                    found_section = True
                else:
                    pass
        else:
            if len(row) > 0:
                alloy_sum += float(row[alloy_index])
            else:
                break

    print(alloy_sum)







