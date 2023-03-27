import math
import rudder_force
import Hull_force
import Propeller_force 
from added_mass_value import *


def model(var, t):

    XP = Propeller_force.propeller(var)
    XR, YR, NR = rudder_force.rudder(var)
    XH, YH, NH = Hull_force.hull(var)
    
    L = l
    X = XH+XP+XR
    Y = YH+YR
    N = NH+NR

    dUdt = (pow(var[0],2)/L)*((X/(mm+mxx))*math.cos(var[1])-(Y/(mm+myy))*math.sin(var[1])-(((mm+myy)/(mm+mxx))-((mm+mxx)/(mm+myy)))*var[2]
            *math.sin(var[1])*math.cos(var[1]))
    dbdt = (var[0]/L)*((mm+mxx)/(mm+myy))*var[2]*pow(math.cos(var[1]), 2)+((mm+myy)/(mm+mxx))*var[2]*pow(math.sin(var[1]), 2)-((1/(mm+mxx))
            *math.sin(var[1])*X)-((1/(mm+myy))*math.cos(var[1])*Y)
    drdt = (var[0]/L)*(N/(Izz+Jzz))-var[2]*(var[0]/L)*((X/(mm+mxx))*math.cos(var[1])-(Y/(mm+myy))*math.sin(var[1])-(((mm+myy)/(mm+mxx))-((mm+mxx)/(mm+myy)))
            *var[2]*math.sin(var[1])*math.cos(var[1]))
    psi= var[0]*var[2]/L
    x0 = var[0]*math.cos(var[3]-var[1])
    y0 = var[0]*math.sin(var[3]-var[1])

    dydt = [dbdt, drdt, dUdt, psi, x0, y0]
    
    return dydt
