import math
pi = math.pi

def solid_T_from_tau(tau, c):  # tau in MPa, c in mm -> T in N*mm
    return tau * pi * c**3 / 2

def solid_tau_from_T(T, c):
    return 2*T/(pi*c**3)

def hollow_J(c2,c1):
    return (pi/2)*(c2**4-c1**4)

def hollow_T_from_tau(tau,c2,c1):
    return tau*hollow_J(c2,c1)/c2

def hollow_tau_from_T(T,c2,c1):
    return T*c2/hollow_J(c2,c1)

print("=== 3.2 ===")
c1,c2=15,22.5
T = hollow_T_from_tau(45,c2,c1)
print("T(a) N*mm=",T,"N*m=",T/1000)
A_hollow = pi*(c2**2-c1**2)
c_solid = math.sqrt(A_hollow/pi)
tau_solid = solid_tau_from_T(T,c_solid)
print("A_hollow=",A_hollow,"c_solid=",c_solid,"tau_solid=",tau_solid)

print("=== 3.4 ===")
c2,c1=20,15
T = hollow_T_from_tau(52,c2,c1)
print("T N*m=",T/1000)

print("=== 3.6 ===")
c=10
Ta = solid_T_from_tau(80,c)
print("Ta N*m=",Ta/1000)
A = pi*c**2
# hollow: c1=c2/2, area = pi*c2^2*(3/4) = A
c2h = math.sqrt(A/(pi*0.75))
c1h = c2h/2
Tb = hollow_T_from_tau(80,c2h,c1h)
print("c2h=",c2h,"c1h=",c1h,"Tb N*m=",Tb/1000)

print("=== 3.8 ===")
T_AB = solid_T_from_tau(84,19)
T_CD = hollow_T_from_tau(50,37.5,31.5)
print("T_AB N*m=",T_AB/1000,"T_CD N*m=",T_CD/1000,"Tmax=",min(T_AB,T_CD)/1000)

print("=== 3.9/3.10 ===")
tauAB9 = solid_tau_from_T(300000,15)
tauBC9 = solid_tau_from_T(700000,23)
print("tauAB9=",tauAB9,"tauBC9=",tauBC9,"govern=",max(tauAB9,tauBC9))
govern = max(tauAB9,tauBC9)
c_new = (2*700000/(pi*govern))**(1/3)
print("3.10 c_BC_new=",c_new,"d=",2*c_new)

print("=== 3.11/3.12 ===")
c1h=4
for name,T,c2 in [("AB",48000,7.5),("BC",192000,9),("CD",252000,10.5)]:
    tau_solid = solid_tau_from_T(T,c2)
    tau_hollow = hollow_tau_from_T(T,c2,c1h)
    print(name,"solid tau=",tau_solid,"hollow(8mm hole) tau=",tau_hollow)

print("=== 3.13/3.14 ===")
TAB=2.8e6; TBC=1.4e6; TCD=0.5e6
tauAB=solid_tau_from_T(TAB,28)
tauBC=solid_tau_from_T(TBC,24)
tauCD=solid_tau_from_T(TCD,24)
print("tauAB=",tauAB,"tauBC=",tauBC,"tauCD=",tauCD)
govern14 = max(tauAB,tauBC,tauCD)
print("govern=",govern14)
c_new_BC = (2*TBC/(pi*govern14))**(1/3)
print("3.14 new c_BC=",c_new_BC,"d=",2*c_new_BC)

print("=== 3.16 ===")
T_AB16=solid_T_from_tau(100,18)
T_BC16=solid_T_from_tau(60,20)
print("T_AB16=",T_AB16/1000,"T_BC16=",T_BC16/1000,"Tmax=",min(T_AB16,T_BC16)/1000)

print("=== 3.18 ===")
T18 = solid_T_from_tau(25,15)  # BC aluminum d=30
print("T18=",T18,T18/1000)
J_AB18 = T18*12.5/50
c1_4 = 12.5**4 - 2*J_AB18/pi
print("c2^4=",12.5**4,"J_AB18=",J_AB18,"c1^4=",c1_4)
c1_18 = c1_4**0.25
print("c1_18=",c1_18,"d1=",2*c1_18)

print("=== 3.20 ===")
T_AB20 = solid_T_from_tau(85,30)
T_CD20 = hollow_T_from_tau(54,45,39)
print("T_AB20=",T_AB20/1000,"T_CD20=",T_CD20/1000,"Tmax=",min(T_AB20,T_CD20)/1000)

print("=== 3.22 ===")
TC=600000
c_BC22 = (2*TC/(pi*60))**(1/3)
F = TC/100
T_EF_int = F*60
c_EF22 = (2*T_EF_int/(pi*60))**(1/3)
print("c_BC22=",c_BC22,"d=",2*c_BC22)
print("T_EF_int=",T_EF_int,"c_EF22=",c_EF22,"d=",2*c_EF22)

print("=== 3.24 ===")
T_AB24 = solid_T_from_tau(60,24)
T_CD24 = solid_T_from_tau(60,33)
T_A_equiv = T_CD24*(80/240)
print("T_AB24=",T_AB24/1000,"T_CD24=",T_CD24/1000,"T_A_equiv_from_CD=",T_A_equiv/1000)
print("governing max T at A=",min(T_AB24,T_A_equiv)/1000)

print("=== 3.26 ===")
T_CD26=1000000
T_AB26=T_CD26*(100/40)
c_CD26=(2*T_CD26/(pi*60))**(1/3)
c_AB26=(2*T_AB26/(pi*60))**(1/3)
print("T_AB26=",T_AB26,"c_CD26=",c_CD26,"d=",2*c_CD26,"c_AB26=",c_AB26,"d=",2*c_AB26)

print("=== 3.28 ===")
T_AB28=120000
T_CD28=T_AB28*(30/25)
T_EF28=T_CD28*(60/75)
print("T_CD28=",T_CD28,"T_EF28=",T_EF28)
for name,T in [("AB",T_AB28),("CD",T_CD28),("EF",T_EF28)]:
    c=(2*T/(pi*75))**(1/3)
    print(name,"c=",c,"d=",2*c)

print("=== 3.30 ratio table ===")
for k in [1.00,0.95,0.75,0.50,0.0]:
    ratio = (k**2+1)/(1+k)
    print("c1/c2=",k,"tau_o/tau_max=",ratio)
