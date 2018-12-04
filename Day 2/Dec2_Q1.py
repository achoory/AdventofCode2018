import collections
results = collections.Counter("dqddwqfwqfggqwq")
twoList = []
threeList = []

for res in results:
    #print(res, results[res])
    if (results[res] == 2):
      print(res, results[res])
    if (results[res] == 3):
      print(res, results[res])