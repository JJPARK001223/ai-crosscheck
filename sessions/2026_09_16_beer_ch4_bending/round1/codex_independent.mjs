// Independent calculation. Initial run was sealed before reading Claude answers.
// Post-comparison PDF reinspection: 4.162 M=68 Nm (not 65); textbook FS uses
// ultimate stress for 4.6/4.8; 4.114 clipped thickness is conditional, not verified.
// Units: N, mm, MPa unless a result key states otherwise. No dependencies.
import fs from 'node:fs';
import assert from 'node:assert/strict';
const results = {};
const out = (id, data) => { results[id] = data; };
function section(parts) { // [area, centroid coordinate, own centroidal I]
  const A=parts.reduce((s,p)=>s+p[0],0);
  const c=parts.reduce((s,p)=>s+p[0]*p[1],0)/A;
  const I=parts.reduce((s,p)=>s+p[2]+p[0]*(p[1]-c)**2,0);
  return {A,c,I};
}
const rect=(b,h,c)=>[b*h,c,b*h**3/12];
function integrate(f,a,b,n=100000) {
  let s=0; const dr=(b-a)/n;
  for(let i=0;i<n;i++) s+=f(a+(i+.5)*dr);
  return s*dr;
}
function curved(b,ri,ro,N,M) { // M positive = inner-fiber tension.
  const A=integrate(b,ri,ro), rc=integrate(r=>r*b(r),ri,ro)/A;
  const rn=A/integrate(r=>b(r)/r,ri,ro), e=rc-rn;
  const stress=r=>N/A+M/(A*e)*(rn/r-1);
  const Ncheck=integrate(r=>stress(r)*b(r),ri,ro);
  const Mcheck=integrate(r=>-stress(r)*(r-rc)*b(r),ri,ro);
  assert.ok(Math.abs(Ncheck-N)<1e-5*Math.max(1,Math.abs(N)));
  assert.ok(Math.abs(Mcheck-M)<1e-6*Math.max(1,Math.abs(M)));
  return {A,rc,rn,e,inner:stress(ri),outer:stress(ro),N,M,Ncheck,Mcheck};
}
function rcBeam(b,d,As,n,M,fcAllow,fsAllow) {
  const x=(-n*As+Math.sqrt((n*As)**2+2*b*n*As*d))/b;
  const I=b*x**3/3+n*As*(d-x)**2;
  const mc=fcAllow*I/x, ms=fsAllow*I/(n*(d-x));
  return {b,d,As,n,x,I,fc:M*x/I,fs:n*M*(d-x)/I,
    Mc_kNm:mc/1e6,Ms_kNm:ms/1e6,Mallow_kNm:Math.min(mc,ms)/1e6};
}
// Fixed-seed Fisher-Yates sample, pool excludes reported low-confidence problems.
const pool=[2,4,10,12,22,24,26,28,32,34,36,38,40,44,54,56,58,60,68,70,72,74,76,78,80,92,94,98,100,102,106,108,110,118,120,122,126,156,158,160,162,166,170,176,178,184];
let seed=20260916; const rand=()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)/4294967296);
const shuffled=[...pool]; for(let i=shuffled.length-1;i>0;i--) {const j=Math.floor(rand()*(i+1));[shuffled[i],shuffled[j]]=[shuffled[j],shuffled[i]];}
out('sample',{seed:20260916,pool,selected:shuffled.slice(0,15).sort((a,b)=>a-b)});
// Priority 4.6, 4.8, 4.16, 4.18, 4.20.
{ const I=2*16*200**3/12+228*10**3/12;out('4.6',{I,allow:400/2.5,M_kNm:(400/2.5)*I/100/1e6,yieldBasedAlternative_kNm:(250/2.5)*I/100/1e6}); }
{ const A=2470,Iweak=1.61e6,b=103,I=2*(Iweak+A*(b/2)**2);out('4.8',{A,Iweak,b,I,allow:400/3,M_kNm:400/3*I/b/1e6,yieldBasedAlternative_kNm:260/3*I/b/1e6}); }
{ const s=section([rect(20,25,12.5),rect(40,15,32.5)]);out('4.16',{...s,top:40-s.c,bottom:s.c,Mt_Nm:24*s.I/(40-s.c)/1000,Mc_Nm:30*s.I/s.c/1000,Mallow_Nm:Math.min(24*s.I/(40-s.c),30*s.I/s.c)/1000}); }
{ const s=section([rect(112,12,6),rect(36,38,31)]);out('4.18',{...s,ctop:50-s.c,cbottom:s.c,topCompression_Nm:Math.min(110*s.I/(50-s.c),80*s.I/s.c)/1000,topTension_Nm:Math.min(80*s.I/(50-s.c),110*s.I/s.c)/1000}); }
{ const b=y=>40+40*y/54,A=integrate(b,0,54),c=integrate(y=>y*b(y),0,54)/A,I=integrate(y=>(y-c)**2*b(y),0,54);out('4.20',{A,c,I,top:54-c,tensionBound_kNm:120*I/(54-c)/1e6,compressionAtTensionBound:120*c/(54-c),note:'Compression allowable is cropped off in source. Bound only.'}); }
// Rotated cap channel: wood top touches underside of horizontal channel web.
{ const Ew=12000,Es=200000,Aw=150*250,As=2170,tw=5.59,xbar=14.5,bf=57.4,ytop=250+tw,ys=ytop-xbar;
  const s=section([[Aw,125,150*250**3/12],[As*Es/Ew,ys,.545e6*Es/Ew]]);
  const EI=Ew*s.I, k=50e6/EI;
  out('4.42',{Aw,As,tw,xbar,bf,ys,ytop,NA_fromBottom:s.c,IwoodEquivalent:s.I,EI,
    woodMax:k*Ew*Math.max(s.c,250-s.c),steelMax:k*Es*Math.max(Math.abs(ytop-s.c),Math.abs(ytop-bf-s.c))});
  out('4.46',{rho_literal_50Nm_m:EI/50000/1000,rho_if50kNm_m:EI/50e6/1000});
}
{const r=rcBeam(350,480,4*Math.PI*25**2/4,8,175e6,0,0);delete r.Mc_kNm;delete r.Ms_kNm;delete r.Mallow_kNm;out('4.48',r);}
out('4.50',rcBeam(1000,100,1000/225*Math.PI*16**2/4,10,0,9,120));
out('4.52',rcBeam(1000,100,1000/140*Math.PI*16**2/4,10,0,9,140));
out('4.62',{D:108,t:18,M:450000,cases:[9,18].map(r=>({r,d:108-2*r,D_over_d:108/(108-2*r),r_over_d:r/(108-2*r),nominal:6*450000/(18*(108-2*r)**2)})),note:'sigma_max=K*nominal; K chart unavailable'});
out('4.64',{D:80,d:40,t:8,M:250000,D_over_d:2,r_over_d:[.1,.2],nominal:6*250000/(8*40**2),note:'sigma_max=K*nominal; K chart unavailable'});
// Straight-member eccentric loads; local stress concentration is not included.
{const A=240*90,I=90*240**3/12;out('4.104',{A,I,a_A:-180000/A,a_B:-180000/A,b_A:-120000/A-60000*150*120/I,b_B:-120000/A+60000*150*120/I});}
{const D=18,d=14,A=Math.PI*(D*D-d*d)/4,I=Math.PI*(D**4-d**4)/64;out('4.112',{D,d,A,I,h:3*I/(A*(D/2))});}
{const s=section([rect(20,60,30),rect(60,20,70)]),e=40+s.c;
 const P=150/(1/s.A+e*s.c/s.I);out('4.114_conditional_t20',{...s,e,P_kN:P/1000,NA_fromLeft:s.c+s.I/(s.A*e),rightStress:P/s.A-P*e*(80-s.c)/s.I,note:'Left stem thickness first digit is clipped. This is a conditional t=20 calculation.'});}
{const s=section([rect(150,25,187.5),rect(25,150,100),rect(100,25,12.5)]),e=s.c-100;
 out('4.116',{A_original:3*25*150,P_original_kN:3*25*150*100/1000,...s,e,P_modified_kN:100/(1/s.A+e*s.c/s.I)/1000});}
// Curved priority sections. 4.180 triangular-section reading remains conditional.
{const b=r=>r<90?20:60;const A=2200,rc=(1000*65+1200*100)/A;
 // Integrate piecewise to avoid a discontinuity at r=90.
 const rn=A/(20*Math.log(90/40)+60*Math.log(110/90)),e=rc-rn,N=-10000,M=-10000*(100+rc);
 const sig=r=>N/A+M/(A*e)*(rn/r-1);
 out('4.172',{A,rc,rn,e,N,M,sigmaA:sig(40),sigmaB:sig(110)});}
{const b=r=>80*(190-r)/90,rc=130;out('4.180_conditional',curved(b,100,190,-10000,-10000*rc));}
// Fifteen sampled problems.
{const I=(80*120**3-40*80**3)/12;out('4.2',{I,A:-15e6*40/I,B:15e6*60/I});}
{const s=section([rect(50,10,5),rect(20,50,35)]);out('4.10',{...s,sigmaT:1.5e6*s.c/s.I,sigmaC:-1.5e6*(60-s.c)/s.I});}
{const rho=1250/2-6/2,I=Math.PI*6**4/64;out('4.22',{rho,I,sigma:200000*3/rho,M_Nm:200000*I/rho/1000});}
out('4.24',{sigma_z:60000*10/(12*20**3/12),rho_z_m:200000*(12*20**3/12)/60000/1000,sigma_y:60000*6/(20*12**3/12),rho_y_m:200000*(20*12**3/12)/60000/1000});
{ // Numerical optimization, constrained b^2+d^2=1, independent of symbolic answer.
 let bestS=[0,0],bestI=[0,0]; for(let k=1;k<100000;k++){const t=k*Math.PI/2/100000,b=Math.cos(t),d=Math.sin(t),S=b*d*d/6,I=b*d**3/12;if(S>bestS[0])bestS=[S,d/b];if(I>bestI[0])bestI=[I,d/b];}
 out('4.28',{stressRatioExact:Math.sqrt(2),curvatureRatioExact:Math.sqrt(3),numericalS:bestS,numericalI:bestI});}
{const Ia=2*(32*8**3/12+32*8*12**2),Ib=2*8*32**3/12,Itr=Ia+1.5*Ib;
 out('4.34',{Ia,Ib,Itr,M_Nm:Math.min(100/16,160/(1.5*16))*Itr/1000});}
{const Iw=250*(3*50**3/12+2*50*56**2),Is=2*250*(6**3/12+6*28**2),n=200/14,Itr=Iw+n*Is;
 out('4.38',{Iw,Is,n,Itr,M_kNm:Math.min(14/81,150/(n*31))*Itr/1e6});}
{const b=200,d=450,n=8,fc=12.5,fs=140,x=d/(1+fs/(n*fc)),As=b*x*x/(2*n*(d-x));
 out('4.54',{x,As,M_kNm:.5*b*x*fc*(d-x/3)/1e6});}
{const b=3,c=5,sigmaMax=7,I=2*b*c**3/3;
 const checks=[.5,1,2,3,5].map(n=>{const M=2*integrate(y=>sigmaMax*(y/c)**(1/n)*y*b,0,c);const computed=(1+2*n)/(3*n)*M*c/I;assert.ok(Math.abs(computed-sigmaMax)<1e-6);return {n,M,recovered:computed};});
 out('4.98',{formula:'sigma_max=(1+2n)/(3n)*Mc/I, n>0',checks});}
{const A=12**2,I=12**4/12,e=24;out('4.106',{A,I,e,P_a_N:105/(1/A+e*6/I),P_b_N:105/(1/A+e*(6*Math.sqrt(2))/I)});}
{const s=section([rect(50,100,50),rect(150,50,125)]);out('4.118',{...s,ymin:s.c-s.I/(s.A*(150-s.c)),ymax:s.c+s.I/(s.A*s.c)});}
{const Iy=17,Iz=29,Iyz=5,Mz=43,D=Iy*Iz-Iyz**2,a=-Iy*Mz/D,b=Iyz*Mz/D;
 const momentY=a*Iyz+b*Iy,momentZ=-(a*Iz+b*Iyz);assert.ok(Math.abs(momentY)<1e-12&&Math.abs(momentZ-Mz)<1e-12);
 out('4.158',{formula:'sigma=-(Iy*y-Iyz*z)*Mz/(Iy*Iz-Iyz^2)',fixture:{Iy,Iz,Iyz,Mz,a,b,momentY,momentZ}});}
out('4.162',curved(()=>30,40,60,0,-68000));
{const ri=20,ro=35,a=7.5,rc=27.5,A=Math.PI*a*a,rn=(rc+Math.sqrt(rc*rc-a*a))/2,e=rc-rn,N=500,M=500*2*rc;
 const sig=r=>N/A+M/(A*e)*(rn/r-1);out('4.178',{A,rc,rn,e,N,M,sigmaA:sig(ri),sigmaB:sig(ro)});}
{const b=r=>35-(r-40)/6,rc=40+60*(35+2*25)/(3*(35+25));out('4.184',curved(b,40,100,15000,15000*rc));}
const dest=new URL('./codex_independent_results.json',import.meta.url);
fs.writeFileSync(dest,JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify(results,null,2));
