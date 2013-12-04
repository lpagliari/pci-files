import newsfeatures

allw, artw, artt = newsfeatures.getarticlewords()
wordmatrix, wordvec = newsfeatures.makematrix(allw, artw)

wordvec[0: 10]
artt[1]
wordmatrix[1][0:10]
