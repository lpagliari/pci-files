import treepredict
treepredict.divideset(treepredict.my_data, 2, 'yes')

treepredict.giniimpurity(treepredict.my_data)
treepredict.entropy(treepredict.my_data)

set1, set2 = treepredict.divideset(treepredict.my_data, 2, 'yes')
treepredict.giniimpurity(set1)
treepredict.entropy(set1)

tree = treepredict.buildtree(treepredict.my_data)
treepredict.printtree(tree)
#treepredict.drawtree(tree, jpeg='treeview.jpg')

treepredict.prune(tree, 0.1)
treepredict.printtree(tree)

treepredict.prune(tree, 1.0)
treepredict.printtree(tree)

treepredict.mdclassify(['google', None, 'yes', None], tree)
treepredict.mdclassify(['google', 'France', None, None], tree)

###########
import zillow
housedata = zillow.getpricelist()
housedata = filter(None, housedata)
reload(treepredict)
housetree = treepredict.buildtree(housedata, scoref = treepredict.variance)
#treepredict.drawtree(housetree,' housetree.jpg')
treepredict.printtree(housetree)
