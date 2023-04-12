import openpyxl

wb = openpyxl.load_workbook("input.xlsx",)
sheet = wb.active

m = sheet['B2'].value #nilai sebenarnya mm = 0.271
cb = sheet['B3'].value
l = sheet['B4'].value
b = sheet['B5'].value
d = sheet['B6'].value
rho = sheet['B7'].value
Izz = sheet['B17'].value #input dari user sdh non dimensional

mx = m * 0.05
my = m * (0.882 - 0.54 * cb * (1-1.6*d/b)- 0.156 * (1-0.673*cb) * l/b  + 0.826 * d/b * l/b*(1-0.678*d/b) - 0.638 * cb * d/b * l/b * (1-0.669*d/b))
jz = m * (1/100 * (33 - 76.85 * cb * (1-0.784*cb) + 3.43 * l/b * (1-0.63*cb))) ** 2

mm = m/(1/2*rho*(l**2)*d)
mxx = mx/(1/2*rho*(l**2)*d)
myy = my/(1/2*rho*(l**2)*d)
Jzz = jz/(1/2*rho*(l**4)*d)

# print(mx,my,jz,mm,mxx,myy,Izz)
