"""
A calculadora abaixo possui regras de precedência e associatividade incorretas. Modifique 
a gramática para consertar tais erros.

Associatividade:
    esquerda: + - * /
    direita: ^

Precedência (da menor para a maior): (+ -), (* /), (^)
"""
from lark import Lark, Transformer


grammar = Lark(
    r"""
?start : expr

?expr  : ...
       | ...

?term  : ...
       | ...

?unary : ...
       | ...

?atom  : NUMBER

NUMBER : /\d+(\.\d+)?/
"""
)


class Calc(Transformer):
    from operator import add, sub, mul, truediv as div, pow

    INT = int


def eval_calc(src):
    ast = grammar.parse(src)
    return Calc().transform(ast)


if __name__ == "__main__":
    ops = "+-*/^"

    for op1 in ops:
        for op2 in ops:
            src = f"1.0 {op1} 2.0 {op2} 3.0"
            calc = eval_calc(src)
            py = eval(src)
            if calc != py:
                print(f"{src} => {calc} (esperava {py})")
