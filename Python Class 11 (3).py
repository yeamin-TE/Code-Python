import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

arr = np.array([1,2,3,4])
print(arr)
print("add 1", arr+1)
print("multiply", arr * 2)
print("sum", arr.sum())
print("mean", arr.mean())

zeros= np.zeros((2,3))
print(zeros)

ones = np.ones((2,3))
print(ones)

ran= np.random.rand(2,3)
print(ran)

arr2 = np.array([10,15,20,25,30,35])
print(arr2)
print("sum", arr2.sum())
print("mean", arr2.mean())
print("standard deviation", arr2.std())
print("max", arr2.max())
print("Index of max", arr2.argmax())
print("min", arr2.min())
print("Index of min", arr2.argmin())

#Matrix Application: 
a = np.array([[2,3],
              [5,6]])
b = np.array([[10,12],
              [13,15]])
print("Matrix multiplication", a@b)
print("element multiplication", a*b)