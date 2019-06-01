import matplotlib
import matplotlib.pyplot as plt

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

plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.plot(mySamples, myCubic)
plt.figure('exp')
plt.plot(mySamples, myExponential)

plt.show()
