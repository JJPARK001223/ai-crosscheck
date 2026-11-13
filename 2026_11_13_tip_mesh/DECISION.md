**최종 결정 (DECISION)**

**결론: 기존 midpoint collapsed mesh를 유지한다. quarter-point 자동 이동은 하지 않는다.**

**근거(INPUT 수준)**
- 2360개 collapsed edge는 모두 동일 xyz에 서로 다른 3개 ID를 가지며, 투영 분율은 약 .5(.25 아님)이다.
- Abaqus 3D 공식 문서는 midpoint/independent-node 1/r 구성을 허용하므로, quarter-point 부재가 곧 결함은 아니다.
- 119개 coincident tip 그룹은 각각 ZSYMM에 정확히 1개 ID만 속한다.
- 41개 XSYMM tip ID는 모두 x=0 중심면에 있다.
- YFIX 및 rigid body에 속한 tip ID는 0개이다.
- Equation/MPC/Tie/Coupling/Transform은 없다.
- 따라서 입력 수준의 멤버십 차단 사유는 **종결**한다.
- (0,0,-1)은 NORMAL 파라미터의 crack plane normal이며 q 벡터가 아니므로 변경하지 않는다.

**유보 사항**
- Abaqus 인식 여부 및 datacheck
- J-contour 및 mesh convergence
- 정확한 HRR 장(field)은 주장하지 않는다.

**다음 단계:** 새 Job을 만들어 WRITE INPUT으로 최종 export 감사를 수행한다. solver 자동 승인과 target graph 검증은 하지 않는다. 이 결과는 후보 geometry 점검일 뿐 solver 결과가 아니다.
