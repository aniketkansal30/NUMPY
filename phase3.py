import numpy as np
import matplotlib.pyplot as plt
# Data Structure: [restaurant_id,2021,2022,2023,2024]
sales_data=np.array([
    [1,150000,180000,220000,250000], #Haldiram
    [2,120000,140000,160000,190000], #Bikanerwala
    [3,200000,230000,260000,300000], #Dominos
    [4,180000,210000,240000,270000], #Macdonalds
    [5,160000,185000,205000,230000]  #Starbucks
])
print("===Zomato Sales Analysis===")
print("\n Sales data shape",sales_data.shape)
print("\n Sample data for first 3 restaurants",sales_data[0:3])
# Total sales per year
print(np.sum(sales_data,axis=0))
yearly_total=np.sum(sales_data[:,1:],axis=0)  #axis 0 means column and axis 1 means row
print(yearly_total)
# Minimum sales per restaurant
min_sales=np.min(sales_data[:,1:],axis=1)
print(min_sales)
# Maximum sales per year
max_sales=np.max(sales_data[:,1:],axis=0)
print(max_sales)
# Average sales per restaurant
avg_sales=np.mean(sales_data[:,1:],axis=1)
print(avg_sales)
# Cummulative sale
cumsum=np.cumsum(sales_data[:,1:],axis=1)
print(cumsum)

# MATPLOT
plt.figure(figsize=(10,6))
plt.plot(np.mean(cumsum,axis=0))
plt.title("Average cumulative sales across all restaurants")
plt.xlabel=("Years")
plt.ylabel=("Sales")
plt.grid(True)
plt.show()

# physics h ek dum vector 
vec1=np.array([1,2,3,4,5])
vec2=np.array([6,7,8,9,10])
print("Vector addition:",vec1+vec2)
print("Vector multiplication:",vec1*vec2)
print("Dot product:",np.dot(vec1,vec2))
angle=np.arccos(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
print(angle)