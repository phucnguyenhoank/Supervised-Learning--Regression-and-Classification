
import sympy

J, w = sympy.symbols("J,w")

J = w**3
J

dJ_dw = sympy.diff(J, w)
dJ_dw

dJ_dw.subs([(w, 2)])



