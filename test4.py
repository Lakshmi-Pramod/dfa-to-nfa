from tabulate import tabulate
import pandas as pd
from automata.fa.dfa import DFA
from graphviz import Digraph

# Initialize variables
nfa = {}
states = int(input("Enter number of states: "))
trans = int(input("Enter number of transitions: "))

# Input NFA transitions
for i in range(states):
    s = input("Enter state name: ")
    nfa[s] = {}
    for j in range(trans):
        p = input("Enter the path: ")
        e = input("Enter the state after transition ({0},{1}): ".format(s, p))
        nfa[s][p] = e.split()

# Print the NFA transitions
ntable = pd.DataFrame(nfa).transpose()
print("NFA Transitions:")
print(tabulate(ntable, headers='keys', tablefmt='fancy_grid'))

ini = input("Enter initial state: ")
f = input("Enter final state(s) separated by space: ").split()

# Construct DFA from NFA
dfa = {}
path = list(nfa[ini].keys())

k = [ini]
v = set()  # Track visited states as a set

while k:
    cs = k.pop()
    if cs in v:
        continue

    v.add(cs)  # Adding current state to visited states

    dfa[cs] = {}
    for p in path:
        ns = set()
        for s in cs.split():
            if s in nfa and p in nfa[s]:
                ns.update(nfa[s][p])
        end = " ".join(sorted(list(ns)))
        dfa[cs][p] = end
        if end not in v:
            k.append(end)

# Print the DFA transitions
dfa_table = pd.DataFrame(dfa).fillna('-')
print("\nDFA Transitions:")
print(tabulate(dfa_table, headers='keys', tablefmt='fancy_grid'))

# Construct DFA object
dfa_states = set(dfa.keys())  # States for the DFA
dfa_obj = DFA(
    states=dfa_states,
    input_symbols=set(path),
    transitions=dfa,
    initial_state=ini,
    final_states=set(f)
)

dot = Digraph(comment='DFA')

# Add nodes
for state in dfa_states:
    if state in dfa_obj.final_states:
        dot.node(state, shape='doublecircle')
    else:
        dot.node(state)

# Add edges
for start_state, transitions in dfa_obj.transitions.items():
    for input_symbol, end_state in transitions.items():
        dot.edge(start_state, end_state, label=input_symbol)

# Render and save the graph
dot.format = 'png'
dot.render('dfa', cleanup=True)

print("DFA graph visualization saved as 'dfa.png'")
