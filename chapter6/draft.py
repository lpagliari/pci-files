import docclass
cl = docclass.classifier(docclass.getwords)
cl.setdb('test_naive.db')
cl.train('the quick brown fox jumps over the lazy dog','good')
cl.train('make quick money in the online casino','bad')
cl.fcount('quick','good')
cl.fcount('quick','bad')
