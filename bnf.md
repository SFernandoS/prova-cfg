# Gramáticas BNF

Considere as gramáticas EBNF abaixo escritas no formato EBNF. Remova todos os operadores extendidos, *, +, [], ?, etc e reescreva as gramáticas na notação BNF. Não é necessário modificar as gramáticas que já obedecem à notação BNF.

Considere que os símbolos não-terminais são escritos em letras minúsculas e os terminais em letras maiúsculas. Você pode criar novas regras, se necessário. Utilize ε para representar as produções vazias.

## Gramáticas

**G1**
```
s : A s B
  | A B
```

**G2**
```
s : A+
```

**G3**
```
s : A*
```

**G4**
```
s : "[" [A ("," A)* ] "]"
```

**G5**
```
s : "if" A "then" A [ "else" ( s | A ) ]
```

## Pontuação

* cfg-bnf: 1pt por item resolvido corretamente
* cfg-ebnf: 1pt se acertar G2 e G3 e 1pt se acertar G4
* cfg-list: 1pt se acertar G4