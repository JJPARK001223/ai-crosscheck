<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>처음 만나는 LEFM | 균열 끝에서 파손까지</title>
  <style>
    :root {
      --ink:#17243a; --muted:#5d6878; --paper:#f7f4ee; --card:#fff;
      --blue:#2166d1; --cyan:#31b7c9; --red:#df4a45; --amber:#e8a82e;
      --green:#16856a; --line:#dbe1e8; --shadow:0 16px 45px #24334b18;
    }
    *{box-sizing:border-box} html{scroll-behavior:smooth}
    body{margin:0;color:var(--ink);background:var(--paper);font-family:system-ui,-apple-system,"Segoe UI","Noto Sans KR",sans-serif;line-height:1.72}
    .wrap{width:min(1120px,calc(100% - 32px));margin:auto}
    header{position:relative;overflow:hidden;padding:76px 0 64px;background:linear-gradient(135deg,#10213c,#173d6d 64%,#12697a);color:white}
    header:after{content:"";position:absolute;width:420px;height:420px;border:80px solid #ffffff12;border-radius:50%;right:-120px;top:-200px}
    .eyebrow{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:#8ee6ee;font-weight:800}
    h1{max-width:800px;margin:.45rem 0 1rem;font-size:clamp(2.25rem,6vw,4.8rem);line-height:1.08;letter-spacing:-.045em}
    header p{max-width:680px;margin:0;font-size:1.08rem;color:#dbe9f4}
    nav{position:sticky;top:0;z-index:10;background:#ffffffed;backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
    nav .wrap{display:flex;gap:24px;overflow:auto;padding:12px 0} nav a{white-space:nowrap;color:var(--muted);text-decoration:none;font-size:.9rem;font-weight:700} nav a:hover{color:var(--blue)}
    main{padding:54px 0 80px} section{scroll-margin-top:76px;margin-bottom:70px}
    .kicker{color:var(--blue);font-size:.78rem;font-weight:900;letter-spacing:.12em;text-transform:uppercase}
    h2{margin:.25rem 0 1rem;font-size:clamp(1.65rem,3.5vw,2.45rem);line-height:1.22;letter-spacing:-.025em}
    h3{margin:.2rem 0 .45rem;font-size:1.1rem}.lead{max-width:800px;font-size:1.08rem;color:#3f4d61}
    .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.two{grid-template-columns:1fr 1fr}
    .card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow)}
    .num{display:grid;place-items:center;width:34px;height:34px;border-radius:10px;background:#eaf1ff;color:var(--blue);font-weight:900;margin-bottom:15px}
    .formula{margin:22px 0;padding:21px;border-radius:15px;background:#10213c;color:white;text-align:center;font-family:Cambria,"Times New Roman",serif;font-size:clamp(1.3rem,3vw,2rem);overflow:auto}
    .formula small{display:block;margin-top:7px;color:#bed1e7;font-family:system-ui,sans-serif;font-size:.75rem}
    .viz{background:#fff;border:1px solid var(--line);border-radius:20px;padding:clamp(16px,3vw,28px);box-shadow:var(--shadow)}
    svg{display:block;width:100%;height:auto}.caption{margin:.8rem 0 0;color:var(--muted);font-size:.86rem}
    .legend{display:flex;flex-wrap:wrap;gap:16px;margin:12px 0 0;font-size:.84rem;color:var(--muted)}.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px}
    .decision{display:grid;grid-template-columns:1fr auto 1fr;gap:18px;align-items:stretch}.state{padding:25px;border-radius:18px;border:2px solid}.safe{background:#effaf6;border-color:#85cbb8}.fail{background:#fff1ef;border-color:#e99a95}.arrow{align-self:center;font-size:1.5rem;color:#7a8798}
    .pill{display:inline-block;padding:4px 10px;border-radius:999px;font-size:.74rem;font-weight:900}.safe .pill{background:#cceee3;color:#0e684f}.fail .pill{background:#ffd7d3;color:#a82d28}
    .note{border-left:5px solid var(--amber);background:#fff9e9;padding:18px 20px;border-radius:4px 14px 14px 4px}.note strong{color:#8a5a00}
    dl{display:grid;grid-template-columns:max-content 1fr;gap:8px 18px;margin:0}dt{font-weight:900;color:var(--blue)}dd{margin:0;color:#46546a}
    .sources{font-size:.9rem}.sources li+li{margin-top:12px}.tag{font-size:.72rem;color:#fff;background:#68778c;padding:3px 8px;border-radius:6px}
    footer{border-top:1px solid var(--line);padding:24px 0 40px;color:var(--muted);font-size:.82rem}
    @media(max-width:760px){.grid,.two,.decision{grid-template-columns:1fr}.arrow{transform:rotate(90deg);justify-self:center}header{padding:55px 0}dl{grid-template-columns:1fr;gap:2px}dd{margin-bottom:10px}}
    @media(prefers-reduced-motion:no-preference){.card,.viz{transition:transform .2s,box-shadow .2s}.card:hover,.viz:hover{transform:translateY(-3px);box-shadow:0 20px 50px #24334b24}}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <div class="eyebrow">Linear Elastic Fracture Mechanics</div>
      <h1>균열 끝의 응력을 읽으면, 파손의 시작이 보인다.</h1>
      <p>선형탄성파괴역학(LEFM)의 핵심인 균열선단 응력집중, 응력확대계수 K, 파괴인성 K<sub>Ic</sub>를 한 흐름으로 이해하는 입문 안내서.</p>
    </div>
  </header>

  <nav aria-label="문서 목차"><div class="wrap">
    <a href="#why">왜 필요한가</a><a href="#tip">균열선단</a><a href="#k">K의 뜻</a><a href="#judge">파손판정</a><a href="#limits">해석 주의점</a><a href="#sources">출처</a>
  </div></nav>

  <main class="wrap">
    <section id="why">
      <div class="kicker">01 · 출발점</div><h2>평균응력만으로는 균열을 설명할 수 없다</h2>
      <p class="lead">매끈한 인장시험편의 중앙부는 응력이 거의 균일해 재료의 파손강도와 비교할 수 있다. 하지만 균열이 있으면 선단 부근의 응력이 위치에 따라 급격히 달라진다. 따라서 “가한 힘이 얼마인가?”보다 “그 힘이 균열 끝에서 얼마나 증폭되는가?”가 중요해진다.</p>
      <div class="grid">
        <article class="card"><div class="num">1</div><h3>선형탄성</h3><p>파손 직전까지 재료 거동을 선형탄성으로 근사한다. 취성재료는 이 가정에 특히 잘 맞는 경우가 많다.</p></article>
        <article class="card"><div class="num">2</div><h3>균열선단 특이성</h3><p>이상적인 선형탄성 해에서는 균열 끝으로 갈수록 응력이 무한대로 발산한다. 한 점의 최대응력만 비교할 수 없는 이유다.</p></article>
        <article class="card"><div class="num">3</div><h3>세기를 K로 요약</h3><p>응력장의 공간적 모양은 같고 그 크기는 K가 정한다. K는 하중과 균열·구조 형상의 효과를 함께 담는 지표다.</p></article>
      </div>
    </section>

    <section id="tip">
      <div class="kicker">02 · 시각화</div><h2>균열 끝에 가까울수록 응력은 급격히 커진다</h2>
      <div class="viz">
        <svg viewBox="0 0 960 430" role="img" aria-labelledby="tipTitle tipDesc">
          <title id="tipTitle">Mode I 균열선단의 응력집중</title><desc id="tipDesc">왼쪽 판의 중앙 균열 끝에 응력 띠가 밀집하고, 오른쪽 그래프에서 거리가 0에 가까울수록 응력이 1 제곱근 r에 비례해 증가한다.</desc>
          <defs><radialGradient id="heat"><stop offset="0" stop-color="#df4a45" stop-opacity=".9"/><stop offset=".35" stop-color="#e8a82e" stop-opacity=".6"/><stop offset="1" stop-color="#e8a82e" stop-opacity="0"/></radialGradient><marker id="arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8Z" fill="#2166d1"/></marker></defs>
          <rect x="28" y="55" width="400" height="300" rx="18" fill="#edf3f8" stroke="#9dafc3"/>
          <g stroke="#2166d1" stroke-width="4" marker-end="url(#arr)"><path d="M100 92V42"/><path d="M228 92V42"/><path d="M356 92V42"/><path d="M100 318v50"/><path d="M228 318v50"/><path d="M356 318v50"/></g>
          <ellipse cx="332" cy="205" rx="92" ry="120" fill="url(#heat)"/>
          <path d="M72 205H331" stroke="#17243a" stroke-width="8" stroke-linecap="round"/><circle cx="332" cy="205" r="7" fill="#df4a45"/>
          <text x="80" y="192" fill="#17243a" font-size="18">균열</text><text x="342" y="194" fill="#b22d29" font-size="18" font-weight="700">선단</text><text x="40" y="28" fill="#2166d1" font-size="17" font-weight="700">Mode I: 위아래로 벌어지는 하중</text>
          <g transform="translate(510,35)"><path d="M35 330H410M35 330V25" stroke="#8291a5" stroke-width="2"/><path d="M48 44C73 72 102 112 141 163S240 263 392 304" fill="none" stroke="#df4a45" stroke-width="6"/><path d="M48 45V330" stroke="#df4a45" stroke-dasharray="6 7" opacity=".5"/><text x="135" y="65" fill="#b22d29" font-size="21" font-weight="700">σ ∝ 1/√r</text><text x="380" y="357" fill="#5d6878" font-size="17">거리 r</text><text x="2" y="20" fill="#5d6878" font-size="17">응력 σ</text><text x="40" y="355" fill="#5d6878" font-size="15">균열선단</text></g>
        </svg>
        <div class="formula">σ<sub>x</sub> = K / √(2πr)<small>균열선단 전방의 대표적인 Mode I 근접장 표현 · r은 선단으로부터의 거리</small></div>
        <p class="caption">K가 같다면 r이 작아질수록 응력은 1/√r 꼴로 상승한다. 실제 재료에서는 선단의 미세 소성·손상 때문에 무한응력이 그대로 나타나는 것은 아니며, 위 식은 선형탄성 이상화의 근접장이다. [1, 식 (4)]</p>
      </div>
    </section>

    <section id="k">
      <div class="kicker">03 · 핵심 물리량</div><h2>K는 “균열선단 응력장의 볼륨 노브”다</h2>
      <div class="grid two">
        <article class="card"><h3>K — 현재의 균열 구동 수준</h3><p>같은 거리 r에서 K가 클수록 응력이 비례해 커진다. 즉 K는 균열선단 응력장의 진폭을 나타내는 응력확대계수다. 아래첨자 I는 균열면을 벌리는 Mode I을 뜻한다.</p></article>
        <article class="card"><h3>K<sub>Ic</sub> — 재료의 임계 저항</h3><p>Mode I에서 파괴가 시작되는 임계 응력확대계수다. 원문은 이를 파괴인성(fracture toughness)이라 부르고, 응력구배 기반 임계값과 연결한다.</p></article>
      </div>
      <div class="formula">K<sub>Ic</sub> = √(2πEw<sub>f</sub>)<small>E: 탄성계수 · w<sub>f</sub>: 응력구배 기반 재료 임계값(단위 J/m²) · [1, 식 (7)]</small></div>
      <p class="note"><strong>단위 확인:</strong> K와 K<sub>Ic</sub>는 같은 종류의 물리량이므로 직접 비교할 수 있다. 다만 이 문서의 두 원문은 K의 근접장 정의에서 상수 표기가 서로 다르다. 위 시각화와 식은 [1]의 <span lang="en">K/√(2πr)</span> 표기를 일관되게 사용했다.</p>
    </section>

    <section id="judge">
      <div class="kicker">04 · 시각화</div><h2>판정은 단순하다: K를 K<sub>Ic</sub>와 비교한다</h2>
      <div class="viz">
        <svg viewBox="0 0 960 280" role="img" aria-labelledby="judgeTitle judgeDesc">
          <title id="judgeTitle">K와 K Ic의 파손 판정 게이지</title><desc id="judgeDesc">게이지의 녹색 영역은 K가 K Ic보다 작은 안정 영역이고, 붉은 영역은 K가 K Ic 이상인 파괴 개시 영역이다.</desc>
          <defs><linearGradient id="bar"><stop offset="0" stop-color="#16856a"/><stop offset=".68" stop-color="#57b99f"/><stop offset=".7" stop-color="#df4a45"/><stop offset="1" stop-color="#aa2828"/></linearGradient></defs>
          <rect x="75" y="100" width="810" height="48" rx="24" fill="url(#bar)"/><line x1="642" y1="65" x2="642" y2="190" stroke="#17243a" stroke-width="4"/><path d="M630 66l12-18 12 18z" fill="#17243a"/>
          <text x="642" y="32" text-anchor="middle" fill="#17243a" font-size="22" font-weight="800">K = K<tspan baseline-shift="sub" font-size="15">Ic</tspan></text><text x="220" y="188" text-anchor="middle" fill="#0f6d56" font-size="22" font-weight="800">K &lt; K<tspan baseline-shift="sub" font-size="15">Ic</tspan></text><text x="220" y="220" text-anchor="middle" fill="#5d6878" font-size="17">임계값 미도달</text><text x="770" y="188" text-anchor="middle" fill="#b22d29" font-size="22" font-weight="800">K ≥ K<tspan baseline-shift="sub" font-size="15">Ic</tspan></text><text x="770" y="220" text-anchor="middle" fill="#5d6878" font-size="17">Mode I 파괴 개시</text>
        </svg>
        <div class="decision">
          <div class="state safe"><span class="pill">임계 미도달</span><h3>K &lt; K<sub>Ic</sub></h3><p>주어진 LEFM 판정에서 균열 구동력이 재료의 임계 저항보다 작다. 즉시 파괴 개시로 판정하지 않는다.</p></div>
          <div class="arrow" aria-hidden="true">→</div>
          <div class="state fail"><span class="pill">임계 도달</span><h3>K ≥ K<sub>Ic</sub></h3><p>임계점에서 Mode I 균열 진전이 시작되는 조건에 도달한다. 설계에서는 이 상태를 허용하지 않도록 여유를 둔다.</p></div>
        </div>
        <p class="caption">원문 [1]은 균열선단에서 국부응력 조건은 특이성 때문에 이미 만족되며 응력구배 조건이 파손을 지배한다고 설명하고, 그 임계값을 K<sub>Ic</sub>와 연결한다. [2]도 균열 시편의 파손하중 예측에 K와 임계 에너지 방출률에 대응하는 재료값을 사용한다.</p>
      </div>
    </section>

    <section id="limits">
      <div class="kicker">05 · 해석할 때</div><h2>이 비교가 의미 있으려면 전제를 확인해야 한다</h2>
      <div class="grid">
        <article class="card"><div class="num">A</div><h3>선형탄성 근사</h3><p>균열선단의 큰 비선형 영역이 구조 거동을 지배한다면 단순 LEFM 근접장만으로 충분하지 않다. 여기서는 원문이 다룬 선형탄성·취성 균열 문제의 범위로 한정한다.</p></article>
        <article class="card"><div class="num">B</div><h3>Mode와 임계값 일치</h3><p>K<sub>Ic</sub>는 Mode I 임계값이다. 현재 문제의 K 역시 같은 Mode I 정의와 조건에서 평가해야 의미 있는 비교가 된다.</p></article>
        <article class="card"><div class="num">C</div><h3>FEA 선단값 주의</h3><p>일반 유한요소해석은 균열선단 바로 근처 응력을 정확히 주기 어렵다. [2]는 선단에서 떨어진 응력 분포를 근접장 식에 곡선맞춤하여 K를 구했다.</p></article>
      </div>
      <p class="note" style="margin-top:18px"><strong>혼동하지 말 것:</strong> 구멍처럼 응력이 유한한 노치에서는 “K 대 K<sub>Ic</sub>” 균열 판정을 그대로 쓰지 않는다. 두 원문은 이런 경우 국부응력과 응력구배 조건을 함께 확인하는 통합 기준을 제안한다.</p>
    </section>

    <section id="sources" class="sources">
      <div class="kicker">근거 문헌</div><h2>이 문서에 사용한 출처</h2>
      <ol>
        <li><strong>Kwon, Y. W.</strong>, “Revisiting Failure of Brittle Materials,” <em>Journal of Pressure Vessel Technology</em>, Vol. 143, 064503, 2021. DOI: 10.1115/1.4050989. <span class="tag">특히 pp. 1–3, 식 (1)–(7)</span></li>
        <li><strong>Kwon, Y. W.; Markoff, E. K.; DeFisher, S.</strong>, “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” <em>Materials</em>, Vol. 17, 569, 2024. DOI: 10.3390/ma17030569. <span class="tag">특히 pp. 1–2, 6–8, 식 (1)–(4), Figs. 8–11</span></li>
      </ol>
      <p>설명과 시각화는 위 두 논문의 내용만을 바탕으로 재구성했다. 그림은 원문 이미지를 복제하지 않고 개념 전달을 위해 새로 그렸다.</p>
    </section>
  </main>

  <footer><div class="wrap">LEFM 입문용 단일 문서 · 균열선단 근접장과 Mode I 파괴 개시 판정에 초점을 둠</div></footer>
</body>
</html>
