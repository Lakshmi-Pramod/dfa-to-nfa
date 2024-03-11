from tabulate import tabulate
import pandas as pd
from automata.fa.dfa import DFA
from graphviz import Digraph
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

df=dfa
print(tabulate(ntable, headers='keys', tablefmt='fancy_grid'))
print(ini,'\n',set(f))
dfa = DFA(
    states=set(keys),
    input_symbols=set(path),
    transitions=dfa,
    initial_state=ini,
    final_states=set(f)
)
dot = Digraph(comment='DFA')


for state in dfa.states:
    if state in dfa.final_states:
        dot.node(state, shape='doublecircle')
    else:
        dot.node(state)

for start_state, transitions in dfa.transitions.items():
    for input_symbol, end_state in transitions.items():
        dot.edge(start_state, end_state, label=input_symbol)


dot.format = 'png'  
dot.render('dfa', cleanup=True)

print("DFA graph visualization saved as 'dfa.png'")

