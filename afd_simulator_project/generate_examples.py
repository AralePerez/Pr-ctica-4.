from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent / 'src'))
from automaton import Automaton, EPSILON
from io_formats import save_automaton

base = Path(__file__).resolve().parent

# Example 1: DFA ends with 1
A = Automaton(alphabet={'0','1'})
A.add_state('q0', initial=True, accept=False, x=180, y=160)
A.add_state('q1', initial=False, accept=True, x=420, y=160)
A.set_transition('q0','0','q0')
A.set_transition('q0','1','q1')
A.set_transition('q1','0','q0')
A.set_transition('q1','1','q1')

# Example 2: NFA contains ab
B = Automaton(alphabet={'a','b'})
B.add_state('q0', initial=True, x=100, y=180)
B.add_state('q1', x=300, y=100)
B.add_state('q2', accept=True, x=500, y=180)
B.add_transition('q0','a','q0')
B.add_transition('q0','b','q0')
B.add_transition('q0','a','q1')
B.add_transition('q1','b','q2')
B.add_transition('q2','a','q2')
B.add_transition('q2','b','q2')

# Example 3: epsilon-NFA toy example
C = Automaton(alphabet={'a','b'})
C.add_state('q0', initial=True, x=100, y=180)
C.add_state('q1', x=260, y=80)
C.add_state('q2', x=260, y=280)
C.add_state('q3', accept=True, x=460, y=180)
C.add_transition('q0', EPSILON, 'q1')
C.add_transition('q0', EPSILON, 'q2')
C.add_transition('q1', 'a', 'q3')
C.add_transition('q2', 'b', 'q3')

examples = {
    'dfa_ends_with_1': A,
    'nfa_contains_ab': B,
    'nfae_a_or_b': C,
}

for name, automaton in examples.items():
    for ext, folder in [('.jff','jff'),('.json','json'),('.xml','xml')]:
        save_automaton(automaton, base / 'examples' / folder / f'{name}{ext}')

(base / 'examples' / 'strings' / 'dfa_ends_with_1.txt').write_text('0\n1\n101\n100\n1111\n', encoding='utf-8')
(base / 'examples' / 'strings' / 'nfa_contains_ab.txt').write_text('ab\nbaab\nbbbb\naaaa\nabab\n', encoding='utf-8')
(base / 'examples' / 'strings' / 'nfae_a_or_b.txt').write_text('a\nb\nab\nε\n', encoding='utf-8')
print('OK')
