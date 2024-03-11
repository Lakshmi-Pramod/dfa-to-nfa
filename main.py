from automata.fa.dfa import DFA
from graphviz import Digraph
from tabulate import tabulate
import pandas as pd
nfa={}
states=int(input("Enter number of states:"))
st=input("Enter all states:")
st=st.split()
trans=int(input("Enter number of transistions:"))
path=input("Enter all possible transitions variables:")
path=path.split()
for i in range(0,states):
    s=input("Enter state name:")
    while s not in st:
        print("State not available")
        s=input("Re-enter state:")
    nfa[s]={}
    for j in range(0,trans):
        p=input("Enter the path:")
        while p not in path:
            print("Path not available")
            p=input("Re-enter path:")
        e=input("Enter the state after transition ({0},{1}):".format(s,p))
        e=e.split()
        while not(set(e)<=set(st)):
            print("State not available")
            e=input("Re-enter state:")
            e=e.split()
        nfa[s][p]=e

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
for i in list(dfa.keys()):
    if i=='':
        dfa['Null']=dfa[i]
        del dfa[i]
for i in list(dfa.keys()):
    for j in path:
        if dfa[i][j]=='':
            dfa[i][j]='Null'
states=dfa.keys()
input_symbols=path
transitions=dfa
initial_state=ini
final_states=f
dot_dfa = Digraph(comment='DFA')
for state in set(states):
    for i in f:
        if i in state:
            dot_dfa.node(state, shape='doublecircle')
    else:
        dot_dfa.node(state)

for start_state, transitions in transitions.items():
    for input_symbol, end_state in transitions.items():
        dot_dfa.edge(start_state, end_state, label=input_symbol)


dot_dfa.format = 'png'  
dot_dfa.render('dfa', cleanup=True)

print("DFA graph visualization saved as 'dfa.png'")
ntable=pd.DataFrame(dfa).transpose()
print(dfa)
dtable=ntable.fillna(0) 
print(tabulate(dtable, headers='keys', tablefmt='fancy_grid'))
