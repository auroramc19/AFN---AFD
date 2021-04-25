# AFN---AFD
Transformación de autómata finito no determinista a autómata finito determinista.

afn-afd_1.py -> AFN = ({q0, q1}, {a, b}, q0, {q1}, {(q0, a, {q0, q1}), (q0, b, {q1}), (q1, b, {q0, q1})})
afn-afd_2.py -> AFN = ({q0, q1, q2, q3, q4}, {a, b}, q0, {q2, q4}, {(q0, a, {q0, q3}), (q0, b, {q0, q1}), (q1, b, {q2}), (q2, a, {q2}),(q2, b, {q2}), (q3, a, {q4}), (q4, a, {q4}), (q4,b,{q4})}


