import numpredict

numpredict.wineprice(95.0, 3.0)
numpredict.wineprice(95.0, 8.0)
numpredict.wineprice(99.0, 1.0)

data = numpredict.wineset1()

data[0]
data[1]

reload(numpredict)
numpredict.euclidean(data[0]['input'], data[0]['input'])

reload(numpredict)
numpredict.knnestimate(data, (95.0, 3.0), k=1)
numpredict.wineprice(95.0, 3.0)

reload(numpredict)
numpredict.weightedknn(data, (95.0, 3.0), k=1)

reload(numpredict)
def knn3(d, v):
  return numpredict.knnestimate(d, v, k = 3)

def knn1(d, v):
  return numpredict.knnestimate(d, v, k = 1)

numpredict.crossvalidate(knn1, data)
numpredict.crossvalidate(knn3, data)
numpredict.crossvalidate(numpredict.knnestimate, data)

