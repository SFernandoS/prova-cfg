"""
Modifique a gramática abaixo e/o a classe de transformer para que as árvores
sintáticas dos exemplos abaixo obedeçam à estrutura desejada.
"""
from lark import Lark, Transformer, Tree


grammar = Lark(r"""

start : ...


""")

class AstTransformer(Transformer):
    ...


def parse(src: str) -> Tree:
    ast = grammar.parse(src)
    return AstTransformer().transform(ast)


def parse_pretty(src: str) -> str:
    ast = parse(src)
    try:
        render_pretty =  ast.pretty
    except AttributeError:
        return [str(ast)]
    else:
        return render_pretty().splitlines()
        

if __name__ == "__main__":
    assert parse_pretty("...") == ["..."]
    assert parse_pretty("...") == ["..."]