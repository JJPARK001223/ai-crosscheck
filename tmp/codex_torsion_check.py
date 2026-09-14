import math
import json
from pathlib import Path
import hashlib

p = math.pi
def J(b, a=0): return p*(b**4-a**4)/2
def simpson(f, a, b, n=20000):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))
def ty(b, y, a=0): return y*J(b,a)/b
def tp(b, y, a=0): return 2*p*y*(b**3-a**3)/3
def tep(b,a,y,r): return 2*p*y*((r**4-a**4)/(4*r)+(b**3-r**3)/3)
def residual_solid(b,y,T):
    r=b*(4-3*T/ty(b,y))**(1/3)
    inner=y-T*r/J(b)
    outer=y-T*b/J(b)
    return dict(rho_mm=r,interface_MPa=inner,outer_MPa=outer,max_abs_MPa=max(abs(inner),abs(outer)))

out={}
out['3.2_corrected']={'T_Nm':ty(45,45,30)/1000,'solid_radius_mm':math.sqrt(45**2-30**2)}
out['3.12_corrected']={s:abs(T)*b/J(b,4) for s,T,b in [('AB',48000,7.5),('BC',-96000,9),('CD',-156000,10.5)]}
out['3.14_CD_corrected_MPa']=500000*23/J(23)
out['3.28_corrected']={s:{'T_Nm':T/1000,'d_mm':2*(2*T/(p*75))**(1/3)} for s,T in [('AB',120000),('CD',288000),('EF',720000)]}
out['3.32_corrected_T_Nm']=math.radians(4)*J(18,12)*27000/1250/1000
out['3.36_actual']={'phi_CB_deg':math.degrees(400000*800/(27000*J(15))), 'phi_DB_deg':math.degrees(400000*800/(27000*J(15))-500000*1000/(27000*J(18)))}
L=[600,800,1000,500]; js=[J(15),J(15),J(18),J(18)]
ta=-sum(c*l/j for c,l,j in zip([0,400000,1300000,1800000],L,js))/sum(l/j for l,j in zip(L,js))
out['3.36_script_hypothetical_fixed']={'TA_Nmm':ta,'compatibility_rad':sum(t*l/j/27000 for t,l,j in zip([ta,ta+400000,ta+1300000,ta+1800000],L,js))}
out['3.38_corrected_phi_deg']=math.degrees(800000*400/(J(18)*27000)+2400000*375/(J(30)*39000)+2400000*250/(J(30,20)*39000))
out['3.44_corrected_phi_deg']=math.degrees(600*60/(J(1)*77000)*(1+1/4+1/16))
out['3.52_scan25m_phi_deg']=math.degrees(60*25000/(77000*27))

k1=77000*J(15)/600; k2=77000*J(18)/900
delta=math.radians(1.5); T=570000
theta_C=(T+k1*delta)/(k1+k2)
theta_B=theta_C-delta
t1=k1*theta_B; t2=k2*theta_C
out['3.56']={'TAB_Nm':t1/1000,'TCD_Nm':t2/1000,'theta_B_deg':math.degrees(theta_B),'theta_C_deg':math.degrees(theta_C),'equilibrium_Nmm':t1+t2-T,'compatibility_rad':theta_C-theta_B-delta,'tau_AB_MPa':t1*15/J(15),'tau_CD_MPa':t2*18/J(18)}
assert abs(t1+t2-T)<1e-8 and abs(theta_C-theta_B-delta)<1e-12

for length in [200,500]:
    k=300/length*J(22.5)/J(30)*100/40
    tab=min(ty(30,50),ty(22.5,50)/k); tcd=k*tab
    compat=100*tab*300/(77000*J(30))-40*tcd*length/(77000*J(22.5))
    out[f'3.58_LCD_{length}']={'k':k,'TAB_Nm':tab/1000,'TCD_Nm':tcd/1000,'T_Nm':(tab+2.5*tcd)/1000,'tau_AB_MPa':tab*30/J(30),'tau_CD_MPa':tcd*22.5/J(22.5),'mesh_arc_residual_mm':compat}
    assert abs(compat)<1e-12

out['3.76_corrected']={s:{'T_Nm':7500/(2*p*30)*m,'d_mm':2*(2*7500/(2*p*30)*1000*m/(p*60))**(1/3)} for s,m in [('AB',1),('CD',2.5),('EF',6.25)]}

b,a,y,G,L=35,15,180,77200,900
for r in [b,25,a]:
    numeric=2*p*(simpson(lambda x:y*x**3/r,a,r)+simpson(lambda x:y*x*x,r,b))
    analytic=tep(b,a,y,r)
    out[f'3.106_rho_{r}']={'analytic_Nm':analytic/1000,'numeric_Nm':numeric/1000,'relative_error':abs(numeric-analytic)/analytic,'phi_deg':math.degrees(y*L/(G*r))}
    assert math.isclose(numeric,analytic,rel_tol=1e-11)
assert math.isclose(tep(b,a,y,b),ty(b,y,a),rel_tol=1e-12)
assert math.isclose(tep(b,a,y,a),tp(b,y,a),rel_tol=1e-12)

T=8475000; y=154
out['3.114_diameter30_hypothesis']={'TY_Nm':ty(15,y)/1000,'TP_Nm':tp(15,y)/1000,'T_over_TP':T/tp(15,y)}
out['3.114_radius30_actual']={'TY_Nm':ty(30,y)/1000,'TP_Nm':tp(30,y)/1000,'T_over_TP':T/tp(30,y),**residual_solid(30,y,T)}

b,y,G,L=16,145,77200,600
r=y*L/(G*math.radians(6)); T=tep(b,0,y,r)
out['3.116_radius16_actual']={'phiY_deg':math.degrees(y*L/(G*b)),'T_Nm':T/1000,'permanent_phi_deg':6-math.degrees(T*L/(G*J(b))),**residual_solid(b,y,T)}

b,a,y=30,12.5,145
T=tp(b,y,a)
res=lambda r:y-T*r/J(b,a)
res_T=2*p*simpson(lambda r:res(r)*r*r,a,b)
out['3.118']={'Tp_Nm':T/1000,'inner_res_MPa':res(a),'outer_res_MPa':res(b),'residual_T_Nmm':res_T,'Tp_over_TY':T/ty(b,y,a)}
assert abs(res_T)<1e-7
assert max(abs(res(a)),abs(res(b)))<y

b=25; alpha=math.radians(5)/725
A=46666.666666666664; B=-6666666.666666667
out['3.112_parabolic_comparison_Nm']=2*p*(A*alpha*b**4/4+B*alpha**2*b**5/5)/1000

c1,c2,t,T=150,100,3,3e6
Am=p*(c1*c1-c2*c2); q=T/(2*Am)
To=q*2*p*c1*c1; Ti=-q*2*p*c2*c2
out['3.148_closed']={'Am_mm2':Am,'q_N_per_mm':q,'tau_MPa':q/t,'outer_T_Nm':To/1000,'inner_T_Nm':Ti/1000,'balance_Nmm':To+Ti-T}
out['3.148_wrong_open_comparison']={'Jopen_mm4':2*p*(c1+c2)*t**3/3,'tau_MPa':3*T/(2*p*(c1+c2)*t*t)}
assert abs(To+Ti-T)<1e-8

directory=Path('sessions/2026_09_14_beer_ch3_torsion/round1')
out['script_sha256']={f'b{i}':hashlib.sha256((directory/f'claude_calc_b{i}.py').read_bytes()).hexdigest() if (directory/f'claude_calc_b{i}.py').exists() else 'MISSING' for i in range(1,6)}
Path('tmp/codex_torsion_check.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
