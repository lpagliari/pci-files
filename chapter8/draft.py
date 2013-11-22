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

reload(numpredict)
data = numpredict.wineset2()
numpredict.crossvalidate(knn1, data)
numpredict.crossvalidate(knn3, data)
numpredict.crossvalidate(numpredict.knnestimate, data)

reload(numpredict)
sdata = numpredict.rescale(data, [10, 10, 0, 0.5])
numpredict.crossvalidate(knn1, sdata)
numpredict.crossvalidate(knn3, sdata)
numpredict.crossvalidate(numpredict.knnestimate, sdata)

#######################################################
import optimization
reload(numpredict)
costf = numpredict.createcostfunction(numpredict.knnestimate, data)
optimization.annealingoptimize(numpredict.weightdomain, costf, step = 2)
# result: [10,10,0,6]

reload(numpredict)
numpredict.probguess(data, [99, 20], 40, 80)
numpredict.probguess(data, [99, 20], 80, 120)
numpredict.probguess(data, [99, 20], 1000, 1200)
numpredict.probguess(data, [99, 20], 30, 120)
