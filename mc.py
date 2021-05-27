from scipy.integrate import quad
import numpy as np
import random
import sympy as sp

def get_function_points(fun, a, b, total_points):         
    fp = {}         #创建一个字典用来保存结果
    interval = (b - a) / total_points
    fp["x"], fp["y"] = [], []
    for counter in range(total_points):
        fp["x"].append(counter * interval)
        fp["y"].append(fun(fp["x"][counter]))
    return fp

def get_max_y_from_function(y_points):      #函数的上界M
    M = 0
    M = max(y_points)
    return M

def create_random_points(total_points, a, b, Max):      #创建点
    rp = {"x" : [], "y" : []}
    for i in range(total_points):
        rp["x"].append(random.uniform(a, b))
        rp["y"].append(random.uniform(0, Max))
    return rp

def calculate_points_below_function(fun, random_points):        #计算在函数下方的点的数量
    counter = 0
    for x, y in zip(random_points["x"], random_points["y"]):
        if y < fun(x):
            counter = counter + 1
    return counter

def mc_integration(fun, a, b, total_points):
    function_points  = get_function_points(fun, a, b, total_points)
    function_max_y   = get_max_y_from_function(function_points["y"])
    random_points    = create_random_points(total_points, a, b, function_max_y)

    print("---")
    print("Limits of Integration: {} and {}".format(a, b))
    print("Total Random Points:   {}".format(total_points))
    print("")                                                                   #(函数下方的点/总点数)*(上限-下限)*函数的上界
    print("Integration calc with Monte Carlo method:      {}".format((calculate_points_below_function(fun, random_points)/total_points)*(b-a)*function_max_y))
    print("Integration calc with SciPy 'quad' function:   {}".format(quad(fun, a, b)))
    print("")
    print("---")

def main():
    fun=lambda x: np.e**-(x ** 2)
    a=int(input("Input lower limit:"))
    b=int(input("Input upper limit:"))
    n=int(input("Input the number of random point you want to create:"))
    mc_integration(fun, a, b, n)

#------------------------#

main()
