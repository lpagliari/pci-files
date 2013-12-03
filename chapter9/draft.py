import advancedclassify
agesonly = advancedclassify.loadmatch('agesonly.csv', allnum = True)
matchmaker = advancedclassify.loadmatch('matchmaker.csv')

reload(advancedclassify)
avgs = advancedclassify.lineartrain(agesonly)

reload(advancedclassify)
advancedclassify.dpclassify([30,30], avgs)
advancedclassify.dpclassify([48,32], avgs)
advancedclassify.dpclassify([25,40], avgs)
advancedclassify.dpclassify([48,20], avgs)

reload(advancedclassify)
numericalset = advancedclassify.loadnumerical()
numericalset[0].data

reload(advancedclassify)
scaledset, scalef = advancedclassify.scaledata(numericalset)
avgs = advancedclassify.lineartrain(scaledset)
numericalset[0].data

reload(advancedclassify)
offset = advancedclassify.getoffset(agesonly)
advancedclassify.nlclassify([30,30], agesonly, offset)
advancedclassify.nlclassify([48,32], agesonly, offset)
advancedclassify.nlclassify([25,40], agesonly, offset)
advancedclassify.nlclassify([48,20], agesonly, offset)
