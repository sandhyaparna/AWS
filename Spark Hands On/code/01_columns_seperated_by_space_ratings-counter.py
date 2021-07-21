from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

# convert data to RDD
lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")

# sample data
# 196	242	3	881250949
# 186	302	3	891717742
# 22	377	1	878887116
# 244	51	2	880606923
# 166	346	1	886397596
# 298	474	4	884182806
# 115	265	2	881171488
# 253	465	5	891628467
# 305	451	3	886324817

# perform operations
ratings = lines.map(lambda x: x.split()[2])  # Extract 3rd from each row, obtained after splitting (extract 3rd column i.e ratings of movies)
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))

if __name__ == '__main__':
    print("Counts")


