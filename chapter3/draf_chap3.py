feed = feedparser.parse('http://spchicagosp.wordpress.com/feed')
feed.entries




================
import clusters
blognames, words, data = clusters.readfile('blogdata.txt')
clust = clusters.hcluster(data)
clusters.printclust(clust, labels = blognames)
clusters.drawdendrogram(clust, blognames, img ='blogclust.png')

