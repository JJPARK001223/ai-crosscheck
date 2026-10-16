import fitz, glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')
files = glob.glob(r"J:\Desktop\XLPR\xLPR참고문헌\*.pdf") + glob.glob(r"J:\Desktop\XLPR\(ML19337C165)*.pdf")
out = r"J:\Desktop\공학\ai-crosscheck\round43\txt"
for f in sorted(files):
    d = fitz.open(f)
    name = os.path.basename(f)[:-4]
    parts = [f"=====PAGE {i+1}=====\n" + p.get_text() for i, p in enumerate(d)]
    txt = "\n".join(parts)
    open(os.path.join(out, name + ".txt"), "w", encoding="utf-8").write(txt)
    print(name, len(d), "pages", len(txt), "chars")
