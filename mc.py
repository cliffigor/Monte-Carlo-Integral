import random
import numpy as np
from scipy.integrate import quad

# method 1

def monteCarloIntegral_1(fun, lower, upper, totalPoints):
    x = np.random.uniform(low=lower, high=upper, size=totalPoints)

    result = (upper - lower) / totalPoints * np.sum(fun(x))
    print(result)
    print("Integration calc with SciPy 'quad' function:   {}".format(round(quad(fun, lower, upper)[0],6)))

    return result
    

# method 2

def monteCarloIntegral_2(fun, lower, upper, totalPoints, M):
    x = np.random.uniform(low=lower, high=upper, size=totalPoints)
    y = np.random.uniform(low=0, high=M, size=totalPoints)

    counter = 0

    for i in range(len(x)):
        if y[i] <= fun(x[i]):
            counter += 1

    result = (upper - lower) * (counter/totalPoints) * M
    print(result)

    return result

fun = lambda x: (x ** 2)

lower = 0
upper = 2

totalPoints = 100000000
counter = 0

monteCarloIntegral_1(fun, lower, upper, totalPoints)
monteCarloIntegral_2(fun,lower,upper, totalPoints, 4)
