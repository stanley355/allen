import pandas
import matplotlib.pyplot as plt
import numpy

df = pandas.read_csv("w3schools/July_pre_post - july.csv")
x = df['tu_post_translate']
y = df['ec_post_translate']

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
ec_count = mymodel(1)
print(ec_count)
myline = numpy.linspace(1, 15, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()