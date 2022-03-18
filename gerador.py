"""
A gramática abaixo no formato EBNF possui um conjunto infinito de exemplos.

start : fizz buzz

fizz  : "fizz" buzz 
      | ...

buzz  : "buzz" fizz
      | ...

Crie um programa que gere strings aleatórias desta linguagem. O programa deve ser capaz
de gerar **TODAS** strings possíveis e **SOMENTE STRINGS VÁLIDAS**, mesmo que a 
probabilidade de gerar um exemplo específico seja muito baixa. 
"""
import random


def random_example() -> str:
    return "..."


if __name__ == "__main__":
    for i in range(1, 11):
        print(f"{i}) {random_example()}")
