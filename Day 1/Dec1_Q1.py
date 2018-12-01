path = './Day1_input.txt'

observations = open(path, 'r')

# read observations from file
obsFromFile = observations.read()
obsFromFile = obsFromFile.split('\n')
observations.close()

print(len(obsFromFile))
print(type(obsFromFile))


print(obsFromFile)
# remove last element in list - empty
obsFromFile.pop()

results = list(map(int, obsFromFile))

print(type(results))

lenRes = len(results)
print(lenRes)

# Making sure the content of the list is of type int
for res in results:
    print(type(res))
    break

count = 0
tempSum = 0
resFreq = [0]

for i in range(len(results)):

       count = count + 1

       if i < len(results)-1:

           # until end is reached

           if count == 1:
               tempSum = results[i] + results[i+1]
               resFreq.append(tempSum)

           else:
               tempSum = tempSum + results[i+1]
               resFreq.append(tempSum)

       else:
           print('tempSum at this stage is:', tempSum)
           # end


finalSum = tempSum

print('Method 1: Final result: ', finalSum)

# Much easier way..Zzz
print('Method 2: Final result is:', sum(results))

# Some calculations necessary for Q2

print('Resulting frequencies are: ')
print(resFreq)

uniqueList = set(resFreq)
# print(len(uniqueList))

for res in resFreq:
    if res not in uniqueList:
        print(res)

# does not print because in reality they want us to loop over this resFreq list several times till a duplicate is found..(Q2)


















