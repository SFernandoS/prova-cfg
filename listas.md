# Listas

A gramática abaixo descreve listas de E's em uma sintaxe compatível com o JSON.

```lark
lst : "[" [ E ("," E)* ] "]"
    
%ignore /\s+/
```

Esta representação é tipicamente aceita na maior parte das linguagens de programação. No entanto, cada linguagem aceita pequenas variações tipicamente diferentes entre si. Adapte a gramática acima para os casos abaixo.

Você pode criar novos símbolos não-terminais, caso ache necessário ou desejável.

**Python**

Semelhante ao caso anterior, mas aceita uma vírgula opcional no final de uma lista.

```lark
lst : "[" [ E ("," E)* ] "]"
    
%ignore /\s+/
```

**...**


**...**

