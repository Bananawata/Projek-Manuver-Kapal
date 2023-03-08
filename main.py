

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