# Codex independent proposal

Source radius r=270..330, half circumference phi=atan2(x,y)=0..pi. The crack arc occupies phi=0..pi/2 at r300 and ends in radial front at phi=pi/2. Preserve t60 and a30 using r'=r+300. Preserve both x=0 symmetry boundaries, theta=.3pi and injectivity with:

- phi<=pi/2: phi'=.6phi.
- Else q=(phi-pi/2)/(pi/2), phi'=.3pi+(pi/2)(.6q+1.6q^3-.8q^4).
- Uncracked angular derivative .6+4.8q^2-3.2q^3=.6..2.2, positive. C2 continuity at crack endpoint, phi'(pi)=pi.
- x'=r'sin(phi'), y'=r'cos(phi'), z'=z.

This is an engineered mesh morph, not a source-paper method, and is not a fit to PNG. Source tiny negative x on symmetry planes (rounding about 1e-4mm) snaps to x'=0, subject to duplicate count and set-plane checks. Assembly-only reference nodes remain unchanged. YFIX set is part node54 at negative-y outer symmetry boundary, mapped from (0,-330,1500) to (0,-630,1500), retaining global U2 constraint.

Keep topology, all sets and all non-part-node input lines identical. Current cload is intentionally unchanged and MUST be adjusted/validated before solve. Length1500 retained only in draft; L/Rm changes5->2.5 and boundary effect requires assessment. Target PNG uniform-depth shape not proven; candidate is conditional, not a confirmed reproduction.

Offline checks: all part nodes finite; exact target ratios from radii and crack tip coordinates; 119 preserved front stations; duplicates unchanged; symmetry sets retain planes; C3D20R shape-function identities tested using natural cube. Evaluate original and candidate Jacobians at all 27 three-point Gauss grid points plus 8 actual reduced-integration points. Nonpositive sampled Jacobians prevent candidate publication. This cannot prove Jacobian positivity everywhere, full mesh quality, mesh convergence or physical validity. Abaqus checks required later.

Implementation: J:/Desktop/abaquse/2026_11_13/transform_geometry.py, numpy from Python314. No solver invocation.
