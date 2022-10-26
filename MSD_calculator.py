#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:13:25 2020

@author: Christopher
"""

#Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Define step length for RW
StepLength=100


#2D Diffusion

#Create function for random walk of n steps in 2d
def random_walk2D(n):
    """Return coordinates after random walk of 'n' steps"""    
    #unit circle to cartesian
    def unitcircle2cart(random_distance, random_angle):
        return [random_distance * np.cos(random_angle),
                random_distance * np.sin(random_angle),
                0]

    #Define initial cartesian coordinates of 0     
    xy = [0, 0, 0]
    #Create a 'trajectory' list to iteratively append random coordinates into
    trajectory = []
    for i in range(n):        
        #Create random angle for step in trajectory
        random_angle = np.random.uniform(low=0.0, high=np.pi*2)        
        #Create random distance for step in trajectory
        random_distance = np.random.normal(loc=15.0, scale=1.0)
        
        #Update trajectory list for step 'i' in RW
        xy = np.add(xy, unitcircle2cart(random_distance, random_angle))        
        trajectory.append(np.copy(xy))
        
       
    trajectory_array = np.array(trajectory)
    return trajectory_array

#xyz = cartesian coordinates after random walk of n steps
trajectory_coordinates = random_walk2D(StepLength)

print("Trajectory: \n", str(trajectory_coordinates))


#Plot trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z = trajectory_coordinates[:,2]
y = trajectory_coordinates[:,1]
x = trajectory_coordinates[:,0]

#Label plot with step length of RW
TitleStepLength=str(StepLength/1000)
PlotTitle='Random Walk of '+ TitleStepLength+ ' K Steps'

ax.plot(x, y, z, label=(PlotTitle))
ax.legend()

plt.show



def MSD(trajectory):
     
#    Set half total_steps as the maximum
#    step lag to measure squared displacement 
#    between points
#    (Round down if an odd number of steps)
    lagstep_range=int((len(trajectory[:,0])/2))

#   Extract x coordinates as two identical vectors
    x_vector=trajectory[:,0]
    y_vector=trajectory[:,1]
    print('\n \n xVector: \n', x_vector)
    print('\n \n yVector: \n', y_vector)

    MSD_vector=[]

    for i in range(1,lagstep_range+1):
        x_difference=x_vector[i:]-x_vector[:-i]
        print("\n \n Iteration number", i, "\n (x difference):\n", x_difference)
        x_differece_squared=x_difference*x_difference
        print(" x square difference:\n", x_differece_squared)
        
        y_difference=y_vector[i:]-y_vector[:-i]
        y_differece_squared=y_difference*y_difference
        print("\n (y difference):\n", y_difference)
        print(" y square difference:\n", y_differece_squared)
        
        squared_displacement=x_differece_squared+y_differece_squared
        print("\n squared displacement:\n", squared_displacement)
        
        MSD=np.mean(squared_displacement)
        print(" MSD:\n", MSD)
        MSD_vector.append(np.copy(MSD))
        
            
    print("\n \n MSD vector:\n",MSD_vector)
    MSD_plot_values=np.array(MSD_vector)
    return(MSD_plot_values)
 


MSD_data=MSD(trajectory_coordinates)

x_axis_values=list(range(1,len(MSD_data)+1))

def multiMSD(randomwalk_steps, randomwalk_repeats):
     
    All_MSDs=[]
    
    for i in range(randomwalk_repeats):
        coordinates=random_walk2D(randomwalk_steps)
        iteration=MSD(coordinates)
        All_MSDs.append(np.copy(iteration))
    All_MSDs_array=np.array(All_MSDs)
    return(All_MSDs_array)


#%%

testMSDs=multiMSD(200, 3000)

x_axis=list(range(1,len(testMSDs[0])+1))


average_MSD_line=np.average(testMSDs, axis=0)
std_MSD=np.std(testMSDs, axis=0)

std_1above = average_MSD_line + std_MSD
std_1below = average_MSD_line - std_MSD


print('average_MSD_line: \n', average_MSD_line)
print('\n \n std_MSD: \n', std_MSD)
print('\n \n 1 std above the mean: \n', std_1above)
print('\n \n 1std below the mean: \n', std_1below)


for i in testMSDs:
    plt.plot(x_axis, i, color='black', alpha=0.03)
plt.plot(x_axis, average_MSD_line, '.', color='#EF0900')
plt.plot(x_axis, std_1above, 'r-', alpha=0.5)
plt.plot(x_axis, std_1below, 'r-', alpha=0.5)


plt.title('Random Walk of 200 Steps \n N=3000 \n Error = $1\\sigma$ above & below mean', fontsize=17)
plt.xlabel('$\\delta$ Steps', fontsize=14)
plt.ylabel('MSD$_{(A.U.^2)}$', fontsize=14)

plt.fill_between(x_axis, std_1below, std_1above, facecolor='red', alpha='0.5')
plt.show()