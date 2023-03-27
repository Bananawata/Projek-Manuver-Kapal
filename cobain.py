import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from rudder_force import XR, YR, NR
from Hull_force import XH, YH, NH
from Propeller_force import XP 
from added_mass_value import mm, mxx, myy, izz, Izz

def model_beta(b, t):
    dydt = (U/L)*((mm+mxx)/(mm+myy))*r*pow(math.cos(b), 2)+((mm+myy)/(mm+mxx))*r*pow(math.sin(b), 2)-((1/(mm+mxx))*math.sin(b)*X)-((1/(mm+myy))*math.cos(b)*Y)
    return dydt

def model_r(r, t):
    dydt = (U/L)*(N/(Izz+izz))-r*(U/L)*((X/(mm+mxx))*math.cos(b)-(Y/(mm+myy))*math.sin(b)-(((mm+myy)/(mm+mxx))-((mm+mxx)/(mm+myy)))*r*math.sin(b)*math.cos(b))
    return dydt

def model_U(U, t):
    dydt = (pow(U,2)/L)*((X/(mm+mxx))*math.cos(b)-(Y/(mm+myy))*math.sin(b)-(((mm+myy)/(mm+mxx))-((mm+mxx)/(mm+myy)))*r*math.sin(b)*math.cos(b))
    return dydt


# kondisi awal
y0 = 0
U, L, r, b = 1, 1, 1, 1
# waktu
def makeTime(start, end, dot):
    t = []
    jump = (start+end)/(dot-1)

    t.append(0)
    iterJump = jump
    for i in range(dot-1):
        t.append(iterJump)
        iterJump = iterJump + jump

    return t

t = makeTime(0, 2, 101)

X = XH+XP+XR
Y = YH+YR
N = NH+NR

# selesaikan persamaan diferensial
beta = odeint(model_beta, y0, t)
rr = odeint(model_r, y0, t)
UU = odeint(model_U, y0, t)

p1 = plt.plot(t,beta,'-')
p2 = plt.plot(t,rr,'-')
p3 = plt.plot(t,UU,'-')
plt.title('Grafik Manuever Kapal')
plt.xlabel('time(t)')
plt.ylabel("Derajat($^o$)")
plt.legend( (p1[0], p2[0], p3[0]), ('Beta', 'yaw', 'ship speed'), loc='best' )
plt.show()