from sympy import symbols, And, Or, Not, Implies, Equivalent
from sympy.logic.boolalg import truth_table, to_dnf, to_cnf
from sympy import satisfiable

p, q, r = symbols('p q r')

expr1 = And(p, q)
expr2 = Or(p, q)
expr3 = Implies(p, q)
expr4 = Equivalent(p, q)


values = {p: True, q: False, r: True}

print("Expression 1 (p AND q):", expr1.subs(values))
print("Expression 2 (p OR q):", expr2.subs(values))
print("Expression 3 (p → q):", expr3.subs(values))
print("Expression 4 (p ↔ q):", expr4.subs(values))


print("\nSatisfiable expressions:")
print("Expr1:", satisfiable(expr1))
print("Expr3:", satisfiable(expr3))

print("\nAre expr1 and expr2 equivalent?")
print(Equivalent(expr1, expr2))

print("\nDNF of (p AND q) OR r:")
print(to_dnf(Or(expr1, r)))

print("\nCNF of (p AND q) OR r:")
print(to_cnf(Or(expr1, r)))
