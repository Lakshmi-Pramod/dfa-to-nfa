from automata.fa.dfa import DFA
from graphviz import Digraph


dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q1'},
        'q2': {'0': 'q0', '1': 'q3'},
        'q3': {'0': 'q3', '1': 'q3'}
    },
    initial_state='q0',
    final_states={'q3'}
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
