import simpy
import random as rand 

intervalo = 10



  

env =  simpy.Environment()
res = simpy.Resource(env, capacity = 1)

RAM = simpy.Container(env, init=100, capacity=100)

