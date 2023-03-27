from scipy.integrate import odeint
import matplotlib.pyplot as plt
from Maneuver import model
import numpy as np

print("Masukkan data")

print("Ship Dimension")
m = float(input("Ship Mass (m): "))
cb = float(input("Block Coefficient (Cb): "))
l = float(input("Ship Length (L): "))
b = float(input("Breadth (B): "))
d = float(input("Draft (d): "))
rho = float(input("Fluid Density (rho): "))

print(30*"=")
print("Propeller")
n = float(input("Propeller Revolution (n): "))
dp = float(input("Propeller Diameter (Dp): "))
P = float(input("Propeller Pitch (P): "))

print(30*"=")
print("Rudder")
AR = float(input("Rudder Area (AR): "))
KR = float(input("Aspect Ratio of Rudder (KR): "))
hR = float(input("Rudder Height (hR): "))

# kondisi awal
y = [0.337, 0, 0, 0, 0, 0] #[U, beta, r, psi, x0, y0]

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

t = makeTime(0, 10, 1001)
#t = np.linspace(0, 2, 101)


# selesaikan persamaan diferensial
dydt = odeint(model, y, t)

p1 = plt.plot(dydt[:, 4],dydt[:, 5],'-')
plt.title('Grafik Manuever Kapal')
plt.xlabel('time(t)')
plt.ylabel("Derajat($^o$)")
#plt.legend( (p1[0]), ('Beta'), loc='best' )
plt.show()
#print(dydt)