from inspect import Parameter
from multiprocessing.pool import TERMINATE
import this
import simpy
import random as rand
proces = 25
memory = 100
intervalo = 10
mark = {}
def new (self, env):
    while (proces != 0):
        mem = rand.randrange(1,10)
        instr = rand.randrange(1,10)
        name = "proces" + proces
        parameters = (mem, instr, name)
        proces =- 1
        return parameters
    
def readynew(self, env, this):
    parameter = new()
    return parameter

def readyold(anc, env):
    Parameter = anc
    return Parameter

def waiting(anc, env, self):
    spec = iter(anc)
    memp = next(spec)
    namep = next(spec)
    mark[namep] = spec, memp
    

def runningnew (self,env):
    proc = readynew()
    ex = iter(proc)
    memp = next(ex)
    interp = rand.randrange(1,2)
    instrp = next(ex)
    namep = next(ex)
    memory =- memp
    instrp =- 3
    if (instrp == 0):
        TERMINATE
    if (interp == 1 & instrp != 0):
        readyold(proc);
    if (interp == 2 & instrp != 0):
        TERMINATE
        
        
        
            

env =  simpy.Environment()
dres = simpy.Resource(env, capacity = 1)

RAM = simpy.Container(env, init=100, capacity=100)

