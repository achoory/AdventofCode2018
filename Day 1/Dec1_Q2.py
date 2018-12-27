path = './Day1_input.txt'
observations = open(path, 'r')

# read observations from file
obsFromFile = observations.read()
obsFromFile = obsFromFile.split('\n')
observations.close()

# remove last element in list - empty
obsFromFile.pop()
results = list(map(int, obsFromFile))

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
        else:
            unique.add(tempSum)