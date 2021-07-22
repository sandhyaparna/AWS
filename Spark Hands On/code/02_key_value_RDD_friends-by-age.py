from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')  # split data by comma
    age = int(fields[2])  # Extract 3rd column i.e. age
    numFriends = int(fields[3])  # Extract 4th column i.e. number of friends
    return (age, numFriends)  # create tuples of age and their respective friends for each row

lines = sc.textFile("file:///SparkCourse/fakefriends.csv")  # csv file
rdd = lines.map(parseLine)  # apply parseLine function to convert csv file to key-value pairs

# mapValues function is applied on the value of the key-value pair. keys are left untouched
# reduceByKey is used to perform summation operation for a given key (if keys are same)
totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
averagesByAge = totalsByAge.mapValues(lambda x: int(x[0] / x[1]))  # within the value pair, value[0]/value[1]

results = averagesByAge.sortByKey().collect()  # sorting the average age by key

for result in results:
    if __name__ == '__main__':  # this code is used to run in pycharm
        print(result)

