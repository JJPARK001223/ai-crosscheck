const T=[[24720,162.2,166.8],[26400,161.8,166.4],[24720,161.5,166.0],[50420,160.7,165.2],[4,127.7,164.0],[6,127.7,163.6],[5,136.4,163.6],[5,155.6,163.6],[26400,158.9,163.4],[5,162.0,162.5],[1,136.4,162.0],[25700,157.5,162.0],[26400,155.9,160.4],[25700,154.2,158.7]];
// R=0.1 equivalent: sa=0.45se, sm=0.55se. Goodman with sfat=0.5su: sa/(0.5su)+sm/su = 0.45se/(0.5su)+0.55se/su = 1.45*se/su... solve se
const se=(mx,mn,su)=>{const sa=(mx-mn)/2,sm=(mx+mn)/2;return (sa/(0.5*su)+sm/su)/(0.45/(0.5*su)+0.55/su)};
for(const [n,su,A] of [["SM490YA",546.2,2691],["SM570TMC",610.2,3311]]){
 let D=0;const rows=[];
 for(const [N,mn,mx] of T){const e=se(mx,mn,su);const Nf=Math.pow(e/A,-1/0.149);D+=N/Nf;rows.push(e.toFixed(1))}
 console.log(n,"se:",rows.join(","),"D=",D.toExponential(3),"life=",(1/D).toFixed(0));
}
console.log("same-stress life ratio 570/490:",Math.pow(3311/2691,1/0.149).toFixed(2));
const s=a=>a.reduce((x,y)=>x+y,0);
const t3=[1.76e-5,1.85e-5,1.70e-5,3.36e-5,4.69e-9,6.88e-9,4.86e-9,3.35e-9,1.63e-5,2.75e-9,8.87e-10,1.50e-5,1.44e-5,1.31e-5];
const t4=[4.37e-6,4.59e-6,4.23e-6,8.36e-6,1.17e-9,1.71e-9,1.21e-9,8.32e-10,4.05e-6,6.85e-10,2.21e-10,3.74e-6,3.58e-6,3.27e-6];
const t6=[2.56e-8,9.13e-9,1.34e-8,1.08e-8,5.44e-9,1.67e-8,2.27e-8,2.72e-8,6.14e-9];
const t7=[6.36e-9,2.27e-9,3.32e-9,2.69e-9,1.35e-9,4.16e-9,5.65e-9,6.78e-9,1.53e-9];
console.log("T3",s(t3),1/s(t3),"T4",s(t4),1/s(t4),"T6",s(t6),"T7",s(t7));
console.log("ship ratio",27630/6872);
