import pylab as plt


mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

#Four kinds of graphs drawn

plt.figure('lin')
plt.title('Linear')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.title('Quadratic')
plt.xlabel('sample points')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)

plt.figure('cube')
plt.title('Cubic')
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic)

plt.figure('exp')
plt.title('Exponential')
plt.xlabel('sample points')
plt.ylabel('exponential function')
plt.plot(mySamples, myExponential)

#Shows the graphs, because drawing turned off by default?
plt.show()
