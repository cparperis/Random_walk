#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:10:46 2020

@author: Christopher
"""
#############################
### Trial of random walks ###
#############################

# Set parameters for 2D random walk trial...
Steps_per_Walk = 500
Walks_per_Trial = 1000

# Import libraries...
import numpy as np

# Function for simulating N random walks...
def RandomWalk2D_Trial(Steps_per_Walk, Walks_per_Trial):

    # Create function for individual random walk of n steps in 2d...
    def analyse_2D_random_walk(n):
        """Return coordinates after random walk of 'n' steps"""
    
        # Unit circle to cartesian...
        def unitcircle2cart(random_distance, random_angle):
            return [random_distance * np.cos(random_angle),
                    random_distance * np.sin(random_angle)]
    
        # Incrementally change cartesian coordinates on every step of walk...
        xy = [0, 0]
        step_distances=[]
        for i in range(n):
            random_angle = np.random.uniform(low=0.0, high=np.pi*2)
            random_distance = np.random.normal(loc=15.0, scale=1.0)
            xy = np.add(xy, unitcircle2cart(random_distance, random_angle))
            step_distances.append(np.copy(random_distance))
            print("Step ", i, " difference: ", (random_distance, random_angle))
            print("Position after step ", i, " = ", str(xy))
            
        # Return final cartsian coordinates of walk,
        # return distance travelled at every step of walk.
        return xy, step_distances

    # Repeating random walk N times...
    def multiwalk(number_of_walks):
        arr=[]
        for m in range(number_of_walks):
            print("\n Random Walk ", m)
            ans=analyse_2D_random_walk(Steps_per_Walk)
            arr.append(np.copy(ans))
        return(arr)

    multi_randomwalk2d=multiwalk(Walks_per_Trial)
    multi_randomwalk_array2d=np.array(multi_randomwalk2d)

    # Return final xy coordinates from all walks,
    # return incremental step distance array from all walks.
    return multi_randomwalk_array2d


#assign variable to 2d random walk trial data
trial=RandomWalk2D_Trial(Steps_per_Walk, Walks_per_Trial)

# Extract xy coordinates from all random walks from the trial
# and put in new array called "final_coordinates_of_walks".
u=0
final=[]
for u in range(len(trial)):
    final.append(trial[u,0])
    u+=1
final_coordinates_of_walks=np.array(final)
print("\n Final (xy) coordinates for each walk in trial: \n",final_coordinates_of_walks)

# Extract incremental step distances from all random 
# walks simulated in the trial and put in new array
# called "Distance_travelled_at_every_step".
l=0
Distance_travelled_at_every_step=[]
for l in range(len(trial)):
    Distance_travelled_at_every_step.append(trial[l,1])
    l+=1
array_of_Distance_travelled_at_every_step=np.array(Distance_travelled_at_every_step)
print("\n Incremental step lengths within each walk: \n", array_of_Distance_travelled_at_every_step)

#%%

#########################
### Analysis of trial ###
#########################

# Compute array of total distance travelled from origin
# at the end of each random walk.

def trialanalysis(Resultof_RandomWalk2D_Trial):
    
    counter1=0
    x=[]
    for counter1 in range(len(Resultof_RandomWalk2D_Trial)):
        x.append(Resultof_RandomWalk2D_Trial[counter1,0])
        counter1+=1
        xy_coordinates=np.array(x)
    
    counter2=0
    stepdistances=[]
    for counter2 in range(len(Resultof_RandomWalk2D_Trial)):
        stepdistances.append(Resultof_RandomWalk2D_Trial[counter2,1])
        counter2+=1
        steps=np.array(stepdistances)    
    
    counter3=0
    meansteps=[]
    for counter3 in range(len(steps)):
        meansteps.append(np.mean(steps[counter3]))
        counter3+=1
        mean_step_increment=np.array(meansteps)    
    
    print("\n Mean step length for each walk of trial: \n",mean_step_increment)
    
    # Compute array of squared displacement from origin
    # at the end of each random walk.
    pythag_A=xy_coordinates[:,0]
    pythag_B=xy_coordinates[:,1]
    SD=np.sqrt((pythag_A*pythag_A)+(pythag_B*pythag_B))
    print("\n Squared displacement for each random walk in trial: \n",SD)


    #Calculate MSD from origin
    MSD=np.mean(SD)
    print("\n MSD from origin: \n", MSD)
    
    return [MSD, mean_step_increment]

#%%
trial500=RandomWalk2D_Trial(500,1000)
trial1000=RandomWalk2D_Trial(1000,1000)
trial1500=RandomWalk2D_Trial(1500,1000)
trial2000=RandomWalk2D_Trial(2000,1000)
trial2500=RandomWalk2D_Trial(2500,1000)
trial3000=RandomWalk2D_Trial(3000,1000)
trial3500=RandomWalk2D_Trial(3500,1000)
trial4000=RandomWalk2D_Trial(4000,1000)
trial4500=RandomWalk2D_Trial(4500,1000)
trial5000=RandomWalk2D_Trial(5000,1000)

step500=trialanalysis(trial500)
step1000=trialanalysis(trial1000)
step1500=trialanalysis(trial1500)
step2000=trialanalysis(trial2000)
step2500=trialanalysis(trial2500)
step3000=trialanalysis(trial3000)
step3500=trialanalysis(trial3500)
step4000=trialanalysis(trial4000)
step4500=trialanalysis(trial4500)
step5000=trialanalysis(trial5000)

print("\n MSD of 500 step walk is ", step500[0])
print("\n MSD of 1000 step walk is ", step1000[0])
print("\n MSD of 1500 step walk is ", step1500[0])
print("\n MSD of 2000 step walk is ", step2000[0])
print("\n MSD of 2500 step walk is ", step2500[0])
print("\n MSD of 3000 step walk is ", step3000[0])
print("\n MSD of 3500 step walk is ", step3500[0])
print("\n MSD of 4000 step walk is ", step4000[0])
print("\n MSD of 4500 step walk is ", step4500[0])
print("\n MSD of 5000 step walk is ", step5000[0])


#%%
trial500_100=RandomWalk2D_Trial(500,100)
trial1000_100=RandomWalk2D_Trial(1000,100)
trial1500_100=RandomWalk2D_Trial(1500,100)
trial2000_100=RandomWalk2D_Trial(2000,100)
trial2500_100=RandomWalk2D_Trial(2500,100)
trial3000_100=RandomWalk2D_Trial(3000,100)
trial3500_100=RandomWalk2D_Trial(3500,100)
trial4000_100=RandomWalk2D_Trial(4000,100)
trial4500_100=RandomWalk2D_Trial(4500,100)
trial5000_100=RandomWalk2D_Trial(5000,100)

step500_100=trialanalysis(trial500_100)
step1000_100=trialanalysis(trial1000_100)
step1500_100=trialanalysis(trial1500_100)
step2000_100=trialanalysis(trial2000_100)
step2500_100=trialanalysis(trial2500_100)
step3000_100=trialanalysis(trial3000_100)
step3500_100=trialanalysis(trial3500_100)
step4000_100=trialanalysis(trial4000_100)
step4500_100=trialanalysis(trial4500_100)
step5000_100=trialanalysis(trial5000_100)



trial500_10=RandomWalk2D_Trial(500,10)
trial1000_10=RandomWalk2D_Trial(1000,10)
trial1500_10=RandomWalk2D_Trial(1500,10)
trial2000_10=RandomWalk2D_Trial(2000,10)
trial2500_10=RandomWalk2D_Trial(2500,10)
trial3000_10=RandomWalk2D_Trial(3000,10)
trial3500_10=RandomWalk2D_Trial(3500,10)
trial4000_10=RandomWalk2D_Trial(4000,10)
trial4500_10=RandomWalk2D_Trial(4500,10)
trial5000_10=RandomWalk2D_Trial(5000,10)

step500_10=trialanalysis(trial500_10)
step1000_10=trialanalysis(trial1000_10)
step1500_10=trialanalysis(trial1500_10)
step2000_10=trialanalysis(trial2000_10)
step2500_10=trialanalysis(trial2500_10)
step3000_10=trialanalysis(trial3000_10)
step3500_10=trialanalysis(trial3500_10)
step4000_10=trialanalysis(trial4000_10)
step4500_10=trialanalysis(trial4500_10)
step5000_10=trialanalysis(trial5000_10)







#%%
trial10000_10=RandomWalk2D_Trial(10000,10)
trial10000_100=RandomWalk2D_Trial(10000,100)
trial10000_1000=RandomWalk2D_Trial(10000,1000)

step10000_10=trialanalysis(trial10000_10)
step10000_100=trialanalysis(trial10000_100)
step10000_1000=trialanalysis(trial10000_1000)

print("\n MSD of 10,000 step walk, 10 walk trial is ", step100000_10[0])
print("\n MSD of 10,000 step walk, 100 walk trial is ", step100000_100[0])
print("\n MSD of 10,000 step walk, 1000 walk trial is ", step100000_1000[0])
#%%

print("\n MSD of 500 step walk is ", step500_100[0])
print("\n MSD of 1000 step walk is ", step1000_100[0])
print("\n MSD of 1500 step walk is ", step1500_100[0])
print("\n MSD of 2000 step walk is ", step2000_100[0])
print("\n MSD of 2500 step walk is ", step2500_100[0])
print("\n MSD of 3000 step walk is ", step3000_100[0])
print("\n MSD of 3500 step walk is ", step3500_100[0])
print("\n MSD of 4000 step walk is ", step4000_100[0])
print("\n MSD of 4500 step walk is ", step4500_100[0])
print("\n MSD of 5000 step walk is ", step5000_100[0])
#%%
print("\n MSD of 500 step walk is ", step500[0])
print("\n MSD of 1000 step walk is ", step1000[0])
print("\n MSD of 1500 step walk is ", step1500[0])
print("\n MSD of 2000 step walk is ", step2000[0])
print("\n MSD of 2500 step walk is ", step2500[0])
print("\n MSD of 3000 step walk is ", step3000[0])
print("\n MSD of 3500 step walk is ", step3500[0])
print("\n MSD of 4000 step walk is ", step4000[0])
print("\n MSD of 4500 step walk is ", step4500[0])
print("\n MSD of 5000 step walk is ", step5000[0])
#%%
print("\n MSD of 500 step walk is ", step500_10[0])
print("\n MSD of 1000 step walk is ", step1000_10[0])
print("\n MSD of 1500 step walk is ", step1500_10[0])
print("\n MSD of 2000 step walk is ", step2000_10[0])
print("\n MSD of 2500 step walk is ", step2500_10[0])
print("\n MSD of 3000 step walk is ", step3000_10[0])
print("\n MSD of 3500 step walk is ", step3500_10[0])
print("\n MSD of 4000 step walk is ", step4000_10[0])
print("\n MSD of 4500 step walk is ", step4500_10[0])
print("\n MSD of 5000 step walk is ", step5000_10[0])


