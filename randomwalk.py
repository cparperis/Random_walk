#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:10:46 2020

@author: Christopher
"""

#Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#3D Diffusion#

#Create function for random walk of n steps in 3d
def random_walk3D(n):
    """Return coordinates after random walk of 'n' steps"""
    
    #Define function for converting spherical to cartesian coordinates
    def spher2cart(random_rho, random_theta, random_phi):
        return [random_rho * np.sin(random_phi) * np.cos(random_theta),
                random_rho * np.sin(random_phi) * np.sin(random_theta),
                random_rho * np.cos(random_phi)]
    
    #Iterate over n steps of random walk: take a random step in spherical coordinates, update cartesian coordinates after every step
    xyz = [0, 0, 0]
    trajectory = []
    for i in range(n):
        random_theta = np.random.uniform(low=0.0, high=np.pi*2)
        random_phi = np.random.uniform(low=0.0, high=np.pi)
        random_rho = np.random.normal(loc=15.0, scale=1.0)
        xyz = np.add(xyz, spher2cart(random_rho, random_theta, random_phi))
        
        trajectory.append(np.copy(xyz))
        
        str(random_phi)
        str(random_rho)
        str(random_theta)
        print("Random spherical for step ", i, " is ", (random_rho, random_theta, random_phi))
        print("deltaCartesian for step ", i, " is ", spher2cart(random_rho, random_theta, random_phi))
        print("Position after step ", i, " = ", str(xyz), "\n")
    trajectory_array=np.array(trajectory)
    return trajectory_array

#xyz = cartesian coordinates after random walk of n steps
(xyz) = random_walk3D(5000)

print("Trajectory: \n", xyz)

#%%

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z = xyz[:,2]
y = xyz[:,1]
x = xyz[:,0]

ax.plot(x, y, z, label='3D Random Walk of 10k Steps', )
ax.legend()

plt.show

#%%

#2D Diffusion

#Create function for random walk of n steps in 2d
def random_walk2D(n):
    """Return coordinates after random walk of 'n' steps"""
    
    #unit circle to cartesian
    def unitcircle2cart(random_distance, random_angle):
        return [random_distance * np.cos(random_angle),
                random_distance * np.sin(random_angle),
                0]
    
    
    xy = [0, 0, 0]
    trajectory = []
    for i in range(n):
        random_angle = np.random.uniform(low=0.0, high=np.pi*2)
        random_distance = np.random.normal(loc=15.0, scale=1.0)
        xy = np.add(xy, unitcircle2cart(random_distance, random_angle))
        
        trajectory.append(np.copy(xy))
        
       
    trajectory_array = np.array(trajectory)
    return trajectory_array

#xyz = cartesian coordinates after random walk of n steps
(xy) = random_walk2D(1000000)

print("Trajectory: \n", str(xy))



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z = xy[:,2]
y = xy[:,1]
x = xy[:,0]

ax.plot(x, y, z, label=('Random Walk of 100 Steps'))
ax.legend()

plt.show




#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.fill(x, stats.norm.pdf(x, mu, sigma), color='#E76E20')

plt.show()

#%%
import seaborn as sns

value = np.random.normal(loc=5,scale=3,size=1000)
sns.distplot(value)

#%%
#Multile 2D Diffusion
Steps_per_Walk=600
Walks_per_Trial=10

#Create function for random walk of n steps in 2d
def analyse_2D_random_walk(n):
    """Return coordinates after random walk of 'n' steps"""
    
    #unit circle to cartesian
    def unitcircle2cart(random_distance, random_angle):
        return [random_distance * np.cos(random_angle),
                random_distance * np.sin(random_angle)]
    
        
    xy = [0, 0]
    step_distances=[]
    for i in range(n):
        random_angle = np.random.uniform(low=0.0, high=np.pi*2)
        random_distance = np.random.normal(loc=15.0, scale=1.0)
        xy = np.add(xy, unitcircle2cart(random_distance, random_angle))
        step_distances.append(np.copy(random_distance))
        print("Step ", i, " difference: ", (random_distance, random_angle))
        print("Position after step ", i, " = ", str(xy))

    return xy, step_distances










def multiwalk(number_of_walks):
    arr=[]
    for m in range(number_of_walks):
        print("\n Random Walk ", m)
        ans=analyse_2D_random_walk(Steps_per_Walk)
        arr.append(np.copy(ans))
    return(arr)

multi_randomwalk2d=multiwalk(Walks_per_Trial)
multi_randomwalk_array2d=np.array(multi_randomwalk2d)

print(multi_randomwalk_array2d)

u=0
final=[]
for u in range(len(multi_randomwalk_array2d)):
    final.append(multi_randomwalk_array2d[u,0])
    u+=1
final_coordinates_of_walk=np.array(final)
print("\n Final coordinates for each walk in trial: \n",final_coordinates_of_walk)

l=0
Distance_travelled_at_every_step=[]
for l in range(len(multi_randomwalk_array2d)):
    Distance_travelled_at_every_step.append(multi_randomwalk_array2d[l,1])
    l+=1
array_of_Distance_travelled_at_every_step=np.array(Distance_travelled_at_every_step)
print("\n Incremental step lengths within each walk: \n", array_of_Distance_travelled_at_every_step)

#%%
print(multi_randomwalk_array2d)


#%%
final=np.array(eg)
print(final)
#%%

first=final[1,0]
print(first)

#%%
dist_from_origin=[]
for i in range(len(final[:,0])):
    d1=(final[i,0])*(final[i,0])
    d2=(final[i,1])*(final[i,1])
    d3=np.sqrt(d1+d2)
    dist_from_origin.append(d3)
print(dist_from_origin)






#%%

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z = 0
y = eg[:,0]
x = eg[:,1]

ax.plot(x, y, z, label='3D Random Walk of 10k Steps', )
ax.legend()

plt.show



#%%



#xyz = cartesian coordinates after random walk of n steps
test = analyse_2D_random_walk(5)

xy=test[0]
array_of_step_distances=test[1]
#%%
dim1=xy[0]
dim2=xy[1]
dist=np.sqrt((dim1*dim1)+(dim2*dim2))
print(array_of_step_distances,"\n")
print(xy)
#%%

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z = xy[:,2]
y = xy[:,1]
x = xy[:,0]

ax.plot(x, y, z, label=('Random Walk of 100 Steps'))
ax.legend()

plt.show

#%%
#Multile 2D Diffusion

Steps_per_Walk = 1000
Walks_per_Trial = 100

import numpy as np

def RandomWalk2D_Trial(Steps_per_Walk, Walks_per_Trial):

    #Create function for random walk of n steps in 2d
    def analyse_2D_random_walk(n):
        """Return coordinates after random walk of 'n' steps"""
    
        #unit circle to cartesian
        def unitcircle2cart(random_distance, random_angle):
            return [random_distance * np.cos(random_angle),
                    random_distance * np.sin(random_angle)]
    
        
        xy = [0, 0]
        step_distances=[]
        for i in range(n):
            random_angle = np.random.uniform(low=0.0, high=np.pi*2)
            random_distance = np.random.normal(loc=15.0, scale=1.0)
            xy = np.add(xy, unitcircle2cart(random_distance, random_angle))
            step_distances.append(np.copy(random_distance))
            print("Step ", i, " difference: ", (random_distance, random_angle))
            print("Position after step ", i, " = ", str(xy))

        return xy, step_distances


    def multiwalk(number_of_walks):
        arr=[]
        for m in range(number_of_walks):
            print("\n Random Walk ", m)
            ans=analyse_2D_random_walk(Steps_per_Walk)
            arr.append(np.copy(ans))
        return(arr)

    multi_randomwalk2d=multiwalk(Walks_per_Trial)
    multi_randomwalk_array2d=np.array(multi_randomwalk2d)

    return multi_randomwalk_array2d



trial=RandomWalk2D_Trial(Steps_per_Walk, Walks_per_Trial)

u=0
final=[]
for u in range(len(trial)):
    final.append(trial[u,0])
    u+=1
final_coordinates_of_walk=np.array(final)
print("\n Final (xy) coordinates for each walk in trial: \n",final_coordinates_of_walk)

l=0
Distance_travelled_at_every_step=[]
for l in range(len(trial)):
    Distance_travelled_at_every_step.append(trial[l,1])
    l+=1
array_of_Distance_travelled_at_every_step=np.array(Distance_travelled_at_every_step)
print("\n Incremental step lengths within each walk: \n", array_of_Distance_travelled_at_every_step)

#%%
print(trial1[])
