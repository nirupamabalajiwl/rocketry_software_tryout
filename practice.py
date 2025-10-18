import matplotlib.pyplot as plt 
import numpy

x = numpy.array([1,2,3,4,1])
y = numpy.array([2,4,1,3,4])

plt.plot(x,y)

plt.xlabel("input")
plt.ylabel("views")
plt.title("Website Views Over Time")

plt.show ()

