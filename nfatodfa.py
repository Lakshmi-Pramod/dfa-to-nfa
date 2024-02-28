from tabulate import tabulate
import pandas as pd
nfa={}
states=int(input("Enter number of states:"))
trans=int(input("Enter number of transistions:"))
for i in range(0,states):
    s=input("Enter state name:")
    nfa[s]={}
    for j in range(0,trans):
        p=input("Enter the path:")
        e=input("Enter the state after transition ({0},{1}):".format(s,p))
        nfa[s][p]=e.split()

ntable=pd.DataFrame(nfa).transpose()
print(ntable)
ini=input("Enter initial state:")
f=input("Enter final state:").split()
dfa={}
path=list(nfa[ini].keys())
keys=list(nfa.keys())
k=[]
k.append(ini)
index=0
dfa = {}
v = []  # Track visited states

k = [ini]
while k:
    cs = k.pop()
    if cs in v:
        continue

    v.append(cs)
    dfa[cs] = {}

    for p in path:
        ns = set()
        for s in cs.split():
            if s in nfa and p in nfa[s]:
                ns.update(nfa[s][p])
        end=" ".join(sorted(list(ns)))
        dfa[cs][p]=end
        if (end not in v) and (end not in k):
            k.append(end)

ntable=pd.DataFrame(dfa).transpose()
ntable.fillna(value='-')
print(tabulate(ntable, headers='keys', tablefmt='fancy_grid'))
