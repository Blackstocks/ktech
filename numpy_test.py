# import numpy as np


# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr)
# print(arr[:5:3])
# print(np.__version__)

# # copy vs view?
# import numpy as np
# # arr = np.array([1,2,3,4,5,6,7,8,9,10])
# # x = arr.copy()
# # arr[1] = 100
# # y = arr.view()
# # print(x)
# # print(y)

# arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
# arr2 = np.array([11,12,13,15,16,17,18,19,14,20])
# arr3 = np.hstack((arr1,arr2))
# arr4 = np.vstack((arr1,arr2))
# arr5 = np.concatenate((arr1,arr2))
# arr6 = np.dstack((arr1,arr2))
# print(arr3)
# print(arr4)
# print(arr5)
# print(arr6)
# arr7 = np.split(arr1,2)
# print(arr7)

# x=np.where(arr2 == 14)
# print(x)

# # x = np.where(arr2%2 == 1)
# y = np.searchsorted(arr2,14)
# print(y)
# Normal distribution(Gaussian distribution):
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# # x = random.normal(loc=1,scale=3,size=(2,3))
# # Displaying the distribution of a normal distribution:
# sns.displot(random.normal(size=100),kind='kde')
# # sns.distplot(x)
# plt.show()
# print(x)


# Binomial distribution(Bernoulli distribution):
# nCr = n! / r!(n-r)!
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.binomial(size=10,n=3,p=0.5),kind='kde')
# plt.show()
# x = random.binomial(size=10,n=3,p=0.5)
# print(x)


# data = {
#     "normal": random.normal(size=100),
#     "binomial": random.binomial(size=100,n=3,p=0.5),

# }

# sns.displot(data,kind='kde')
# plt.show()

# *****************numpy universal function(ufunc)*****************

# import numpy as np
# def newadd(x,y):
#     return x+y

# newadd = np.frompyfunc(newadd,2,1)
# print(newadd(1,2))



import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)
# variable_name = library.function_name(argument)
# print(myvar)
# print(pd.__version__)


a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)