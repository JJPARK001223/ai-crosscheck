// Independent calculations from the source diagrams. Units: N, mm, MPa.
// 4.100: conditional on W200x31.3 properties in Nucor Skyline (2026),
// Technical Product Manual, PDF p. 37. Source problem says W200x31.1.
const EAl = 70000;
const EBr = 105000;
const c = 16;
const IAl = 2 * (32 * 8 ** 3 / 12 + 32 * 8 * 12 ** 2);
const IBr = 2 * 8 * 32 ** 3 / 12;
const EI = EAl * IAl + EBr * IBr;
const kAl = 100 / (EAl * c);
const kBr = 160 / (EBr * c);
const k = Math.min(kAl, kBr);

function rectangularPlasticBending(b, h, elasticCoreThickness) {
  const yieldStress = 300;
  const a = elasticCoreThickness / 2;
  const I = b * h ** 3 / 12;
  return {
    b_mm: b, h_mm: h, I_mm4: I,
    firstYield_Nm: yieldStress * I / (h / 2) / 1000,
    elasticCore4mm_Nm: yieldStress * b * ((h / 2) ** 2 - a ** 2 / 3) / 1000,
  };
}

const P = 50000;
const A = 3970;
const I = 31.3e6;
const extremeDistance = 105;
const M = P * 80;
const sigmaAxial = -2 * P / A;
const sigmaBendingAtA = -M * extremeDistance / I;

console.log(JSON.stringify({
  problem4_34: {
    IAl_mm4: IAl, IBr_mm4: IBr, EI_Nmm2: EI,
    kAl_per_mm: kAl, kBr_per_mm: kBr,
    allowableMoment_Nm: EI * k / 1000,
    sigmaAlMax_MPa: EAl * k * c,
    sigmaBrMax_MPa: EBr * k * c,
    controllingMaterial: 'Aluminum',
    claudeMoment_Nm: 2269.5,
  },
  problem4_68_z_axis: rectangularPlasticBending(8, 12, 4),
  comparison_x_axis: rectangularPlasticBending(12, 8, 4),
  problem4_100_conditional_W200x31_3: {
    A_mm2: A, I_mm4: I, c_mm: extremeDistance,
    a_sigmaA_MPa: -3 * P / A,
    b_moment_Nmm: M,
    b_axial_MPa: sigmaAxial,
    b_bendingAtA_MPa: sigmaBendingAtA,
    b_sigmaA_MPa: sigmaAxial + sigmaBendingAtA,
    comparison_opposite_flange_MPa: sigmaAxial - sigmaBendingAtA,
    claude_a_MPa: -37.78,
    claude_b_MPa: -11.78,
  },
}, null, 2));
