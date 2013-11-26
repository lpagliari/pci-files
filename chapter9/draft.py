import advancedclassify
agesonly = advancedclassify.loadmatch('agesonly.csv', allnum = True)
matchmaker = advancedclassify.loadmatch('matchmaker.csv')

reload(advancedclassify)
avgs = advancedclassify.lineartrain(agesonly)

reload(advancedclassify)
advancedclassify.dpclassify([30,30], avgs)
advancedclassify.dpclassify([48,32], avgs)
advancedclassify.dpclassify([25,40], avgs)