import simpy
import random as rand
proces = 25
memory = 100
intervalo = 10
def new (self, env):
    while (proces != 0):
        mem = rand.randrange(1,10)
        instr = rand.randrange(1,10)
        name = "proces" + proces
        parameters = (mem, instr, name)
        return parameters
    
def ready():
    new()
    parameter = [new.mem, new.instr, new.name]
        

env =  simpy.Environment()
dres = simpy.Resource(env, capacity = 1)

RAM = simpy.Container(env, init=100, capacity=100)

