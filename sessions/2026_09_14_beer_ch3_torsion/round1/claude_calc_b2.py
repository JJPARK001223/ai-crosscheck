import math
pi=math.pi

def Jh(c2,c1): return (pi/2)*(c2**4-c1**4)
def Js(c): return pi*c**4/2
def tau_s(T,c): return 2*T/(pi*c**3)
def tau_h(T,c2,c1): return T*c2/Jh(c2,c1)
def T_s_allow(tau,c): return tau*pi*c**3/2
def T_h_allow(tau,c2,c1): return tau*Jh(c2,c1)/c2

print("=== 3.32 ===")
c2,c1=9,6
G=27000.0
phi=4*pi/180
L=1250.0
J=Jh(c2,c1)
T=phi*J*G/L
print("J=",J,"T=",T,"N*mm =",T/1000,"N*m")
A=pi*(c2**2-c1**2)
c_s=math.sqrt(A/pi)
phi_s=T*L/(Js(c_s)*G)
print("A=",A,"c_s=",c_s,"phi_s(rad)=",phi_s,"deg=",math.degrees(phi_s))

print("=== 3.34 ===")
G=77200.0
c=100.0
Lm=1500.0*1000
phi=4*pi
tau=phi*G*c/Lm
print("tau=",tau)

print("=== 3.36: statically indeterminate, both ends fixed ===")
# segments AB(30mm,0.6m) BC(30mm,0.8m) CD(36mm,1.0m) DE(36mm,0.5m)
# torques at B=400,C=900,D=500 (same direction), A and E fixed
# unknown reaction T_A; internal: AB=T_A, BC=T_A+400, CD=T_A+1300, DE=T_A+1800
# compatibility: sum(T_i*L_i/J_i)=0 (G cancels, same material)
cAB=15.0; cBC=15.0; cCD=18.0; cDE=18.0
LAB,LBC,LCD,LDE=600.,800.,1000.,500.
JAB=Js(cAB); JBC=Js(cBC); JCD=Js(cCD); JDE=Js(cDE)
# sum: TA*LAB/JAB + (TA+400000)*LBC/JBC + (TA+1300000)*LCD/JCD + (TA+1800000)*LDE/JDE = 0
coef = LAB/JAB + LBC/JBC + LCD/JCD + LDE/JDE
const = 400000*LBC/JBC + 1300000*LCD/JCD + 1800000*LDE/JDE
TA = -const/coef
print("TA=",TA)
T_AB=TA; T_BC=TA+400000; T_CD=TA+1300000; T_DE=TA+1800000
print("T_AB=",T_AB,"T_BC=",T_BC,"T_CD=",T_CD,"T_DE=",T_DE)
G=27000.0
phi_CB = T_BC*LBC/(JBC*G)   # twist between B and C (segment BC)
phi_DB = (T_BC*LBC/JBC + T_CD*LCD/JCD)*(1/G)  # from B to D = BC+CD
print("phi(C-B) rad=",phi_CB,"deg=",math.degrees(phi_CB))
print("phi(D-B) rad=",phi_DB,"deg=",math.degrees(phi_DB))

print("=== 3.38 ===")
c_al=18.0
J_al=Js(c_al)
G_al=27000.0
c2_br,c1_br=30.,20.
J_br=Jh(c2_br,c1_br)
G_br=39000.0
T_AB38=800000.0
T_BC38=800000.0+1600000.0
T_CD38=T_BC38
phiA=(T_AB38*400/(J_al*G_al)) + (T_BC38*375/(J_al*G_al)) + (T_CD38*250/(J_br*G_br))
print("J_al=",J_al,"J_br=",J_br)
print("phiA rad=",phiA,"deg=",math.degrees(phiA))

print("=== 3.39/3.40 (spindle+sleeve, ds=40, sleeve OD75 t6) ===")
c_sp=20.0
c2_sl,c1_sl=37.5,31.5
tau_all=120.0
G=77000.0
T_sp_lim=T_s_allow(tau_all,c_sp)
T_sl_lim=T_h_allow(tau_all,c2_sl,c1_sl)
print("T_sp_lim=",T_sp_lim,"T_sl_lim=",T_sl_lim,"govern=",min(T_sp_lim,T_sl_lim))
Tgov=min(T_sp_lim,T_sl_lim)
J_sp=Js(c_sp); J_sl=Jh(c2_sl,c1_sl)
phiA_39 = Tgov*300/(J_sp*G) + Tgov*200/(J_sl*G)
print("3.39 phiA rad=",phiA_39,"deg=",math.degrees(phiA_39))
# 3.40: (a) max T such that sleeve's own twist <=0.375deg AND stress<=120 both members
phi_sl_limit=0.375*pi/180
T_from_phi = phi_sl_limit*J_sl*G/200
print("T_from_sleeve_phi=",T_from_phi)
T40 = min(T_sp_lim,T_sl_lim,T_from_phi)
print("3.40(a) T=",T40)
phiA_40 = T40*300/(J_sp*G) + T40*200/(J_sl*G)
print("3.40(b) phiA rad=",phiA_40,"deg=",math.degrees(phiA_40))

print("=== 3.42 ===")
tau_all=60.0
c_AB,c_CD,c_EF=10.,12.5,20.
T_AB_lim=T_s_allow(tau_all,c_AB)
T_CD_lim=T_s_allow(tau_all,c_CD)
T_EF_lim=T_s_allow(tau_all,c_EF)
# T_CD=2.5*T, T_EF=7.5*T
T_from_AB=T_AB_lim
T_from_CD=T_CD_lim/2.5
T_from_EF=T_EF_lim/7.5
print("from AB=",T_from_AB,"from CD=",T_from_CD,"from EF=",T_from_EF)
Tmax42=min(T_from_AB,T_from_CD,T_from_EF)
print("Tmax=",Tmax42, Tmax42/1000)

print("=== 3.44 (gear train, phi_A=(Tl/JG)(1+n^2+n^4)) ===")
T=600.0; l=60.0; d=2.0; G=77000.0; n=2
c=d/2
J=Js(c)
phiA=(T*l/(J*G))*(1+n**2+n**4)
print("J=",J,"phiA rad=",phiA,"deg=",math.degrees(phiA))

print("=== 3.46 ===")
tau_all=60.0
T_AB46=800000.0
c_stress = (2*T_AB46/(pi*tau_all))**(1/3)
print("c_stress=",c_stress,"d=",2*c_stress)
G=77000.0
phi_limit=1.5*pi/180
LAB,LBC=400.,600.
TAB,TBC=800000.,500000.
# phi_total = TAB*LAB/(J*G) + TBC*LBC/(J*G) <= phi_limit
J_needed = (TAB*LAB+TBC*LBC)/(phi_limit*G)
c_stiff = (2*J_needed/pi)**0.25
print("J_needed=",J_needed,"c_stiff=",c_stiff,"d=",2*c_stiff)
print("governing d=",max(2*c_stress,2*c_stiff))

print("=== 3.48 ===")
P=600.0
lever=300.0
T48=P*lever
tau_all=80.0
c_stress48=(2*T48/(pi*tau_all))**(1/3)
G=77000.0
L48=500.0
phi_limit48=15.0/300.0  # rad
J_needed48=T48*L48/(phi_limit48*G)
c_stiff48=(2*J_needed48/pi)**0.25
print("T48=",T48,"c_stress=",c_stress48,"d=",2*c_stress48)
print("J_needed48=",J_needed48,"c_stiff=",c_stiff48,"d=",2*c_stiff48)
print("governing d=",max(2*c_stress48,2*c_stiff48))

print("=== 3.50 ===")
T50=680000.0
tau_all=83.0
c_stress50=(2*T50/(pi*tau_all))**(1/3)
G=77000.0
L50=1200.0
phi_limit50=4*pi/180
J_needed50=T50*L50/(phi_limit50*G)
c_stiff50=(2*J_needed50/pi)**0.25
print("c_stress=",c_stress50,"d=",2*c_stress50)
print("c_stiff=",c_stiff50,"d=",2*c_stiff50)
print("governing d=",max(2*c_stress50,2*c_stiff50))

print("=== 3.52 (parallel composite, phi limited by stress) ===")
c_s,c_a=27.,36.
Gs,Ga=77000.,27000.
tau_s_all,tau_a_all=60.,45.
L=2500.0
phi_s_lim = tau_s_all*L/(Gs*c_s)
phi_a_lim = tau_a_all*L/(Ga*c_a)
print("phi_s_lim=",phi_s_lim,"deg=",math.degrees(phi_s_lim))
print("phi_a_lim=",phi_a_lim,"deg=",math.degrees(phi_a_lim))
print("phi_max=",min(phi_s_lim,phi_a_lim),"deg=",math.degrees(min(phi_s_lim,phi_a_lim)))

print("=== 3.54 ===")
c_s,c_a=15.,20.
Gs,Gbr=77000.,39000.
tau_s_all,tau_br_all=100.,55.
L=1800.0
phi_s_lim=tau_s_all*L/(Gs*c_s)
phi_br_lim=tau_br_all*L/(Gbr*c_a)
print("phi_s_lim deg=",math.degrees(phi_s_lim))
print("phi_br_lim deg=",math.degrees(phi_br_lim))
print("phi_max deg=",math.degrees(min(phi_s_lim,phi_br_lim)))

print("=== 3.56 (flange backlash, T at C) ===")
c_AB,c_CD=15.,18.
LAB,LCD=600.,900.
G=77000.0
JAB=Js(c_AB); JCD=Js(c_CD)
phi_CD_alone = 570000.0*LCD/(JCD*G)
print("phi_CD_alone deg=",math.degrees(phi_CD_alone))
backlash=1.5*pi/180
if math.degrees(phi_CD_alone) > 1.5:
    T1 = backlash*JCD*G/LCD
    dT = 570000.0-T1
    kAB=JAB*G/LAB
    kCD=JCD*G/LCD
    dT_AB=dT*kAB/(kAB+kCD)
    dT_CD=dT-dT_AB
    T_AB_final=dT_AB
    T_CD_final=T1+dT_CD
else:
    T_AB_final=0
    T_CD_final=570000.0
print("T1=",T1,"T_AB_final=",T_AB_final,"T_CD_final=",T_CD_final,"sum=",T_AB_final+T_CD_final)
tau_AB56=tau_s(T_AB_final,c_AB)
tau_CD56=tau_s(T_CD_final,c_CD)
print("tau_AB=",tau_AB56,"tau_CD=",tau_CD56)

print("=== 3.58 (gear, both ends fixed) ===")
c_AB,c_CD=30.,22.5
LAB,LCD=300.,200.
R_B,R_C=100.,40.
JAB=Js(c_AB); JCD=Js(c_CD)
G=77000.0
k = (LAB/LCD)*(JCD/JAB)*(R_B/R_C)   # T_CD = k*T_AB
print("k(T_CD/T_AB)=",k)
tau_all=50.0
TAB_from_AB = T_s_allow(tau_all,c_AB)
TAB_from_CD = T_s_allow(tau_all,c_CD)/k
TAB_gov = min(TAB_from_AB,TAB_from_CD)
print("TAB_from_AB=",TAB_from_AB,"TAB_from_CD=",TAB_from_CD,"TAB_gov=",TAB_gov)
TCD_gov = k*TAB_gov
Tapplied = TAB_gov + TCD_gov*(R_B/R_C)
print("TCD_gov=",TCD_gov,"Tapplied=",Tapplied, Tapplied/1000)
print("check tau_AB=",tau_s(TAB_gov,c_AB),"tau_CD=",tau_s(TCD_gov,c_CD))

print("=== 3.59 ===")
c_shaft=20.0
J_shaft=Js(c_shaft)
c2_j,c1_j=40.,36.
J_j=Jh(c2_j,c1_j)
T_total=500000.0
T_jacket=T_total*J_j/(J_j+J_shaft)
tau_jacket=T_jacket*c2_j/J_j
print("J_shaft=",J_shaft,"J_jacket=",J_j,"T_jacket=",T_jacket,"tau_jacket=",tau_jacket)
