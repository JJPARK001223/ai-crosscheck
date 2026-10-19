import json,re,os
D=os.path.dirname(os.path.abspath(__file__))
def load():
    U=json.load(open(os.path.join(D,'units_all.json'),encoding='utf-8'))+json.load(open(os.path.join(D,'in','b00.json'),encoding='utf-8'))
    U.sort(key=lambda u:u['id'])
    return U
def groups(U):
    G=[[U[0]]]
    for u in U[1:]:
        a=G[-1][-1];ea=a['en'].rstrip();sb=u['en'].lstrip()
        pa=int(a['id'][1:4]);pb=int(u['id'][1:4])
        m=False
        if re.search(r'\bin\.$',ea) and pa==pb and (sb[:1]=='(' or sb[:1].islower() or sb[:1].isdigit()): m=True
        elif re.search(r'U\.S\.$',ea): m=True
        elif pa!=pb and sb[:1].islower() and not re.search(r'[.:?!)\]]$',ea) and not ea.startswith('•'): m=True
        elif pa!=pb and sb[:1].islower() and ea.startswith('•') and not re.search(r'[.:?!)\]]$',ea): m=True
        if m: G[-1].append(u)
        else: G.append([u])
    # 수동 추가 병합
    for ex in (['p038_04','p038_05','p038_06'],):
        gi=[k for k,g in enumerate(G) if g[0]['id']==ex[0]]
        ids=set(ex)
        if gi:
            k=gi[0]
            allu=[x for g in G[k:k+3] for x in g if x['id'] in ids]
            G[k:k+3]=[allu]+[g for g in G[k:k+3] if not any(x['id'] in ids for x in g)]
    return G
if __name__=='__main__':
    G=groups(load());m=[g for g in G if len(g)>1]
    print(len(G),len(m))
    for g in m: print([x['id'] for x in g],'|'.join(x['en'][-30:] if k==0 else x['en'][:30] for k,x in enumerate(g)))
