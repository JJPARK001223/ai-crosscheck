# Codex independent node/edge inventory

Read-only audit script at J:/Desktop/abaquse/2026_11_13/audit_tip_nodes.py, resulttip_node_audit.json. Source and target both collapsed C3D20R, distinct coincident IDs, projected midside approximately.5 rather than.25. Topology and collapsed-edge patterns preserved; maxfractionchange8.79547e-5, targetrange.499869882.. .500131292.

Official Abaqus AnalysisGuide 2025 https://docs.software.vt.edu/abaqusv2025/English/SIMACAEANLRefMap/simaanl-c-contintegral.htm 3D singularity section distinguishes midpoint/independent-node1/r and quarterpoint/independent-nodecombinedsingularity. It permits midpoint-based1/r construction as practical alternative. Thus absenceof.25 is not itself an input defect requiring immediate mesh modification for this power-law hardening J assessment.

Do not claim exact HRR singularity or confirmed independent DOF freedom solely from distinctIDs. NoEquation/MPC/Tie/Coupling/Transform keywords, remoteRigidBodyonly; ordinary BCmembership still tocheck. Preserve mesh pendingAbaqusdatacheck and laterContour/localmeshconvergence. Originalpureelasticmaterialmodelvalidity remainsseparate: thisedgeaudit doesnotvalidate originalFE or targetgraphshape/provenance.
