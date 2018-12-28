path = './Day1_input.txt'

results = []
for row in open(path, 'r'):
    if row != '\n':  # Only if row is not a blank line
        row.strip()  # Remove any whitespaces from start/end of row
        results.append(int(row))  # Convert the row to an int and save it

unique = set()
#starts from 0
unique.add(0);
tempSum = 0


while True:

    for res in results:

        tempSum += res

        if tempSum in unique:
            print(tempSum)
            exit(0)

        unique.add(tempSum)