from pyspark import SparkConf
from pyspark import SparkContext
import os

conf = SparkConf()
conf.setMaster('yarn')
conf.setAppName('testing')
sc = SparkContext(conf=conf)
rdd = sc.parallelize([1,2,3,4,5])
print(rdd.sum())
